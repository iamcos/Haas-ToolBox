from typing import Union

from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from loguru import logger as log

from api.Haas import Haas


# TODO: Decompose to two classes for inquirer and buisness logic
class TradeBotEditor:
    """
    Trade Bot parameter manipulation class.
    Responsible for Trade Bot selection, parameter selection,
    keyboard interface to change parameter values and backtest_bot
    """

    def __init__(self):
        log.info("Initializing TradeBotEditor")
        self.haas: Haas = Haas()
        self.ticks = 0
        self.tradebotapi: TradeBotApi = TradeBotApi(
            self.haas.config_manager.url,
            self.haas.config_manager.secret
        )


class TradeBotParameterEditor:
    def __init__(self, tradebot: TradeBot, tradebotapi: TradeBotApi) -> None:
        self.ticks: int = 0
        self.tradebotapi = tradebotapi
        self.tradebot: TradeBot = tradebot

    def edit_parameters(self) -> TradeBot:
        interface: Union[Safety, Indicator,
                         Insurance] = self._interface_selector()
        param_interfaces = self._get_indicator_options(interface)
        param_num = None

        if param_interfaces:
            selectedInterface = self._parameter_selector(param_interfaces)
            for i, x in enumerate(param_interfaces):
                if x.title == selectedInterface.title:
                    param_num = i

            return self._iterate_parameter(
                interface, selectedInterface, param_num
            )
        return self.tradebot

    # def _interface_selector(self, tradebot: TradeBot) -> Union[Safety, Indicator, Insurance]:
    #     choices = self._get_interfaces_menu_options(tradebot)
    #     action = inquirer.select(
    #         message="Select Interface:",
    #         choices=choices,
    #         style=get_style({"seprator": "#658bbf bg:#ffffff"}),
    #     )
    #     return action.execute()

    # def _get_interfaces_menu_options(self) -> list[
    #         Union[Separator, Safety, Indicator, Insurance]]:

    #     choices: list[Any] = list()

    #     # if self.tradebot is not None:
    #     indicators_names: tuple = (
    #         ("indicator", "Indicators"),
    #         ("insurance", "Insurances"),
    #         ("safety", "Safeties"),
    #     )

    #     for indicator in indicators_names:
    #         choices.append(
    #             self._display_indicator_selector(indicator[0], indicator[1])
    #         )

    #     choices.extend([Separator(""), "Back"])

    #     return choices

    # def _display_indicator_selector(
    #         self, indicator_name: str, plurar_indicator_name: str) -> list[Any]:

    #     indicators_dict: dict[str, Any] = getattr(
    #         self.tradebot, plurar_indicator_name.lower()
    #     )

    #     if len(indicators_dict) > 0:
    #         return self.menu_for_choosing_indicator(
    #             indicator_name, plurar_indicator_name
    #         )
    #     else:
    #         return [
    #             Separator(""),
    #             Separator(f"No {plurar_indicator_name} to select"),
    #             Separator(""),
    #         ]

    # def menu_for_choosing_indicator(self, indicator_name: str,
    #                                 plurar_indicator_name: str) -> list[Any]:

    #     name_format: str = "  {EnumIndicator(indicator." + \
    #         indicator_name + "Type).name}"
    #     indicators_menu: list[Any] = list([
    #         Separator(""),
    #         Separator(plurar_indicator_name + ":")
    #     ])

    #     for i in getattr(self.tradebot, plurar_indicator_name.lower()).values():
    #         if i.enabled:
    #             indicators_menu.append({
    #                 "name": name_format.format(i), "value": i
    #             })
    #         else:
    #             indicators_menu.append(
    #                 Separator(indicator_name.format(i) + " DISABLED")
    #             )

    #     return indicators_menu

    # def _get_indicator_options(self, source) -> Union[
    #         list[IndicatorOption], None]:
    #     if type(source) is Safety:
    #         return source.safetyInterface
    #     if type(source) is Indicator:
    #         return source.indicatorInterface
    #     if type(source) is Insurance:
    #         return source.insuranceInterface

    # def _parameter_selector(
    #         self, interface: list[IndicatorOption]) -> IndicatorOption:

    #     interfaceParameters: IndicatorOption = inquirer.select(
    #         message="Select Parameter",
    #         choices=[{"name": f"{i.title} : {i.value}", "value": i}
    #                  for i in interface],
    #     ).execute()
    #     log.info("selected_parameter number", interfaceParameters.__dict__)
    #     return interfaceParameters

    # def _iterate_parameter(
    #         self, interface,
    #         selectedInterfaceParmeter,
    #         param_num) -> TradeBot:

    #     used_values = []
    #     value_roi = []
    #     self.value = self._get_param_value(selectedInterfaceParmeter)
    #     step = self._get_param_step(selectedInterfaceParmeter)
    #     action = inquirer.select(
    #         message="",
    #         choices=[
    #             Separator(
    #                 f"{selectedInterfaceParmeter.title}:"
    #                 f"{selectedInterfaceParmeter.value} |"
    #                 f" step: {selectedInterfaceParmeter.step} |"
    #                 f" ROI: {self.tradebot.roi}%"
    #             ),
    #             Separator(f"Press right to backtest up"),
    #             Separator(f"Press left to backtest down"),
    #             Separator(f"Press '.' to backtest 10 steps down"),
    #             Separator(f"Press '.' to backtest 10 steps up"),
    #             Separator(f"Press '=' - backtesting length X 2"),
    #             Separator(f"Press '-' - backtesting length \\/ 2"),
    #             "Select another parameter",
    #         ],
    #     )

    #     @action.register_kb("right")
    #     def _(_):
    #         self.value = self._calculate_next_value(self.value, step, 0)
    #         while self.value in used_values:
    #             self.value = self._calculate_next_value(self.value, step, 0)
    #         api = self._edit_interface(interface)
    #         tradebot = self._edit_param_value(
    #             api, interface, self.tradebot, param_num, self.value
    #         )
    #         tradebot = self._backtest_bot(self.tradebot, self.ticks)
    #         log.info(
    #             f"{selectedInterfaceParmeter.title}"
    #             f" : {self.value} ROI:{tradebot.roi}%")
    #         if float(tradebot.roi) != 0.0:
    #             value_roi.append([float(tradebot.roi), self.value, self.ticks])
    #         used_values.append(self.value)

    #     @action.register_kb("left")
    #     def _(_):
    #         self.value = self._calculate_next_value(self.value, step, 1)
    #         while self.value in used_values:
    #             self.value = self._calculate_next_value(self.value, step, 1)
    #         api = self._edit_interface(interface)
    #         tradebot = self._edit_param_value(
    #             api, interface, self.tradebot, param_num, self.value
    #         )
    #         tradebot = self._backtest_bot(self.tradebot, self.ticks)
    #         log.info(
    #             f"{selectedInterfaceParmeter.title}"
    #             f": {self.value} ROI:{tradebot.roi}%")
    #         value_roi.append([float(tradebot.roi), self.value])
    #         used_values.append(self.value)

    #     @action.register_kb("escape")
    #     def _(_):
    #         pass

    #     @action.register_kb("=")
    #     def _(_):
    #         self.ticks = int(self.ticks * 2)
    #         log.info(self.ticks)

    #     @action.register_kb("-")
    #     def _(_):
    #         self.ticks = int(self.ticks / 2)
    #         log.info(self.ticks)

    #     @action.register_kb(",")
    #     def _(_):
    #         for _ in range(10):
    #             self.value = self._calculate_next_value(self.value, step, 1)
    #             while self.value in used_values:
    #                 self.value = self._calculate_next_value(
    #                     self.value, step, 1)
    #             api = self._edit_interface(interface)
    #             tradebot = self._edit_param_value(
    #                 api, interface, self.tradebot, param_num, self.value
    #             )
    #             tradebot = self._backtest_bot(self.tradebot, self.ticks)
    #             log.info(
    #                 f"{selectedInterfaceParmeter.title}"
    #                 f": {self.value} ROI:{tradebot.roi}%                  "
    #             )
    #             value_roi.append([float(tradebot.roi), self.value])
    #             used_values.append(self.value)

    #     @action.register_kb(".")
    #     def _(_):
    #         for _ in range(10):
    #             self.value = self._calculate_next_value(self.value, step, 0)
    #             while self.value in used_values:
    #                 self.value = self._calculate_next_value(
    #                     self.value, step, 0)
    #             api = self._edit_interface(interface)
    #             tradebot = self._edit_param_value(
    #                 api, interface, self.tradebot, param_num, self.value
    #             )
    #             tradebot = self._backtest_bot(self.tradebot, self.ticks)
    #             log.info(
    #                 f"{selectedInterfaceParmeter.title}"
    #                 f" : {self.value} ROI:{tradebot.roi}%                  "
    #             )
    #             value_roi.append([float(tradebot.roi), self.value])
    #             used_values.append(self.value)

    #     action = action.execute()
    #     if action == "Select another parameter":
    #         if len(value_roi) > 0:
    #             value = sorted(value_roi, key=lambda x: x[0], reverse=True)
    #             log.info(value)
    #             api = self._edit_interface(interface)
    #             self.tradebot = self._edit_param_value(
    #                 api, interface, self.tradebot, param_num, value[0][1]
    #             )
    #             self.edit_parameters()
    #     elif action == "Set best value by ROI":
    #         if len(value_roi) > 0:
    #             value = sorted(value_roi, key=lambda x: x[0], reverse=True)
    #             api = self._edit_interface(interface)
    #             self.tradebot = self._edit_param_value(
    #                 api, interface, self.tradebot, param_num, value[0][1]
    #             )
    #             log.info(value)
    #             self.edit_parameters()

    # def _edit_interface(self, source):
    #     if type(source) is Safety:
    #         return self.tradebotapi.edit_bot_safety_settings
    #     if type(source) is Indicator:
    #         return self.tradebotapi.edit_bot_indicator_settings
    #     if type(source) is Insurance:
    #         return self.tradebotapi.edit_bot_insurance_settings

    # def _get_param_value(self, selectedInterfaceParameter) -> float:
    #     return self._smart_round(
    #         float(selectedInterfaceParameter.step),
    #         float(selectedInterfaceParameter.value)
    #     )

    # def _get_param_step(self, selectedInterfaceParameter) -> float:
    #     return self._smart_round(
    #         float(selectedInterfaceParameter.step),
    #         float(selectedInterfaceParameter.step)
    #     )

    # def _smart_round(self, step: float, value: float) -> float:
    #     numbers_after_dot: int = len(str(step)[2:])
    #     return round(value, numbers_after_dot)

    # def _calculate_next_value(self, value, step, direction):
    #     if direction == 0:
    #         return round(value + step, 4)
    #     if direction == 1:
    #         return round(value - step, 4)

    # def _backtest_bot(self, tradebot, interval):
    #     return self.tradebotapi.backtest_trade_bot(
    #         tradebot.guid, interval).result

    # # TODO: Refactor
    # def _edit_param_value(
    #         self,
    #         api,
    #         interface,
    #         tradebot,
    #         param_num,
    #         new_val,
    # ):
    #     result = api(tradebot.guid, interface.guid, param_num, new_val)
    #     return result.result
