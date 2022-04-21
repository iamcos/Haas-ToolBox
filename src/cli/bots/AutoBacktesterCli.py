from __future__ import annotations
from abc import ABC, abstractmethod
from api.bots.BotManager import BotManager


class AutoBacktesterCli(ABC):
    @classmethod
    @abstractmethod
    def with_manager(cls, manager: BotManager) -> AutoBacktesterCli:
        pass

    @abstractmethod
    def start(self) -> None:
        pass

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        pass

