from typing import Type
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot
from api.bots.bot_managers_factory import get_bot_manager
from api.bots.BotManager import BotManager
from api.models import Bot
from api.MainContext import main_context
from api.config import custom_bot_types
from loguru import logger as log


def start_multiple_backtesting(bots: list[Bot]) -> None:
    if not bots:
        log.error("Must select at least 1 bot")
        return

    log.info(f"Starting multiple backtesting for {len(bots)} bots")
    ticks: int = main_context.config_manager.read_ticks()
    bot_type: Type = type(bots[0])

    if bot_type is BaseCustomBot:
        bot_type = _get_custom_bot_type(bots[0])

    manager: BotManager = get_bot_manager(bot_type)

    for bot in bots:
        manager.set_bot(bot)
        manager.backtest_bot(ticks)

    log.info("Multiple backtesting finished")


def _get_custom_bot_type(bot: Bot) -> Type:
    if bot.botType in custom_bot_types:
        return custom_bot_types[bot.botType.value]

