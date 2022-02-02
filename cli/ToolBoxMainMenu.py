"""https://github.com/tmbo/questionary - inquirer analog"""
from typing import Any
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
# from api.bots.flash_crash import FlashCrashBotManager
# from api.bots.interactive.InteractiveBotManager import InteractiveBotManager
# from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
# from api.TradingViewManager import TradingViewManager
# from api.bots.scalper.ScalperBotManager import ScalperBotManager
from cli.bots.TradeBotCli import TradeBotCli


class ToolBoxMainMenu:
    """
    ToolBox main menu
    """

    def __init__(self) -> None:
        # TODO: Use CLI classes here, not managers !
        self._start_message: str = "Choose action: "
        # FIXME: Delete Nones!
        self._bot_chain: dict[str, type] = {
            # Fully configurable
            "Trade Bots": TradeBotCli,
            # Custom
            # "[Not working] Mad-Hatter Bots": None,
            # "[Not working] Scalper Bots": None,
            # "[Not working] Flash-Crash Bots": None,
            # "[Not working] AssistedBT": None,
            # "[Not working] TradingView": None,
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

    def _process_main_menu_response(self, response: str) -> None:
        self._bot_chain[response]().menu()


class QuitOption:
    def menu(self):
        KeyboardInterrupt()
