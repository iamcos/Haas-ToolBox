from typing import Any, Callable, NamedTuple, Union, cast
from InquirerPy import get_style, inquirer
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from loguru import logger as log
from api.bots.trade.TradeBotManager import TradeBotManager, Interfaces
from cli.bots.BotCli import BotCli

InterfacesForCli = Union[Safety, Indicator, Insurance, Separator, str]

class TradeBotCli(BotCli):
    def __init__(self) -> None:
        self.manager: TradeBotManager = TradeBotManager()

        self.indicators_names: tuple[tuple[str, str], ...] = tuple((
            ("indicator", "Indicators"),
            ("insurance", "Insurances"),
            ("safety", "Safeties"),
        ))

        self.tradebot_setting_options: dict[str, Callable] = dict({
            "Select interface": self._select_interface,
            "Select another Trade Bot": self._select_tradebot,
            "Quit": KeyboardInterrupt,
        })

    def menu(self) -> None:
        if not self.manager.tradebot_selected():
            log.info("Trade bot isn't selected")
            self.manager.set_tradebot(self._select_tradebot())
        else:
            log.info("Trade bot selected")
            user_selection: str = inquirer.select(
                message="Select action:",
                choices=list(self.tradebot_setting_options.keys())
            ).execute()

            # TODO: Add 'Back' option
            self.tradebot_setting_options[user_selection]()


    def _select_tradebot(self) -> TradeBot:
        log.info("Starting selecting trade bot...")
        tradebots: list[TradeBot] = self.manager.get_available_tradebots()
        log.info(f"{tradebots=}")

        if tradebots is not None and len(tradebots) != 0:
            result = self._process_selecting_bot()
            if result != "Back" or "Refresh Botlist":
                # TODO: Bad practice, create Wrapper
                return cast(TradeBot, result)
            else:
                log.error("Not implemented choose. Invoking this method again")
                return self._select_tradebot()
        else:
            self._wait_creating()
            return self._select_tradebot()

    def _process_selecting_bot(self) -> Union[TradeBot, str]:
        log.info("Starting processing selecting bot..")
        tradebots: list[TradeBot] = self.manager.get_available_tradebots()
        log.info(f"{tradebots=}")
        bots_chain: list[dict[str, Union[str, TradeBot]]] = []
        price_source_format: str = "{}"

        # log.info(f"{tradebots[0].name=}")
        # price_source_format: str = """{{i}.name}"""
        # log.info(f"{price_source_format.format(tradebots[0])=}")

        for i in tradebots:
            bots_chain.append({
                "name": price_source_format.format(
                    i.name,
                    # FIXME
                    # EnumPriceSource(i.priceMarket.priceSource)
                ),
                "value": i,
            })

        log.info("salfkj")
        action: TradeBot = inquirer.select(
            message="Select Trade Bot",
            choices=[*bots_chain, "Refresh Botlist"],
        ).execute()

        return action


    def _wait_creating(self) -> None:
        msg: str = "NO TRADE BOT DETECTED! Please create one by hand"
        log.warning(msg)

        # Wait until customer will create bot and press "Refresh" btn
        inquirer.select(
            message="Select Trade Bot",
            choices=[
                Separator(msg),
                "Refresh bots list",
            ],
        ).execute()


    def _select_interface(self) -> Interfaces:
        choices: list[InterfacesForCli] = self._interfaces_menu_options()
        action = inquirer.select(
            message="Select Interface:",
            choices=choices,
            style=get_style({"seprator": "#658bbf bg:#ffffff"}),
        )
        return action.execute()


    def _interfaces_menu_options(self) -> list[InterfacesForCli]:
        choices: list[InterfacesForCli] = []

        for indicator in self.indicators_names:
            indicators: list[Interfaces] = self.manager \
                                .get_available_interfaces(indicator[1].lower())

            selected_indicator = self._display_indicator_selector(
                # indicator[0],
                # (indicator[1], indicators)
                indicator, indicators
            )

            choices.append(selected_indicator)

        choices.extend([Separator(""), "Back"])

        return choices


    def _parameter_selector(
            self, interfaces: list[IndicatorOption]) -> IndicatorOption:

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

    def _display_indicator_selector(self, indicator: tuple[str, str], tradebot_indicators) -> list[InterfacesForCli]:
        # TODO: Add method for getting tradebot indicators to manager
        # tradebot_indicators: tuple[str, list]
        if len(tradebot_indicators) > 0:
            return self._menu_for_choosing_indicator(
                indicator[0], tradebot_indicators
            )
        else:
            msg: str = f"No {tradebot_indicators[0]} to select"
            return self._get_separated_msg(msg )

    def _get_separated_msg(self, msg: str) -> list[Separator]:
        return list([
            Separator(""),
            Separator(msg),
            Separator(""),
        ])

    def _menu_for_choosing_indicator(self, indicator_name: str,
                tradebot_indicators: tuple[str, list]) -> list[Any]:

        name_format: str = "  {EnumIndicator(indicator." + \
                            indicator_name + "Type).name}"

        indicators_menu: list[Any] = list([
            Separator(""),
            Separator(tradebot_indicators[0] + ":")
        ])

        for i in tradebot_indicators[1]:
            if i.enabled:
                indicators_menu.append({
                    "name": name_format.format(i),
                    "value": i
                })
            else:
                indicators_menu.append(
                    Separator(indicator_name.format(i) + " DISABLED")
                )

        return indicators_menu

    def _get_indicator_options(self,
                               source) -> Union[list[IndicatorOption], None]:
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
        return backtest_steps(tradebot, 10, 0)

    @staticmethod
    def backtest_10_steps_up(tradebot: TradeBot) -> TradeBot:
        return backtest_steps(tradebot, 10, 1)

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
