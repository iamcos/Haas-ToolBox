import functools
from typing import Any
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.separator import Separator
from api.exceptions import HaasToolBoxException
from cli.bots.BotCli import BotCli
from cli.bots.tradebot.TradeBotCli import TradeBotCli
from cli.bots.madhatter.MadHatterCli import MadHatterCli
from cli.bots.scalper.ScalperCli import ScalperCli
from loguru import logger as log


def sigint_catcher(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            log.info("Shutting up...")
            exit()
    return inner


class ToolBoxMainMenu:
    def __init__(self) -> None:
        self._start_message: str = "Choose action: "
        self._bot_chain: dict[str | Separator, type[BotCli | QuitOption] | None] = {
            "Trade Bots": TradeBotCli,
            # Custom
            "Mad-Hatter Bots": MadHatterCli,
            "Scalper Bots": ScalperCli,
            Separator("[Not working] Flash-Crash Bots"): QuitOption,
            Separator("[Not working] AssistedBT"): QuitOption,
            Separator("[Not working] TradingView"): QuitOption,
            # Special class with keyboard interrupt
            "Quit": QuitOption
        }

    @sigint_catcher
    def start_session(self) -> None:
        menu_promt: ListPrompt = inquirer.select(
            message=self._start_message,
            choices=list(self._bot_chain.keys()),
        )
        response: Any = menu_promt.execute()

        self._process_main_menu_response(response)

    @functools.lru_cache
    def _process_main_menu_response(self, response: str) -> None:
        bot_cli = self._bot_chain[response]
        try:
            bot_cli().menu()
        except HaasToolBoxException as e:
            log.warning(e)
        except KeyboardInterrupt:
            pass

        self.start_session()


class QuitOption():
    def menu(self):
        KeyboardInterrupt()

