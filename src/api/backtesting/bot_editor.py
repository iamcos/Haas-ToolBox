from typing import Protocol, Any

from api.domain.types import GUID, InterfaceOption
from api.providers.bot_api_provider import BotApiProvider
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption


class BotEditor(Protocol):
    def edit_option(
        self,
        interface_name: str,
        option: InterfaceOption
    ) -> None: ...

    def edit_option_by_value(
        self,
        interface_name: str,
        title: str,
        value: Any
    ) -> None: ...


class ApiProviderBotEditor:
    def __init__(self, provider: BotApiProvider, bot_guid: GUID) -> None:
        self._provider: BotApiProvider = provider
        self._bot_guid: GUID = bot_guid

    def edit_option(
        self,
        interface_name: str,
        option: InterfaceOption
    ) -> None:

        self._provider.update_bot_interface_option(
                self._bot_guid, interface_name, option)

    def edit_option_by_value(
        self,
        interface_name: str,
        title: str,
        value: Any
    ) -> None:

        option = IndicatorOption()
        option.title = title
        option.value = value
        self.edit_option(interface_name, option)

