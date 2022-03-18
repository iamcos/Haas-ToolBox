from typing import Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot

from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.trade.TradeBotManager import TradeBotManager


class BotManagerCreationException(Exception):
    pass


def get_bot_manager(t: Type):
    # TODO: Go to dict, delete if else
    if t is TradeBot:
        return TradeBotManager()
    elif t is MadHatterBot:
        return MadHatterBotManager()
    else:
        raise BotManagerCreationException(
            f"Passed type {t} is wrong or not implemented"
        )

