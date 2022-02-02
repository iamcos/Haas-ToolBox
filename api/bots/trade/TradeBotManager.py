from typing import Union

from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse

from api.MainContext import main_context
from loguru import logger as log

Interfaces = Union[Indicator, Safety, Insurance]

class TradeBotManager:
    def __init__(self):
        self._tradebot: Union[TradeBot, None] = None
        self.tradebot_api: TradeBotApi = main_context.trade_bot_api

    def tradebot_selected(self) -> bool:
        return self._tradebot is not None

    def set_tradebot(self, tradebot: TradeBot):
        self._tradebot = tradebot

    def get_available_tradebots(self) -> list[TradeBot]:
        # TODO: Maybe use caching, not every time request
        # TODO: Add error catching
        tradebots_res: HaasomeClientResponse = self.tradebot_api.all_tradebots()

        log.info(
            f'ErrorCode: {tradebots_res.errorCode}, '
            f'ErrorMessage: {tradebots_res.errorMessage}'
        )

        return tradebots_res.result

    def get_available_interfaces(self, indicator: str) -> list[Interfaces]:
        """
        Gets values of all indicators, insurances and safeties
        from current tradebot
        """
        return getattr(self._tradebot, indicator).values()
