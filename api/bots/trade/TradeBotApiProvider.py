import itertools
from typing import Any, Callable, Optional, Type
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from api.bots.BotApiProvider import BotApiProvider, BotException, Interfaces
from api.MainContext import main_context
from api.models import Bot
from api.bots.InterfaceWrapper import InterfaceWrapper


class TradeBotException(BotException): pass


class TradeBotApiProvider(BotApiProvider):
    def __init__(self) -> None:
        self.api: TradeBotApi = main_context.trade_bot_api
        self.interfaces: dict[Type, str] = {
            Indicator: "indicators",
            Insurance: "insurances",
            Safety: "safeties"
        }
        self.edit_methods: dict[Type, str] = {
            Indicator: "edit_bot_indicator_settings",
            Insurance: "edit_bot_insurance_settings",
            Safety: "edit_bot_safety_settings"
        }

    def get_all_bots(self) -> tuple[TradeBot, ...]:
        response: HaasomeClientResponse = self.api.get_all_trade_bots()

        return tuple(self.process_error(
            response, "Error while getting tradebots list"))

    def get_all_interfaces(self, guid: str) -> tuple[Interfaces, ...]:
        return tuple(itertools.chain(*[
            self.get_interfaces_by_type(guid, t)
            for t in set(self.interfaces.keys())
        ]))

    def get_interfaces_by_type(
        self,
        guid: str,
        t: Type[Interfaces]
    ) -> tuple[Interfaces]:
        return tuple(getattr(
            self.get_refreshed_bot(guid), self.interfaces[t]).values())

    def get_refreshed_bot(self, guid: str) -> TradeBot:
        response: HaasomeClientResponse = self.api.get_trade_bot(guid)
        return self.process_error(response, "Error while refreshing bot")

    def edit_interface(
        self,
        t: Interfaces,
        param_num: int,
        value: Any,
        bot_guid: str
    ) -> None:
        edit_func = getattr(self.api, self.edit_methods[type(t)])

        res = edit_func(bot_guid, InterfaceWrapper(t).guid, param_num, value)

        self.process_error(res, "Error while editing interface")

    def get_backtest_method(self) -> Callable:
        return self.api.backtest_trade_bot

    def process_error(
        self,
        response: Optional[HaasomeClientResponse | Any] = None,
        message: str = "Trade Bot Error"
    ) -> Any:
        if response is None:
            raise TradeBotException(message)

        if type(response) is HaasomeClientResponse:
            if response.errorCode is not EnumErrorCode.SUCCESS:
                raise TradeBotException(
                    f"{message}"
                    f" [Error code: {response.errorCode} "
                    f" Error message: {response.errorMessage}]"
                )

            return response.result

        return response

    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        return tuple([Indicator, Safety, Insurance])

    def clone_bot_and_save(self, bot: Bot) -> Bot:
        res = self.api.clone_trade_bot(
            bot.accountId,
            bot.guid,
            f"{bot.name} [{bot.roi}]",
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            bot.leverage,
            True, True, True, True, True
        )

        return self.process_error(res, "Clone bot error")

    def delete_bot(self, bot_guid: str) -> None:
        self.api.remove_trade_bot(bot_guid)

