from api.bots.bot_multiple_backtester import start_multiple_backtesting
from api.models import Bot
from InquirerPy import inquirer
from typing import Callable, Any
from loguru import logger as log


class MultiBotSelectedCli:

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

        buf: Any = self.bots
        for method in self.menu[action]:
            buf = method(buf)

    def _menu_action(self) -> str:
        return inquirer.select(
            message="Select action:",
            choices=list(self.menu.keys())
        ).execute()

