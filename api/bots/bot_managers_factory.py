from typing import Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from api.bots.BotApiProvider import Bot, BotApiProvider
from api.bots.BotManager import BotManager

from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.trade.TradeBotApiProvider import TradeBotApiProvider
from api.bots.mad_hatter.MadHatterApiProvider import MadHatterApiProvider
from api.bots.trade.TradeBotManager import TradeBotManager


class BotManagerCreationException(Exception): pass

class BotApiProviderCreationException(Exception): pass


def get_bot_manager(t: Type) -> BotManager:
    # TODO: Go to dict, delete if else
    if t is TradeBot:
        return TradeBotManager(t)
    elif t is MadHatterBot:
        return MadHatterBotManager(t)
    else:
        raise BotManagerCreationException(
            f"Passed type {t} is wrong or not implemented"
        )

def get_provider(t: Type[Bot]) -> BotApiProvider:
    if t is TradeBot:
        return TradeBotApiProvider()
    elif t is MadHatterBot:
        return MadHatterApiProvider()
    else:
        raise BotApiProviderCreationException(
            f"Passed type {t} is wrong or not implemented"
        )
