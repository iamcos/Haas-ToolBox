from typing import Type

from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot

from api.bots.BotApiProvider import BotApiProvider
from api.bots.trade.TradeBotApiProvider import TradeBotApiProvider
from api.bots.mad_hatter.MadHatterApiProvider import MadHatterApiProvider
from api.models import Bot


class BotApiProviderCreationException(Exception): pass


def get_provider(t: Type[Bot]) -> BotApiProvider:
    if t is TradeBot:
        return TradeBotApiProvider()
    elif t is MadHatterBot:
        return MadHatterApiProvider()
    else:
        raise BotApiProviderCreationException(
            f"Passed type {t} is wrong or not implemented"
        )

