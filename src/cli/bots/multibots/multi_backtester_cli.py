from InquirerPy import inquirer
from api.type_specifiers import get_bot_type
from cli.factories.autobacktester_types_factory import get_autobacktesters_types
from api.models import Bot
from api.bots.BotManager import BotManager
from api.factories.bot_managers_factory import get_bot_manager
from typing import Type
from loguru import logger as log

from cli.bots.AutoBacktesterCli import AutoBacktesterCli


def start_multiple_backtesting(bots: list[Bot]) -> None:
    bot_type: Type = get_bot_type(bots[0])
    AutoBacktester: Type = _get_auto_backtester(bot_type)
    manager: BotManager = get_bot_manager(bot_type)

    log.info(f"Starting multiple backtesting for {len(bots)} bots")
    log.debug(f"Choosed bot type {bot_type}")

    for i, bot in enumerate(bots):
        log.info(
            "Starting backtesting for "
            f"{manager.bot_name()} №{i+1}"
        )
        manager.set_bot(bot)
        AutoBacktester.with_manager(manager).start()

    log.info("Multiple backtesting finished")


def _get_auto_backtester(bot_type: Type) -> Type[AutoBacktesterCli]:
    autobacktesters: tuple[Type, ...] = get_autobacktesters_types(bot_type)

    if len(autobacktesters) > 1:
        AutoBacktester = _choose_backtesting_method(autobacktesters)
    else:
        AutoBacktester = autobacktesters[0]

    return AutoBacktester


def _choose_backtesting_method(
    autobacktesters: tuple[Type, ...]
) -> Type[AutoBacktesterCli]:

    return inquirer.select(
        message="Choose auto backtesting method",
        choices=[
            {"name": i.get_name(), "value": i}
            for i in autobacktesters
        ]
    ).execute()
