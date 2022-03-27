from re import sub

from typing import Any, Callable, Optional, Type
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from api.bots.BotApiProvider import BotApiProvider, BotException
from api.MainContext import main_context
from api.models import Interfaces, Bot


class MadHatterException(BotException): pass


class MadHatterApiProvider(BotApiProvider):
    def __init__(self) -> None:
        self.api: CustomBotApi = main_context.haas.client.customBotApi
        self.indicators: tuple[str, ...] = (
            "macd",
            "rsi",
            "bBands"
        )

        self.options_names: dict[str, tuple[str, ...]] = dict({
            "Mad Hatter MACD": ("MACD Fast", "MACD Slow", "MACD Signal"),
            "Mad Hatter RSI": ("Length", "Buy level", "Sell level"),
            "Mad Hatter BBands": (
                "Length",
                "Dev.Up",
                "Dev.Down",
                "MA Type",
                "Require FCC",
                "Reset Middle",
                "Allow Mid Sells"
            ),
        })

    def get_all_bots(self) -> tuple[MadHatterBot]:
        bots = self.process_error(
            self.api.get_all_custom_bots(), "Can't get bots list")
        res = tuple(bot for bot in bots if bot.botType == 15)
        return res

    def get_all_interfaces(self, guid: str) -> tuple[Interfaces]:
        bot: MadHatterBot = self.get_refreshed_bot(guid)

        res = []
        for i in self.indicators:
            indicator = self.get_as_dict(bot, i)
            res.append(self.create_indicator(indicator))

        return tuple(res)

    def get_as_dict(self, bot: MadHatterBot, indicator_name: str) -> dict:
        interface = getattr(bot, indicator_name)
        if type(interface) is not dict:
            interface = vars(interface)
        return interface

    def create_indicator(self, d: dict) -> Indicator:
        if "indicatorName" in d.keys():
            indicator_name: str = d["indicatorName"]
        else:
            indicator_name: str = d["IndicatorName"]

        if "indicatorInterface" in d.keys():
            interfaces: list = d["indicatorInterface"]
        else:
            interfaces: list = d["IndicatorInterface"]

        options_dict: dict[str, dict[str, Any]] = dict(
            [(i["Title"], i) for i in interfaces]
        )

        indicator = Indicator()
        indicator.indicatorName = indicator_name
        indicator.enabled = True

        indicator.guid = indicator_name

        # max_option_num: int = max(self.options_names[indicator_name], key=lambda x: x[1])

        indicator.indicatorInterface = [
            self.create_option(options_dict[i])
            for i in self.options_names[indicator_name]
        ]

        return indicator

    def create_option(self, d: dict[str, Any]) -> IndicatorOption:
        option: IndicatorOption = IndicatorOption()
        option.title = d["Title"]
        option.value = d["Value"]
        option.options = d["Options"]

        if option.title in ("Buy level", "Sell level"):
            option.step = 1
        else:
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

    def edit_interface(
        self,
        t: Interfaces,
        param_num: int,
        value: Any,
        bot_guid: str
    ) -> None:

        edit_func = self._inject_interface_type(
            self._get_indicator_enum_type(t)
        )

        res = edit_func(bot_guid, param_num, value)

        self.process_error(res, "Error while editing interface")

    def _inject_interface_type(
        self,
        t: EnumMadHatterIndicators,
    ) -> Callable:
        return lambda a, b, c: self.api.set_mad_hatter_indicator_parameter(
            a, t, b, c
        )

    def _get_indicator_enum_type(self, t: Interfaces) -> EnumMadHatterIndicators:
        if type(t) is not Indicator:
            raise MadHatterException("Only indicators supported now")

        match t.indicatorName:
            case "Mad Hatter MACD":
                return EnumMadHatterIndicators.MACD
            case "Mad Hatter RSI":
                return EnumMadHatterIndicators.RSI
            case "Mad Hatter BBands":
                return EnumMadHatterIndicators.BBANDS

        raise MadHatterException(
            f"Wrong indicator for getting enum type: {t.indicatorName}"
        )

    def get_backtest_method(self) -> Callable:
        return self.api.backtest_custom_bot

    def process_error(
        self,
        response: Optional[HaasomeClientResponse | Any] = None,
        message: str = "Mad Hatter Error"
    ) -> Any:
        if response is None:
            raise MadHatterException(message)

        if type(response) is HaasomeClientResponse:
            if response.errorCode is not EnumErrorCode.SUCCESS:
                raise MadHatterException(
                    f"{message}"
                    f" [Error code: {response.errorCode} "
                    f" Error message: {response.errorMessage}]"
                )

            return response.result

        return response

    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        return tuple([Indicator])

    def clone_bot_and_save(self, bot: Bot) -> Bot:
        name: str = sub(r"\s\[.*\]", "", bot.name)

        res = self.api.clone_custom_bot(
            bot.accountId,
            bot.guid,
            EnumCustomBotType.MAD_HATTER_BOT,
            f"{name} [{self.get_refreshed_bot(bot.guid).roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage
        )

        return self.process_error(res, "Clone bot error")

    def delete_bot(self, bot_guid: str) -> None:
        self.api.remove_custom_bot(bot_guid)

