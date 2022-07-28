from api.domain.types import GUID, Bot, Interface, InterfaceOption
from typing import Protocol, Type


class BotApiProvider(Protocol):
    def get_all_bots(self) -> tuple[Bot]: ...

    def get_all_bot_interfaces(self, bot_guid: GUID) -> tuple[Interface]: ...

    def get_refreshed_bot(self, bot_guid: GUID) -> Bot: ...

    def get_available_interface_types(self) -> tuple[Type[Interface], ...]: ...

    def clone_and_save_bot(self, bot_or_guid: Bot | GUID) -> Bot: ...

    def delete_bot(self, bot_guid: GUID) -> None: ...

    def backtest_bot(self, bot_guid: GUID, ticks: int) -> None: ...

    def get_bot_interfaces_by_type(
        self,
        guid_or_bot: GUID | Bot,
        interface_type: Type[Interface]
    ) -> tuple[Interface]: ...

    def update_bot_interface_option(
        self,
        bot_guid: GUID,
        interface_name: str,
        option: InterfaceOption
    ) -> None: ...

