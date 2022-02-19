from typing import Any, Callable, NamedTuple, Union, cast
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from loguru import logger as log
from api.bots.trade.TradeBotManager import TradeBotManager, Interfaces
from cli.bots.BotCli import BotCli

InterfacesForCli = Union[Safety, Indicator, Insurance, Separator, str]
MainMenuAction = Union[TradeBot, Interfaces, None, KeyboardInterrupt]


class InterfaceName(NamedTuple):
    name: str
    uppercase_name: str


class TradeBotCli(BotCli):
    def __init__(self) -> None:
        self.manager: TradeBotManager = TradeBotManager()

        self.interfaces_names: tuple[InterfaceName, ...] = tuple((
            InterfaceName("indicator", "Indicators"),
            InterfaceName("insurance", "Insurances"),
            InterfaceName("safety", "Safeties"),
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

        log.info("Starting base bot setting..")
        choosed_action: Callable = inquirer.select(
            message="Select action:",
            choices=self.main_menu
        ).execute()

        self._process_user_choice(choosed_action())

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
        elif type(choice) is KeyboardInterrupt:
            log.info(f"Bye :)")
        else:
            log.warning(f"Unknow return value type: {type(choice)=}, {choice=}")

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
    def _select_interface(self) -> Union[Interfaces, None]:
        choices: list[InterfacesForCli] = self._interfaces_menu_options()
        action = inquirer.select(
            message="Select Interface:",
            choices=choices,
        ).execute()

        if action == "Back":
            return self.menu()
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

    def _display_indicator_selector(
        self,
        interface_name: InterfaceName,
        interfaces: tuple[Interfaces]
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
        interface_name: InterfaceName,
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

    # Interfaces settings method
    def _parameter_selector(
        self,
        interfaces: list[IndicatorOption]
    ) -> IndicatorOption:

        choices: list[dict[str, Union[str, IndicatorOption]]] = []
        for i in interfaces:
            temp = dict({
                "name": f"{i.title} : {i.value}",
                "value": i
            })
            choices.append(temp)

        interfaceParameters: IndicatorOption = inquirer.select(
            message="Select Parameter",
            choices=choices,
        ).execute()

        log.info("selected_parameter number", interfaceParameters.__dict__)

        return interfaceParameters

    def _get_indicator_options(
        self,
        source
    ) -> Union[list[IndicatorOption], None]:
        if type(source) is Safety:
            return source.safetyInterface
        if type(source) is Indicator:
            return source.indicatorInterface
        if type(source) is Insurance:
            return source.insuranceInterface

    def _get_backtest_promt(self, selectedInterfaceParmeter) -> ListPrompt:
        return inquirer.select(
            message="",
            choices=[
                Separator(
                    f"{selectedInterfaceParmeter.title}:"
                    f"{selectedInterfaceParmeter.value} |"
                    f" step: {selectedInterfaceParmeter.step} |"
                    f" ROI: {self.tradebot.roi}%"
                ),
                Separator(f"Press right to backtest up"),
                Separator(f"Press left to backtest down"),
                Separator(f"Press ',' to backtest 10 steps down"),
                Separator(f"Press '.' to backtest 10 steps up"),
                Separator(f"Press '=' - backtesting length X 2"),
                Separator(f"Press '-' - backtesting length \\/ 2"),
                "Select another parameter",
            ],
        )

    class TradeBotBackTestMethods(NamedTuple):
        backtest_up: Callable
        backtest_down: Callable
        backtest_10_steps_down: Callable
        backtest_10_steps_up: Callable
        backtesting_length_x2: Callable
        backtesting_length_devide2: Callable

    @staticmethod
    def backtest_up(tradebot: TradeBot) -> TradeBot:
        # new_value = self._calculate_next_value(value, step, 0)
        # while new_value in used_values:
        #     new_value = self._calculate_next_value(value, step, 0)
        # api = self._edit_interface(interface)
        # tradebot = self._edit_param_value(
        #     api, interface, self.tradebot, param_num, new_value
        # )
        # tradebot = self._backtest_bot(self.tradebot, self.ticks)
        # log.info(
        #     f"{selectedInterfaceParmeter.title}"
        #     f" : {self.value} ROI:{tradebot.roi}%")
        # if float(tradebot.roi) != 0.0:
        #     value_roi.append([float(tradebot.roi), self.value, self.ticks])
        # used_values.append(self.value)
        return tradebot

    @staticmethod
    def backtest_down(tradebot: TradeBot) -> TradeBot:
        # self.value = self._calculate_next_value(self.value, step, 1)
        # while self.value in used_values:
        #     self.value = self._calculate_next_value(self.value, step, 1)
        # api = self._edit_interface(interface)
        # tradebot = self._edit_param_value(
        #     api, interface, self.tradebot, param_num, self.value
        # )
        # tradebot = self._backtest_bot(self.tradebot, self.ticks)
        # log.info(
        #     f"{selectedInterfaceParmeter.title}"
        #     f": {self.value} ROI:{tradebot.roi}%")
        # value_roi.append([float(tradebot.roi), self.value])
        # used_values.append(self.value)
        return tradebot

    @staticmethod
    def backtesting_length_x2(tradebot: TradeBot) -> TradeBot:
        # self.ticks = int(self.ticks * 2)
        # log.info(self.ticks)
        return tradebot

    @staticmethod
    def backtesting_length_devide2(tradebot: TradeBot) -> TradeBot:
        # self.ticks = int(self.ticks / 2)
        # log.info(self.ticks)
        return tradebot

    @staticmethod
    def backtest_10_steps_down(tradebot: TradeBot) -> TradeBot:
        return TradeBotCli.backtest_steps(tradebot, 10, 0)

    @staticmethod
    def backtest_10_steps_up(tradebot: TradeBot) -> TradeBot:
        return TradeBotCli.backtest_steps(tradebot, 10, 1)

    @staticmethod
    def backtest_steps(tradebot: TradeBot, steps: int, direction: int) -> TradeBot:
        # for _ in range(steps):
        #     self.value = self._calculate_next_value(self.value, step, direction)
        #     while self.value in used_values:
        #         self.value = self._calculate_next_value(
        #             self.value, step, direction)
        #     api = self._edit_interface(interface)
        #     tradebot = self._edit_param_value(
        #         api, interface, self.tradebot, param_num, self.value
        #     )
        #     tradebot = self._backtest_bot(self.tradebot, self.ticks)
        #     log.info(
        #         f"{selectedInterfaceParmeter.title}"
        #         f": {self.value} ROI:{tradebot.roi}%                  "
        #     )
        #     value_roi.append([float(tradebot.roi), self.value])
        #     used_values.append(self.value)
        return tradebot

    def _iterate_parameter(
            self, interface,
            selectedInterfaceParmeter,
            param_num,
            tradebot: TradeBot,
            methods: TradeBotBackTestMethods) -> TradeBot:

        used_values = []
        value_roi = []
        value = self._get_param_value(selectedInterfaceParmeter)
        step = self._get_param_step(selectedInterfaceParmeter)

        # FIXME: Move to special method
        action = self._get_backtest_promt(selectedInterfaceParmeter)

        @action.register_kb("right")
        def _(_):
            methods.backtest_up(tradebot)

        @action.register_kb("left")
        def _(_):
            methods.backtest_down(tradebot)

        @action.register_kb("escape")
        def _(_):
            pass

        @action.register_kb("=")
        def _(_):
            methods.backtesting_length_x2(tradebot)

        @action.register_kb("-")
        def _(_):
            methods.backtesting_length_devide2(tradebot)

        @action.register_kb(",")
        def _(_):
            methods.backtest_10_steps_down(tradebot)

        @action.register_kb(".")
        def _(_):
            methods.backtest_10_steps_up(tradebot)

        action = action.execute()

        if action == "Select another parameter":
            if len(value_roi) > 0:
                value = sorted(value_roi, key=lambda x: x[0], reverse=True)
                log.info(value)
                api = self._edit_interface(interface)
                self.tradebot = self._edit_param_value(
                    api, interface, self.tradebot, param_num, value[0][1]
                )
                self.edit_parameters()
        elif action == "Set best value by ROI":
            if len(value_roi) > 0:
                value = sorted(value_roi, key=lambda x: x[0], reverse=True)
                api = self._edit_interface(interface)
                self.tradebot = self._edit_param_value(
                    api, interface, self.tradebot, param_num, value[0][1]
                )
                log.info(value)
                self.edit_parameters()

        return tradebot

    def _get_param_value(self, selectedInterfaceParameter) -> float:
        return self._smart_round(
            float(selectedInterfaceParameter.step),
            float(selectedInterfaceParameter.value)
        )

    def _get_param_step(self, selectedInterfaceParameter) -> float:
        return self._smart_round(
            float(selectedInterfaceParameter.step),
            float(selectedInterfaceParameter.step)
        )

    def _smart_round(self, step: float, value: float) -> float:
        numbers_after_dot: int = len(str(step)[2:])
        return round(value, numbers_after_dot)

    def _calculate_next_value(self, value, step, direction):
        if direction == 0:
            return round(value + step, 4)
        if direction == 1:
            return round(value - step, 4)

    def _backtest_bot(self, tradebot, interval):
        return self.tradebotapi.backtest_trade_bot(
            tradebot.guid, interval).result

    # TODO: Refactor
    def _edit_param_value(
            self,
            api,
            interface,
            tradebot,
            param_num,
            new_val,
    ):
        result = api(tradebot.guid, interface.guid, param_num, new_val)
        return result.result
