from abc import abstractmethod
from typing import Type

from api.bots.BotApiProvider import Bot, Interfaces

InterfaceGuid = str


class BotManager():
    @abstractmethod
    def bot_not_selected(self) -> bool: pass

    @abstractmethod
    def set_bot(self, bot: Bot)-> None: pass

    @abstractmethod
    def get_available_bots(self) -> list[Bot]: pass

    @abstractmethod
    def get_interfaces_by_type(
        self,
        t: Type[Interfaces]
    ) -> tuple[Interfaces, ...]: pass

    # TODO: Create basic impl by using get_interfaces_by_type
    @abstractmethod
    def get_all_interfaces(self) -> tuple[Interfaces, ...]: pass

    @abstractmethod
    def refresh_bot(self) -> None: pass

    @abstractmethod
    def bot_name(self) -> str: pass
