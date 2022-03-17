from typing import Any, Callable, Type
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from api.bots.BotApiProvider import BotApiProvider
from api.MainContext import main_context
from api.bots.BotManager import Interfaces
from loguru import logger as log


class MadHatterApiProvider(BotApiProvider):
    def __init__(self) -> None:
        self.api: CustomBotApi = main_context.haas.client.customBotApi
        self.indicators: tuple[str, ...] = (
            "macd",
            "rsi",
            "bBands"
        )

        self.options_names: dict[str, tuple[str, ...]] = dict({
            "Mad Hatter MACD": ("MACD Fast", "MACD Slow"),
            "Mad Hatter RSI": ("Buy level", "Sell level"),
            "Mad Hatter BBands": ("Length", "Dev.Up", "Dev.Down"),
        })

    def get_all_bots(self) -> tuple[MadHatterBot]:
        bots = self.process_error(
            self.api.get_all_custom_bots(), "Can't get bots list")
        res = tuple(bot for bot in bots if bot.botType == 15)
        log.info(f"{vars(res[0])=}")
        return res

    def get_all_interfaces(self, guid: str) -> tuple[Interfaces]:
        bot: MadHatterBot = self.get_refreshed_bot(guid)

        res = []
        for i in self.indicators:
            indicator = self.get_as_dict(bot, i)
            res.append(self.create_indicator(indicator))

        return tuple(res)

    def get_as_dict(self, bot: MadHatterBot, indicator_name: str) -> dict:
        if indicator_name == "bBands":
            return getattr(bot, indicator_name)
        return vars(getattr(bot, indicator_name))

    def create_indicator(self, d: dict) -> Indicator:
        log.info(f"{d=}")
        indicator_name: str = d["indicatorName"] \
            if "indicatorName" in d.keys() \
            else d["IndicatorName"]

        interfaces: list = d["indicatorInterface"] \
            if "indicatorInterface" in d.keys() \
            else d["IndicatorInterface"]


        options_dict: dict[str, dict[str, Any]] = dict(
            [(i["Title"], i) for i in interfaces]
        )

        indicator = Indicator()
        indicator.indicatorName = indicator_name
        indicator.enabled = True
        indicator.indicatorInterface = [
            self.create_option(options_dict[i])
            for i in self.options_names[indicator_name]
        ]

        return indicator

    def create_option(self, d: dict[str, Any]) -> IndicatorOption:
        option: IndicatorOption = IndicatorOption()
        option.title = d["Title"]
        option.value = d["Value"]
        option.step = d["Step"]
        return option


    def get_interfaces_by_type(
        self,
        guid: str,
        t: Type[Interfaces]
    ) -> tuple[Interfaces]:
        return self.get_all_interfaces(guid)

    def get_refreshed_bot(self, guid: str) -> MadHatterBot:
        response: HaasomeClientResponse = self.api.get_custom_bot(
            guid, EnumCustomBotType.MAD_HATTER_BOT
        )
        return self.process_error(response, "Error while refreshing bot")

    def get_edit_interface_method(self, t: Interfaces) -> Callable:
        # https://haasome-tools.github.io/haasomeapi/haasomeapi.apis.CustomBotApi.html
        # set_mad_hatter_indicator_parameter
        return super().get_edit_interface_method(t)

    def get_backtest_method(self) -> Callable:
        return self.api.backtest_custom_bot

    def process_error(
        self,
        response: HaasomeClientResponse,
        message: str
    ) -> Any:
        if response.errorCode is EnumErrorCode.SUCCESS:
            return response.result
        else:
            raise MadHatterException(
                f"{message}"
                f" [Error code: {response.errorCode} "
                f" Error message: {response.errorMessage}]"
            )


class MadHatterException(Exception): pass

