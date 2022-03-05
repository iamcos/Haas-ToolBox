from typing import Any, Callable, NamedTuple, Union, cast
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from loguru import logger as log
from api.bots.trade.TradeBotManager import TradeBotException, TradeBotManager, Interfaces
from cli.bots.BotCli import BotCli
from cli.bots.tradebot.TradeBotBacktestCli import TradeBotBacktestCli

InterfacesForCli = Union[Safety, Indicator, Insurance, Separator, str]
MainMenuAction = Union[TradeBot, Interfaces, None, KeyboardInterrupt]


class TradeBotInterface(NamedTuple):
    name: str
    uppercase_name: str


class TradeBotCli(BotCli):
    def __init__(self) -> None:
        self.manager = TradeBotManager()
        self.backtester_cli = TradeBotBacktestCli(self.manager)

        self.interfaces_names: tuple[TradeBotInterface, ...] = tuple((
            TradeBotInterface("indicator", "Indicators"),
            TradeBotInterface("insurance", "Insurances"),
            TradeBotInterface("safety", "Safeties"),
        ))

        # TODO: Add 'Back' option
        self.main_menu = list([
            {
                "name": "Select interface",
                "value": self._select_interface
            },
            {
                "name": "Select another Trade Bot",
                "value": self._select_tradebot
            },
            {
                "name": "Quit",
                "value": KeyboardInterrupt
            }
        ])

    def menu(self) -> None:
        log.info("Starting Trade Bot CLI menu..")
        self._choose_tradebot()

        choice: MainMenuAction = self._bot_actions()

        self._process_user_choice(choice)

    def _bot_actions(self) -> MainMenuAction:
        log.info("Starting base bot setting..")
        choosed_action: Callable = inquirer.select(
            message="Select action:",
            choices=self.main_menu
        ).execute()

        return choosed_action()


    def _choose_tradebot(self) -> None:
        if self.manager.tradebot_not_selected():
            log.info("Trade bot isn't selected")
            self.manager.set_tradebot(self._select_tradebot())
        else:
            log.info("Trade bot selected")

    def _process_user_choice(
        self,
        choice: MainMenuAction
    ) -> None:
        if type(choice) is TradeBot:
            log.info("Choosed TradeBot")
            self.manager.set_tradebot(cast(TradeBot, choice))
            self.menu()
        elif type(choice) in [Indicator, Safety, Insurance]:
            log.info("Choosed Interface")
            self.backtester_cli.process_backtest(
                choice,
                self._parameter_selector(self._indicator_options(choice))
            )
        elif type(choice) is KeyboardInterrupt:
            log.info(f"Bye :)")
        else:
            log.warning(f"Unknow return value type: {type(choice)=}, {choice=}")


    # Bot selection, previous section is menu
    def _select_tradebot(self) -> TradeBot:
        log.info("Starting processing selecting bot..")

        bots_chain: list[dict[str, Union[TradeBot, str]]] = [
            {
                "name": f"{bot.name} {bot.priceMarket.displayName}",
                "value": bot
            }
            for bot in self.manager.get_available_tradebots()
        ]

        if not bots_chain:
            self._wait_bot_creating()
            return self._select_tradebot()

        return self._process_selecting_bot(bots_chain)

    def _wait_bot_creating(self) -> None:
        msg: str = "NO TRADE BOT DETECTED! Please create one by hand"

        while not self.manager.get_available_tradebots():
            log.warning(msg)
            inquirer.select(
                message="Select Trade Bot",
                choices=[
                    Separator(msg),
                    "Refresh bots list",
                ],
            ).execute()

        log.info("Trade bot detected!")

    def _process_selecting_bot(
        self,
        bots_chain: list[dict[str, Union[TradeBot, str]]]
    ) -> TradeBot:
        action: Union[TradeBot, str] = inquirer.select(
            message="Select Trade Bot:",
            choices=[*bots_chain, "Refresh Botlist"],
        ).execute()

        if type(action) is str:
            return self._select_tradebot()

        return cast(TradeBot, action)


    # Interface selection methods, previous section is menu
    def _select_interface(self) -> Interfaces:
        choices: list[InterfacesForCli] = self._interfaces_menu_options()
        action = inquirer.select(
            message="Select Interface:",
            choices=choices,
        ).execute()

        # if action == "Back":
        #     pass
            # return self._bot_actions()
        if action == "Refresh":
            self.manager.refresh_bot()
            return self._select_interface()

        return action

    def _interfaces_menu_options(self) -> list[InterfacesForCli]:
        choices: list[InterfacesForCli] = []

        for interface_name in self.interfaces_names:
            log.info(f"Interface name: {interface_name}")

            interfaces: tuple[Interfaces] = self.manager.get_available_interfaces(
                interface_name.uppercase_name.lower()
            )
            log.info(f"{interfaces=}")

            iterface_selector = self._display_indicator_selector(
                interface_name, interfaces
            )
            log.info(f"{iterface_selector=}")

            choices.extend(iterface_selector)

        log.info(f"{choices=}")
        choices.extend([Separator(""), "Refresh", Separator(""), "Back"])

        return choices




    # TODO: Create one DTO for interface name and tuple
    def _display_indicator_selector(
        self,
        interface_name: TradeBotInterface,
        interfaces: tuple[Interfaces, ...]
    ) -> list[InterfacesForCli]:

        if interfaces:
            log.info("Interfaces size more than 0")
            return self._menu_for_choosing_indicator(
                interface_name,
                interfaces
            )
        else:
            log.info("Interfaces size less than 0")
            msg: str = f"No {interface_name.uppercase_name} to select"
            return self._get_separated_msg(msg)

    def _menu_for_choosing_indicator(
        self,
        interface_name: TradeBotInterface,
        interfaces: tuple[Interfaces, ...]
    ) -> list[InterfacesForCli]:

        # name_format: str = "  {EnumIndicator(indicator." + \
        #                     interface_name + "Type).name}"

        indicators_menu: list[Any] = list([
            Separator(""),
            Separator(interface_name.uppercase_name + ":")
        ])

        for i in interfaces:
            if i.enabled:
                name: str = getattr(i, interface_name.name + "Name")
                indicators_menu.append({
                    "name": " " * 4 + name,
                    "value": i
                })
            else:
                indicators_menu.append(Separator(str(i) + " DISABLED"))

        log.info(f"")
        return indicators_menu

    def _get_separated_msg(self, msg: str) -> list[InterfacesForCli]:
        return list([
            Separator(""),
            Separator(msg),
        ])

    def _indicator_options(
        self,
        source: Interfaces
    ) -> list[IndicatorOption]:
        if type(source) is Safety:
            return source.safetyInterface

        elif type(source) is Indicator:
            return source.indicatorInterface

        elif type(source) is Insurance:
            return source.insuranceInterface

        raise TradeBotException(f"No Trade bot interface passed: {type(source)}")


    def _parameter_selector(
        self,
        indicator_options: list[IndicatorOption]
    ) -> IndicatorOption:

        choices: list[dict[str, Union[str, IndicatorOption]]] = [
            {
                "name": f"{i.title} : {i.value}",
                "value": i
            }
            for i in indicator_options
        ]

        selected_option: IndicatorOption = inquirer.select(
            message="Select Parameter",
            choices=choices,
        ).execute()

        log.info(f"{selected_option.__dict__=}")
        return selected_option



