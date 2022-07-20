from api.domain.types import Bot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from typing import Type, cast


custom_bot_types: dict[int, Type] = dict({
    3: ScalperBot,
    15: MadHatterBot
})


def get_bot_type(bot: Bot) -> Type:
    bot_type: Type = type(bot)

    if bot.botType in custom_bot_types:
        return custom_bot_types[cast(int, bot.botType)]

    return bot_type

