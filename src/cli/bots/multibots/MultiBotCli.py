from api.models import Bot
from InquirerPy import inquirer
from typing import Callable, Any
from loguru import logger as log
from cli.bots.multibots.multi_backtester_cli import start_multiple_backtesting



class MultiBotCli:
    def __init__(self, bots: list[Bot]) -> None:
        self.bots = bots
        self.menu: dict[str, tuple[Callable[..., Any], ...]] = dict({
            "Multiple backtesting": (
                start_multiple_backtesting,
            )
        })

    def start(self) -> None:
        log.info("Starting processing multiple bots")
        action: str = self._menu_action()

        buf = self.bots
        for method in self.menu[action]:
            buf = method(buf)

    def _menu_action(self) -> str:
        return inquirer.select(
            message="Select action:",
            choices=list(self.menu.keys())
        ).execute()

