from typing import Type, cast
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from api.models import Bot
from api.config import custom_bot_types
from api.exceptions import AutobacktesterTypesFactryException

from cli.bots.AutoBacktesterCli import AutoBacktesterCli
from cli.bots.BotConfigBacktestCli import BotConfigBacktestCli
from cli.bots.scalper.ScalperRangeBacktesterCli import ScalperRangeBacktesterCli


AutoBacktesresDict = dict[Type[Bot], tuple[Type[AutoBacktesterCli], ...]]


bot_auto_backtesters: AutoBacktesresDict = dict({
    ScalperBot: tuple([ScalperRangeBacktesterCli, BotConfigBacktestCli]),
    MadHatterBot: tuple([BotConfigBacktestCli])
})


def get_bot_type(bot: Bot) -> Type:
    bot_type: Type = type(bot)

    if bot.botType in custom_bot_types:
        return custom_bot_types[cast(int, bot.botType)]

    return bot_type


def get_autobacktesters_types(
    bot_type: Type[Bot]
) -> tuple[Type[AutoBacktesterCli], ...]:

    if bot_type not in bot_auto_backtesters:
        raise AutobacktesterTypesFactryException(
            f"There are no implemented auto backtesters for {bot_type.__name__}")

    return bot_auto_backtesters[bot_type]

