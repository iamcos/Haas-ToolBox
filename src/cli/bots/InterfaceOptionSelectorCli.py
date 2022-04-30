from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.bots.BotManager import BotManager
from api.models import Interfaces
from InquirerPy import inquirer


class InterfaceOptionSelectorCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager
        self.bot_name: str = manager.bot_name()

    def select_option(self, interface: Interfaces) -> IndicatorOption | str:
        return self._parameter_selector(
            self.manager.interface_options(interface)
        )

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

