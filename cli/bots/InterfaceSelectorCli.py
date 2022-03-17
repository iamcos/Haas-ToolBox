from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.bots.BotManager import BotManager
from api.bots.BotApiProvider import Interfaces
from loguru import logger as log
from typing import Any, Type
from InquirerPy.separator import Separator
from InquirerPy import inquirer

from cli.bots.custom_dtos import InterfacesForCli


class InterfaceSelectorCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager

    def select_interface(self) -> Interfaces:
        choices: list[InterfacesForCli] = self._interfaces_menu_options()
        action = inquirer.select(
            message="Select Interface:",
            choices=choices,
        ).execute()

        if action == "Refresh":
            self.manager.refresh_bot()
            return self.select_interface()

        return action

    def _interfaces_menu_options(self) -> list[InterfacesForCli]:
        choices: list[InterfacesForCli] = []

        # TODO: Add manager method to get available interfaces
        for interface_name in (Indicator, Safety, Insurance):
            log.info(f"Interface name: {interface_name}")

            interfaces: tuple[Interfaces] = self.manager.get_interfaces_by_type(
                interface_name
            )

            iterface_selector = self._display_interface_selector(
                interface_name, interfaces
            )

            choices.extend(iterface_selector)

        log.info(f"{choices=}")
        choices.extend([Separator(""), "Refresh", Separator(""), "Back"])

        return choices

    def _display_interface_selector(
            self,
            interface_name: Type[Interfaces],
            interfaces: tuple[Interfaces, ...]
    ) -> list[InterfacesForCli]:

        if interfaces:
            log.info("Interfaces size more than 0")
            return self._menu_for_choosing_indicator(interfaces)
        else:
            log.info("Interfaces size less than 0")
            msg: str = f"No {interface_name.__name__} to select"
            return self._get_separated_msg(msg)

    def _menu_for_choosing_indicator(
            self,
            interfaces: tuple[Interfaces, ...]
    ) -> list[InterfacesForCli]:
        type_as_name: str = type(interfaces[0]).__name__.lower()
        log.info(f"{type_as_name=}")

        indicators_menu: list[Any] = list([
            Separator(""),
            Separator(type_as_name.capitalize() + " interfaces:")
        ])

        for i in interfaces:
            if i.enabled:
                indicators_menu.append({
                    "name": " " * 4 + getattr(i, type_as_name + "Name"),
                    "value": i
                })
            else:
                indicators_menu.append(Separator(str(i) + " DISABLED"))

        log.info(f"")
        return indicators_menu

    def _get_separated_msg(self, msg: str) -> list[InterfacesForCli]:
        return list([
            Separator(""),
            Separator(msg),
        ])

