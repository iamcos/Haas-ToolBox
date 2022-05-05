from typing import Type
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot

from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from api.bots.BotManager import BotManager

from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.trade.TradeBotManager import TradeBotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.exceptions import BotManagerCreationException
from api.models import Bot
from api.type_specifiers import get_bot_type


def get_bot_manager_by_type(t: Type) -> BotManager:
    # TODO: Go to dict, delete if else
    if t is TradeBot:
        return TradeBotManager(t)
    elif t is MadHatterBot:
        return MadHatterBotManager(t)
    elif t is ScalperBot:
        return ScalperBotManager(t)
    else:
        raise BotManagerCreationException(
            f"Passed type {t} is wrong or not implemented"
        )



def get_bot_manager_by_bot(bot: Bot) -> BotManager:
    bot_type: Type = type(bot)
    if bot_type is BaseCustomBot:
        bot_type = get_bot_type(bot)
        return get_bot_manager_by_type(bot_type)
    else:
        return get_bot_manager_by_type(bot_type)
