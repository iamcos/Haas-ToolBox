from typing import Type, Optional, cast

from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.bots.BotManager import BotManager
from cli.bots.BotSelectorCli import BotSelectorCli
from cli.bots.InterfaceSelectorCli import InterfaceSelectorCli
from cli.bots.InterfaceOptionSelectorCli import InterfaceOptionSelectorCli
from api.bots.BotApiProvider import Bot
from api.bots.bot_managers_factory import get_bot_manager
from api.bots.trade.TradeBotManager import Interfaces
from loguru import logger as log
from typing import Callable
from InquirerPy import inquirer

from cli.bots.BotBacktestCli import BotBacktestCli


MainMenuAction = Optional[Bot | Interfaces | KeyboardInterrupt]


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
        self.backtester = BotBacktestCli(self.manager)

        self.main_menu = list([
            {
                "name": "Select interface",
                "value": self.interface_selector.select_interface
            },
            {
                "name": f"Select another {self.manager.bot_name()}",
                "value": self.bot_selector.select_bot
            },
            {
                "name": "Quit",
                "value": KeyboardInterrupt
            }
        ])

    def menu(self) -> None:
        log.info(f"Starting {self.manager.bot_name()} CLI menu..")
        self.bot_selector.choose_bot()
        self._process_user_choice(self._menu_action())

    def _menu_action(self) -> MainMenuAction:
        log.info("Starting base bot setting..")
        choosed_action: Callable = inquirer.select(
            message="Select action:",
            choices=self.main_menu
        ).execute()

        return choosed_action()

    def _process_user_choice(self, choice: MainMenuAction) -> None:
        if type(choice) is Bot:
            self._process_bot(cast(Bot, choice))
        elif type(choice) in (Insurance, Indicator, Safety):
            self._process_interface(cast(Interfaces, choice))
        elif type(choice) is KeyboardInterrupt:
            self._process_keyboard_interrupt()
            exit("666")

        self.menu()

    def _process_bot(self, bot: Bot) -> None:
        self.manager.set_bot(bot)

    def _process_interface(self, choice: Interfaces) -> None:
        option = self.indictator_option_selector.select_option(choice)
        self.backtester.process_backtest(choice, option)

    def _process_keyboard_interrupt(self) -> None:
        log.info("Bye :)")

