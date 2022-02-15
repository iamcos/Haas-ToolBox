from typing import Union

from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode
from numpy import deprecate

from api.MainContext import main_context
from loguru import logger as log


Interfaces = Union[Indicator, Safety, Insurance]


class TradeBotManager:
    def __init__(self):
        self._tradebot: Union[TradeBot, None] = None
        self.tradebot_api: TradeBotApi = main_context.trade_bot_api

    def tradebot_not_selected(self) -> bool:
        return self._tradebot is None

    def set_tradebot(self, tradebot: TradeBot):
        self._tradebot = tradebot

    @deprecate
    def clear_selected_tradebot(self):
        self._tradebot = None

    def get_available_tradebots(self) -> list[TradeBot]:
        """
        Gets bots objects from Haas online server
        """
        response: HaasomeClientResponse = self.tradebot_api.get_all_trade_bots()

        if response.errorCode is EnumErrorCode.SUCCESS:
            return response.result
        else:
            raise TradeBotException(
                "Error while getting tradebots list: "
                f"{response.errorCode=} "
                f"{response.errorMessage=}"
            )

    def get_available_interfaces(self, indicator: str) -> tuple[Interfaces]:
        """
        Gets values of all indicators, insurances and safeties
        from current tradebot
        """
        return tuple(getattr(self._tradebot, indicator).values())

    def refresh_bot(self) -> None:
        if self._tradebot is None:
            raise TradeBotException("Cant refresh bot, cause it is None")

        response = self.tradebot_api.get_trade_bot(self._tradebot.guid)

        if response.errorCode is EnumErrorCode.SUCCESS:
            self._tradebot = response.result
        else:
            raise TradeBotException(
                "Error while refreshing bot: "
                f"{response.errorCode=} "
                f"{response.errorMessage=}"
            )


class TradeBotException(Exception):
    pass
