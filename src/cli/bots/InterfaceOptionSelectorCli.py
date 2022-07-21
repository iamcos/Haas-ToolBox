from api.domain.types import GUID, Interface, InterfaceOption
from InquirerPy import inquirer
from api.exceptions import HaasToolBoxException

from api.providers.bot_api_provider import BotApiProvider
from api.wrappers.interface_wrapper import InterfaceWrapper
from cli.bots.config.ignored_options import ignored_options


class InterfaceOptionSelectorCli:
    def __init__(self, api: BotApiProvider, bot_name: str, bot_guid: GUID) -> None:
        self._api: BotApiProvider = api
        self.bot_name: str = bot_name
        self.bot_guid: GUID = bot_guid

    def select_option(self, interface: Interface) -> InterfaceOption | str:
        interface = self._update_interface(interface)
        wrapped = InterfaceWrapper(interface)
        tofilter = ignored_options[self.bot_name][wrapped.name]
        filtered_options = [i for i in wrapped.options if i.title not in tofilter]
        return self._parameter_selector(filtered_options)


    def _update_interface(self, interface: Interface) -> Interface:
        interface_name: str = InterfaceWrapper(interface).name

        for i in self._api.get_all_bot_interfaces(self.bot_guid):
            if InterfaceWrapper(i).name == interface_name:
                return i

        raise HaasToolBoxException(f"Interface {interface_name} not found") 

    def _parameter_selector(
        self,
        options: list[InterfaceOption]
    ) -> InterfaceOption | str:

        choices: list[dict[str, str | InterfaceOption]] = [
            {
                "name": f"{i.title} : {i.value}",
                "value": i
            }
            for i in options
        ]

        choices.append({"name": "Back", "value": "Back"})

        selected_option: InterfaceOption = inquirer.select(
            message="Select Parameter",
            choices=choices,
        ).execute()

        return selected_option

