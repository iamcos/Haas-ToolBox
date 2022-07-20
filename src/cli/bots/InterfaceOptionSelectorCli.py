from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.domain.types import GUID, Interface, InterfaceOption
from InquirerPy import inquirer
from api.exceptions import HaasToolBoxException

from api.providers.bot_api_provider import BotApiProvider
from api.wrappers.interface_wrapper import InterfaceWrapper
from cli.bots.config.ignored_options import ignored_options


class InterfaceOptionSelectorCli:
    def __init__(self, api: BotApiProvider, bot_name: str) -> None:
        self._api: BotApiProvider = api
        self.bot_name: str = bot_name
        self.bot_guid: GUID

    def set_bot_guid(self, bot_guid: GUID) -> None:
        self.bot_guid = bot_guid

    def select_option(self, interface: Interface) -> IndicatorOption | str:
        interface = self._update_interface(interface)
        return self._parameter_selector(InterfaceWrapper(interface).options)


    def _update_interface(self, interface: Interface) -> Interface:
        interface_name: str = InterfaceWrapper(interface).name

        for i in self._api.get_all_bot_interfaces(self.bot_guid):
            if InterfaceWrapper(i).name == interface_name:
                return i

        raise HaasToolBoxException(f"Interface {interface_name} not found") 

    def _parameter_selector(
            self,
            indicator_options: tuple[IndicatorOption]
    ) -> IndicatorOption | str:

        choices: list[dict[str, str | IndicatorOption]] = [
            {
                "name": f"{i.title} : {i.value}",
                "value": i
            }
            for i in indicator_options
        ]

        choices.append({"name": "Back", "value": "Back"})

        selected_option: IndicatorOption = inquirer.select(
            message="Select Parameter",
            choices=choices,
        ).execute()

        return selected_option

