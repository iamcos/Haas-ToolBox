from typing import Type, Any, cast

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from cli.bots.BotSelectorCli import BotSelectorCli
from cli.bots.InterfaceSelectorCli import InterfaceSelectorCli
from cli.bots.InterfaceOptionSelectorCli import InterfaceOptionSelectorCli
from api.bots.BotManager import BotManager
from api.bots.BotApiProvider import Bot
from api.bots.bot_managers_factory import get_bot_manager
from api.models import Interfaces
from loguru import logger as log
from typing import Callable
from InquirerPy import inquirer

from cli.bots.BotBacktestCli import BotBacktestCli


class BotCli:
    """
    Base class for bot setting CLI
    """

    def __init__(self, t: Type) -> None:
        self.manager: BotManager = get_bot_manager(t)

        self.bot_selector = BotSelectorCli(self.manager)
        self.interface_selector = InterfaceSelectorCli(self.manager)
        self.indictator_option_selector = InterfaceOptionSelectorCli(
            self.manager)

        self.main_menu: dict[str, tuple[Callable[..., Any], ...]] = dict({
            "Select interface": (
                self.interface_selector.select_interface,
                self._process_interface
            ),
            f"Select another {self.manager.bot_name()}": (
                self.bot_selector.select_bot,
                self._process_bot
            ),
            "Quit": (
                self._process_keyboard_interrupt,
            )
        })

    def add_menu_action(
            self,
            title: str,
            methods_chain: tuple[Callable[..., Any], ...]
        ) -> None:

        quit: tuple[Callable[..., Any], ...] = self.main_menu["Quit"]
        del self.main_menu["Quit"]

        self.main_menu[title] = methods_chain

        self.main_menu["Quit"] = quit

    def menu(self) -> None:
        log.info(f"Starting {self.manager.bot_name()} CLI menu..")
        self.bot_selector.choose_bot()
        self._process_user_choice(self._menu_action())

    def _menu_action(self) -> str:
        log.info("Starting base bot setting..")
        choosed_action: str = inquirer.select(
            message="Select action:",
            choices=list(self.main_menu.keys())
        ).execute()

        return choosed_action

    def _process_user_choice(self, choice: str) -> None:
        method_result: Any = None

        log.info(f"Starting processing {choice=}")
        for method in self.main_menu[choice]:
            log.info(f"{method=}, {method_result=}")
            if method_result is None:
                method_result = method()
            else:
                method_result = method(method_result)

        log.info(f"{method_result=}")

        self.menu()

    def _process_bot(self, bot: Bot) -> None:
        self.manager.set_bot(bot)

    def _process_interface(self, choice: Interfaces) -> None:
        if choice == "Back":
            return self._process_user_choice(self._menu_action())

        option = self.indictator_option_selector.select_option(choice)
        log.info("Waiting")

        if option == "Back":
            return self._process_user_choice("Select interface")
        else:
            BotBacktestCli(self.manager).process_backtest(
                    choice,
                    cast(IndicatorOption, option)
            )
            return self._process_interface(choice)

    def _process_keyboard_interrupt(self) -> None:
        log.info("Bye :)")
        exit("666")

