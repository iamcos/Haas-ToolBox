from api.domain.types import Bot
from api.exceptions import AutobacktesterTypesFactryException
from cli.bots.AutoBacktesterCli import AutoBacktesterCli

from cli.bots.BotConfigBacktestCli import BotConfigBacktestCli
from cli.bots.scalper.ScalperRangeBacktesterCli import ScalperRangeBacktesterCli
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from typing import Type


AutoBacktesresDict = dict[Type[Bot], tuple[Type[AutoBacktesterCli], ...]]


bot_auto_backtesters: AutoBacktesresDict = dict({
    ScalperBot: tuple([ScalperRangeBacktesterCli]),
    MadHatterBot: tuple([BotConfigBacktestCli])
})


def get_autobacktesters_types(
    bot_type: Type[Bot]
) -> tuple[Type[AutoBacktesterCli], ...]:

    if bot_type not in bot_auto_backtesters:
        raise AutobacktesterTypesFactryException(
            f"There are no implemented auto backtesters for {bot_type.__name__}")

    return bot_auto_backtesters[bot_type]

