import itertools
from functools import lru_cache
from api.domain.dtos import InterfaceOptionInfo
from api.domain.types import GUID, Bot, InterfaceOption, Interface
from api.exceptions import TradeBotException
from api.wrappers.interface_wrapper import InterfaceWrapper
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from re import sub
from typing import Any, NamedTuple, Type, cast


class TradeBotApiProvider:
    def __init__(self, api: TradeBotApi) -> None:
        self._api: TradeBotApi = api

        self.interfaces: dict[Type, str] = {
            Indicator: "indicators",
            Insurance: "insurances",
            Safety: "safeties"
        }
        self.edit_methods: dict[Type[Interface], str] = {
            Indicator: "edit_bot_indicator_settings",
            Insurance: "edit_bot_insurance_settings",
            Safety: "edit_bot_safety_settings"
        }

    def get_all_bots(self) -> tuple[TradeBot, ...]:
        response: HaasomeClientResponse = self._api.get_all_trade_bots()

        return tuple(self._process_response(
            response, "Error while getting tradebots list"))

    def get_all_bot_interfaces(self, bot_guid: GUID) -> tuple[Interface, ...]:
        bot: Bot = self.get_refreshed_bot(bot_guid)
        return tuple(itertools.chain(*[
            self.get_bot_interfaces_by_type(bot, t)
            for t in set(self.interfaces.keys())
        ]))

    def get_bot_interfaces_by_type(
        self,
        guid_or_bot: GUID | Bot,
        interface_type: Type[Interface]
    ) -> tuple[Interface]:
        bot: Bot

        if type(guid_or_bot) is GUID:
            bot = self.get_refreshed_bot(guid_or_bot)
        elif "guid" in vars(guid_or_bot):
            bot = cast(Bot, guid_or_bot)
        else:
            raise TradeBotException(
                    "Str or Bot must be passed as guid_or_bot, "
                    f"got {guid_or_bot}")


        return tuple(getattr(bot, self.interfaces[interface_type]).values())


    def get_refreshed_bot(self, bot_guid: GUID) -> TradeBot:
        response: HaasomeClientResponse = self._api.get_trade_bot(bot_guid)
        return self._process_response(response, "Error while refreshing bot")

    def update_bot_interface_option(
        self,
        option: InterfaceOption,
        bot_guid: GUID
    ) -> None:
        option_info = self._get_option_info(option, bot_guid)

        edit_func = getattr(
                self._api, self.edit_methods[type(option_info.interface)])

        res = edit_func(
                bot_guid,
                option_info.interface_guid,
                option_info.option_num,
                option.value)

        self._process_response(res, "Error while editing interface")

    def _get_option_info(
        self,
        option: InterfaceOption,
        bot_guid: GUID
    ) -> InterfaceOptionInfo:

        for interface in self.get_all_bot_interfaces(bot_guid):
            interface_wrapper: InterfaceWrapper = InterfaceWrapper(interface)
            options: tuple[InterfaceOption, ...] = interface_wrapper.options

            for opt_number, opt in enumerate(options):
                if opt.title == option.title: 
                    return InterfaceOptionInfo(
                            interface,
                            interface_wrapper.guid,
                            opt_number)

        raise TradeBotException(f"Option {option} not found")

    def get_available_interface_types(self) -> tuple[Type[Interface], ...]:
        return tuple([Indicator, Safety, Insurance])

    def clone_and_save_bot(self, bot: Bot) -> Bot:
        name: str = sub(r"\s\[.*\]", "", bot.name)

        res = self._api.clone_trade_bot(
            bot.accountId,
            bot.guid,
            f"{name} [{bot.roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage,
            True, True, True, True, True
        )

        return self._process_response(res, "Clone bot error")

    def delete_bot(self, bot_guid: GUID) -> None:
        self._api.remove_trade_bot(bot_guid)

    def backtest_bot(self, bot_guid: GUID, ticks: int) -> None:
        self._api.backtest_trade_bot(bot_guid, ticks)

    def _process_response(
        self,
        response: HaasomeClientResponse,
        message: str = "Trade Bot Error"
    ) -> Any:
        if response.errorCode is not EnumErrorCode.SUCCESS:
            raise TradeBotException(
                f"{message}"
                f" [Error code: {response.errorCode} "
                f" Error message: {response.errorMessage}]"
            )

        return response.result

