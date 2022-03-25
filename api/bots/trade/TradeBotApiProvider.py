import itertools
from typing import Any, Callable, Optional, Type
from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from api.bots.BotApiProvider import BotApiProvider, Interfaces
from api.MainContext import main_context


class TradeBotApiProvider(BotApiProvider):
    def __init__(self) -> None:
        self.tradebot_api: TradeBotApi = main_context.trade_bot_api
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
        response: HaasomeClientResponse = self.tradebot_api.get_all_trade_bots()

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
        response: HaasomeClientResponse = self.tradebot_api.get_trade_bot(guid)
        return self.process_error(response, "Error while refreshing bot")

    def get_edit_interface_method(self, t: Interfaces) -> Callable:
        return getattr(self.tradebot_api, self.edit_methods[t])

    def get_backtest_method(self) -> Callable:
        return self.tradebot_api.backtest_trade_bot

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


class TradeBotException(Exception): pass

