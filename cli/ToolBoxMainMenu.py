"""https://github.com/tmbo/questionary - inquirer analog"""
import functools
from typing import Any
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
from InquirerPy.separator import Separator
from cli.bots.BotCli import BotCli
from cli.bots.tradebot.TradeBotCli import TradeBotCli
from cli.bots.madhatter.MadHatterCli import MadHatterCli


class ToolBoxMainMenu:
    def __init__(self) -> None:
        self._start_message: str = "Choose action: "
        self._bot_chain: dict[str | Separator, type[BotCli | QuitOption] | None] = {
            # Fully configurable
            "Trade Bots": TradeBotCli,
            "Mad-Hatter Bots": MadHatterCli,
            # Custom
            Separator("[Not working] Scalper Bots"): None,
            Separator("[Not working] Flash-Crash Bots"): None,
            Separator("[Not working] AssistedBT"): None,
            Separator("[Not working] TradingView"): None,
            # Special class with keyboard interrupt
            "Quit": QuitOption
        }

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
        return bot_cli().menu()


class QuitOption():
    def menu(self):
        KeyboardInterrupt()

