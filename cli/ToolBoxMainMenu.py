"""https://github.com/tmbo/questionary - inquirer analog"""
import functools
from typing import Any
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
from cli.bots.BotCli import BotCli
from cli.bots.tradebot.TradeBotCli import TradeBotCli
from cli.bots.madhatter.MadHatterCli import MadHatterCli


class ToolBoxMainMenu:
    """
    ToolBox main menu
    """

    def __init__(self) -> None:
        self._start_message: str = "Choose action: "
        self._bot_chain: dict[str, type[BotCli] | None] = {
            # Fully configurable
            "Trade Bots": TradeBotCli,
            "Mad-Hatter Bots": MadHatterCli,
            # Custom
            "[Not working] Mad-Hatter Bots": None,
            "[Not working] Scalper Bots": None,
            "[Not working] Flash-Crash Bots": None,
            "[Not working] AssistedBT": None,
            "[Not working] TradingView": None,
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
        return self._bot_chain[response]().menu()


class QuitOption(BotCli):
    def menu(self):
        KeyboardInterrupt()
