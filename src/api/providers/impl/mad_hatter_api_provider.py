from api.domain.dtos import InterfaceOptionInfo
from api.domain.types import GUID, Interface, Bot, InterfaceOption
from api.exceptions import MadHatterException
from api.wrappers.interface_wrapper import InterfaceWrapper
from typing import Any, Type, cast
from re import sub
from haasomeapi.apis.CustomBotApi import CustomBotApi
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators


class MadHatterApiProvider:
    def __init__(self, api: CustomBotApi) -> None:
        self._api: CustomBotApi = api

        self.indicators: tuple[str, ...] = tuple([
            "macd",
            "rsi",
            "bBands"
        ])

        self.options_names: dict[str, tuple[str, ...]] = dict({
            "Mad Hatter MACD": (
                "MACD Fast",
                "MACD Slow",
                "MACD Signal"
            ),
            "Mad Hatter RSI": (
                "Length",
                "Buy level",
                "Sell level"
            ),
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

    def get_all_bots(self) -> tuple[MadHatterBot, ...]:
        bots = self._process_error(
            self._api.get_all_custom_bots(), "Can't get bots list")
        return tuple(bot for bot in bots if bot.botType == 15)

    def get_all_bot_interfaces(self, bot_guid: GUID) -> tuple[Interface, ...]:
        bot: MadHatterBot = self.get_refreshed_bot(bot_guid)
        res: list[Interface] = []

        for i in self.indicators:
            indicator = self._get_as_dict(bot, i)
            res.append(self._create_indicator(indicator))

        return tuple(res)

    def _get_as_dict(self, bot: Bot, indicator_name: str) -> dict:
        interface = getattr(bot, indicator_name)
        if type(interface) is not dict:
            interface = vars(interface)
        return interface

    def _create_indicator(self, d: dict) -> Indicator:
        if "indicatorName" in d.keys():
            indicator_name: str = d["indicatorName"]
        else:
            indicator_name: str = d["IndicatorName"]

        if "indicatorInterface" in d.keys():
            interfaces: list = d["indicatorInterface"]
        else:
            interfaces: list = d["IndicatorInterface"]

        options_dict: dict[str, dict[str, Any]] = {
            i["Title"]: i
            for i in interfaces
        }

        indicator = Indicator()
        indicator.indicatorName = indicator_name
        indicator.enabled = True # type: ignore
        indicator.guid = indicator_name

        indicator.indicatorInterface = [
            self._create_option(options_dict[i])
            for i in self.options_names[indicator_name]
        ]

        return indicator

    def _create_option(self, d: dict[str, Any]) -> IndicatorOption:
        option: IndicatorOption = IndicatorOption()
        option.title = d["Title"]
        option.value = d["Value"]
        option.options = d["Options"]

        if option.title in ("Buy level", "Sell level"):
            option.step = 1 # type: ignore
        else:
            option.step = d["Step"] # type: ignore

        return option

    def get_bot_interfaces_by_type(
        self,
        guid_or_bot: GUID | Bot,
        interface_type: Type[Interface]
    ) -> tuple[Interface]:
        if interface_type != Indicator:
            raise MadHatterException("Only indicators supported "
                                     f"got {interface_type}")

        guid: GUID

        if type(guid_or_bot) is GUID:
            guid = guid_or_bot
        elif "guid" in vars(guid_or_bot):
            guid = cast(Bot, guid_or_bot).guid
        else:
            raise MadHatterException(
                    "GUID or Bot must be passed as guid_or_bot, "
                    f"got {guid_or_bot}")

        return self.get_all_bot_interfaces(guid)

    def get_refreshed_bot(self, bot_guid: GUID) -> MadHatterBot:
        response: HaasomeClientResponse = self._api.get_custom_bot(
            bot_guid, EnumCustomBotType.MAD_HATTER_BOT
        )
        return self._process_error(response, "Error while refreshing bot")

    def update_bot_interface_option(
        self,
        bot_guid: GUID,
        interface_name: str,
        option: InterfaceOption
    ) -> None:

        option_info = self._get_option_info(interface_name, option, bot_guid)

        interface_enum_type = self._get_interface_enum_type(
                option_info.interface)

        print(vars(option), bot_guid, option_info, interface_enum_type)

        res = self._api.set_mad_hatter_indicator_parameter(
            bot_guid,
            interface_enum_type,
            option_info.option_num,
            option.value
        )

        self._process_error(res, "Error while editing interface")

    def _get_option_info(
        self,
        interface_name: str,
        option: InterfaceOption,
        bot_guid: GUID
    ) -> InterfaceOptionInfo:
        interface = next((
            interface
            for interface in self.get_all_bot_interfaces(bot_guid)
            if InterfaceWrapper(interface).name == interface_name
        ))

        wrapped = InterfaceWrapper(interface)
        options: tuple[InterfaceOption, ...] = wrapped.options

        for opt_number, opt in enumerate(options):
            if opt.title == option.title: 
                return InterfaceOptionInfo(
                        interface,
                        wrapped.guid,
                        opt_number)

        raise MadHatterException(f"Option {option.title} not found")

    def _get_interface_enum_type(
        self,
        interface: Interface
    ) -> EnumMadHatterIndicators:
        if type(interface) is not Indicator:
            raise MadHatterException("Only indicators supported now")

        match interface.indicatorName:
            case "Mad Hatter MACD":
                return EnumMadHatterIndicators.MACD
            case "Mad Hatter RSI":
                return EnumMadHatterIndicators.RSI
            case "Mad Hatter BBands":
                return EnumMadHatterIndicators.BBANDS

        raise MadHatterException(
            f"Wrong indicator for getting enum type: {interface.indicatorName}"
        )

    def get_available_interface_types(self) -> tuple[Type[Interface], ...]:
        return tuple([Indicator])

    def clone_and_save_bot(self, bot_or_guid: Bot | GUID) -> Bot:
        if type(bot_or_guid) is GUID:
            bot = self.get_refreshed_bot(bot_or_guid)
        else:
            bot = cast(Bot, bot_or_guid)

        name: str = sub(r"\s\[.*\]", "", bot.name)

        res = self._api.clone_custom_bot(
            bot.accountId,
            bot.guid,
            EnumCustomBotType.MAD_HATTER_BOT,
            f"{name} [{self.get_refreshed_bot(bot.guid).roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage
        )

        return self._process_error(res, "Clone bot error")

    def delete_bot(self, bot_guid: str) -> None:
        self._api.remove_custom_bot(bot_guid)

    def backtest_bot(self, bot_guid: GUID, ticks: int) -> None:
        self._api.backtest_custom_bot(bot_guid, ticks)

    def _process_error(
        self,
        response: HaasomeClientResponse,
        message: str = "Mad Hatter Error"
    ) -> Any:
        if response.errorCode is not EnumErrorCode.SUCCESS:
            raise MadHatterException(
                f"{message}"
                f" [Error code: {response.errorCode} "
                f" Error message: {response.errorMessage}]"
            )

        return response.result

