from abc import abstractmethod
from typing import Any, Callable, Optional, Type
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from api.models import Bot, Interfaces


class BotException(Exception): pass


class BotApiProvider():
    def get_as_dict(self, bot: Bot, indicator_name: str) -> dict:
        interface = getattr(bot, indicator_name)
        if type(interface) is not dict:
            interface = vars(interface)
        return interface

    @abstractmethod
    def get_all_bots(self) -> tuple[Bot]: pass

    @abstractmethod
    def get_all_interfaces(self, guid: str) -> tuple[Interfaces]: pass

    @abstractmethod
    def get_interfaces_by_type(
        self,
        guid: str,
        t: Type[Interfaces]
    ) -> tuple[Interfaces]: pass

    @abstractmethod
    def get_refreshed_bot(self, guid: str) -> Bot: pass

    @abstractmethod
    def edit_interface(
        self,
        t: Interfaces,
        param_num: int,
        value: Any,
        bot_guid: str
    ) -> None: pass

    @abstractmethod
    def get_backtest_method(self) -> Callable: pass

    @abstractmethod
    def process_error(
        self,
        response: Optional[HaasomeClientResponse] = None,
        message: str = ""
    ) -> Any: pass

    @abstractmethod
    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        pass

    @abstractmethod
    def clone_bot_and_save(self, bot: Bot) -> Bot: pass

    @abstractmethod
    def delete_bot(self, bot_guid: str) -> None: pass

