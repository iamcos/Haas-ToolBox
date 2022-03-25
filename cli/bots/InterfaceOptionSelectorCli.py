from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.bots.InterfaceWrapper import InterfaceWrapper
from api.bots.BotManager import BotManager
from api.models import Interfaces
from InquirerPy import inquirer
from cli.bots.config.ignored_options import ignored_options


class InterfaceOptionSelectorCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager
        self.bot_name: str = manager.bot_name()

    def select_option(self, interface: Interfaces) -> IndicatorOption | str:
        return self._parameter_selector(
            self._indicator_options(interface)
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

    def _indicator_options(
            self,
            source: Interfaces
    ) -> tuple[IndicatorOption]:
        boosted: InterfaceWrapper = InterfaceWrapper(source)

        filtered_options: tuple[IndicatorOption] = tuple([
            self.manager.update_option(i) for i in boosted.options
            if i.title not in ignored_options[self.bot_name][boosted.name]
        ])

        return filtered_options

