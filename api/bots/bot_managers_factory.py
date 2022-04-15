from typing import Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from api.bots.BotManager import BotManager

from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.trade.TradeBotManager import TradeBotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager


class BotManagerCreationException(Exception): pass


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

