import api.factories as factories

from api.loader import log
from api.domain.types import GUID, Interface, Bot
from api.providers.bot_api_provider import BotApiProvider
from cli.bots.BotSelectorCli import BotSelectorCli
from cli.bots.InterfaceSelectorCli import InterfaceSelectorCli
from cli.bots.InterfaceOptionSelectorCli import InterfaceOptionSelectorCli
from cli.bots.BotBacktestCli import BotBacktestCli
from cli.bots.multibots.MultiBotCli import MultiBotCli
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from typing import Type, Any, cast, Callable
from InquirerPy import inquirer


class BotCli:
    """
    Base class for bot setting CLI
    """

    def __init__(self, t: Type) -> None:
        self.bot: Bot
        self.provider: BotApiProvider = factories.get_provider(t)
        self.bot_name: str = t.__name__

        self.main_menu: dict[str, tuple[Callable[..., Any], ...]] = dict({
            "Select interface": (
                self.select_interface,
                self._process_interface
            ),
            f"Select another {self.bot_name}": (
                self.select_bots,
                self._process_bots
            ),
            "Quit": (
                self._process_keyboard_interrupt,
            )
        })

    def select_interface(self, bot_guid: GUID) -> Interface:
        return InterfaceSelectorCli(self.provider, bot_guid).select_interface()

    def select_bots(self) -> list[Bot]:
        return BotSelectorCli(self.provider, self.bot_name).select_bots()

    def menu(self) -> None:
        log.info(f"Starting {self.bot_name} CLI menu..")
        bots: list[Bot] = self.select_bots()
        self._process_bots(bots)

    def _process_bots(self, bots: list[Bot]) -> None:
        if len(bots) > 1:
            MultiBotCli(bots).start()
        else:
            self.guid: GUID = bots.pop().guid
            interface = self.select_interface(self.guid)
            self._process_interface(interface)

    # def _menu_action(self) -> str:
    #     choosed_action: str = inquirer.select(
    #         message="Select action:",
    #         choices=list(self.main_menu.keys())
    #     ).execute()
    #
    #     return choosed_action

    def _process_user_choice(self, choice: str, *args) -> None:
        method_result: Any = args

        for method in self.main_menu[choice]:
            if hasattr(method_result, "__iter__"):
                method_result = method(*method_result)
            else:
                method_result = method(method_result)

    def _process_interface(self, choice: Interface) -> None:
        if choice == "Back":
            return self.menu()

        option = InterfaceOptionSelectorCli(
                self.provider, self.bot_name, self.guid).select_option(choice)

        log.info("Waiting")

        if option == "Back":
            return self.select_interface(self.guid)
        else:
            BotBacktestCli(self.provider).process_backtest(
                    self.guid,
                    choice,
                    cast(IndicatorOption, option)
            )
            return self._process_interface(choice)

    def _process_keyboard_interrupt(self) -> None:
        log.info("Bye :)")
        exit("666")

    def add_menu_action(
            self,
            title: str,
            methods_chain: tuple[Callable[..., Any], ...]
        ) -> None:

        quit: tuple[Callable[..., Any], ...] = self.main_menu["Quit"]
        del self.main_menu["Quit"]

        self.main_menu[title] = methods_chain

        self.main_menu["Quit"] = quit


