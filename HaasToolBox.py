"""https://github.com/tmbo/questionary - inquirer analog"""
from typing import Any
from InquirerPy import inquirer
from InquirerPy.prompts.list import ListPrompt
from bots.flash_crash.flash_crash_bot import FlashCrashBot
from bots.interactive.interactive_bot import InteractiveBot as AssistedBT
from bots.mad_hatter.mad_hatter_bot import MadHatterBot
from bots.trade.trade_bot import Trade_Bot
from trading_view import TradingView
from bots.scalper.scalper_bot import ScalperBot


class HaasToolBox:

    def __init__(self) -> None:
        self._start_choices: list[str] = [
            "Mad-Hatter Bots",
            'Trade Bots',
            "Flash-Crash Bots",
            "AssistedBT",
            "Scalper Bots",
            "TradingView",
            "Quit",
        ]
        self._start_message: str = "Choose action: "

    """ToolBox main menu"""

    def start_session(self) -> None:
        menu_promt: ListPrompt = inquirer.select(
            message=self._start_message,
            choices=self._start_choices,
        )
        response: Any = menu_promt.execute()

        self._process_main_menu_repsonse(response)

    def _process_main_menu_repsonse(self, response: Any) -> None:
        if response == "Mad-Hatter Bots":
            MadHatterBot().mh_menu()

        if response == "Trade Bots":
            Trade_Bot().menu()

        if response == "Scalper Bots":
            ScalperBot().scalper_bot_menu()

        if response == "Flash-Crash Bots":
            FlashCrashBot().menu()

        if response == "AssistedBT":
            AssistedBT().menu()

        if response == "TradingView":
            TradingView().main()

        if response == "Quit":
            KeyboardInterrupt()
