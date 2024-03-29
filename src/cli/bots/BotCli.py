from api.backtesting.BotFineTuneBacktester import BotFineTuneBacktester
from api.backtesting.interface_fine_tune_backtester import InterfaceFineTuneBacktester
from api.domain.dtos import BotFineTuneSetup, InterfaceFineTuneSetup
import api.factories as factories
from api.loader import log, main_context
from api.domain.types import GUID, Interface, Bot, InterfaceOption
from api.providers.bot_api_provider import BotApiProvider
from api.wrappers.interface_wrapper import InterfaceWrapper
from cli.bots.BotSelectorCli import BotSelectorCli
from cli.bots.InterfaceSelectorCli import InterfaceSelectorCli
from cli.bots.InterfaceOptionSelectorCli import InterfaceOptionSelectorCli
from cli.bots.BotBacktestCli import BotBacktestCli
from cli.bots.config.ignored_options import ignored_options
from cli.bots.multibots.MultiBotCli import MultiBotCli
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from typing import Optional, Type, Any, cast, Callable
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
            "Bot Fine Tune": (
                self.bot_fine_tune,
            ),
            "Quit": (
                self._process_keyboard_interrupt,
            )
        })

    def menu(self) -> None:
        log.info(f"Starting {self.bot_name} CLI menu..")
        bots: list[Bot] = self.select_bots()
        self._process_bots(bots)

    def _process_bots(self, bots: list[Bot]) -> None:
        if len(bots) > 1:
            MultiBotCli(bots).start()
        else:
            self.bot_guid: GUID = bots.pop().guid
            self._do_action()

    def _do_action(self) -> None:
        choosed_action: str = self._menu_action()
        self._process_user_choice(choosed_action)

    def _menu_action(self) -> str:
        choosed_action: str = inquirer.select(
            message="Select action:",
            choices=list(self.main_menu.keys())
        ).execute()

        return choosed_action

    def _process_user_choice(self, choice: str) -> None:
        method_result: Any = None
        for method in self.main_menu[choice]:
            if method_result is None:
                method_result = method()
            else:
                method_result = method(method_result)

    def select_interface(self) -> Optional[Interface]:
        interface_or_back = InterfaceSelectorCli(
                self.provider, self.bot_guid).select_interface()

        if interface_or_back == "Back":
            return self._do_action()

        return cast(Interface, interface_or_back)


    def select_bots(self) -> list[Bot]:
        return BotSelectorCli(self.provider, self.bot_name).select_bots()

    def _process_interface(self, choice: Interface) -> None:
        action: str = inquirer.select(
                message="Select action",
                choices=[
                    {"name": "Select interface option", "value": 1},
                    {"name": "Start interface fine tune", "value": 2}
                ]).execute()

        if action == 1:
            self._process_interface_option(choice)
        elif action == 2:
            self._process_interface_fine_tune(choice)
        else:
            log.error("Unknow option selected")


    def _process_interface_option(self, choice: Interface) -> None:
        option: InterfaceOption | str = InterfaceOptionSelectorCli(
                self.provider, self.bot_name, self.bot_guid).select_option(choice)

        if option == "Back":
            return self._process_user_choice("Select interface")
        else:
            BotBacktestCli(self.provider).process_backtest(
                    self.bot_guid,
                    choice,
                    cast(IndicatorOption, option)
            )
            return self._process_interface(choice)

    def _process_interface_fine_tune(self, choice: Interface) -> None:
        backtester: InterfaceFineTuneBacktester = \
                factories.get_interface_fine_tune_backtester(self.provider)

        setup = InterfaceFineTuneSetup(
                bot_guid=self.bot_guid,
                interface=choice,
                ticks=main_context.config_manager.read_ticks())

        backtester.execute(setup)


    def _process_keyboard_interrupt(self) -> None:
        log.info("Bye :)")
        exit("666")

    def bot_fine_tune(self) -> None:
        backtester = factories.get_bot_fine_tune_backtester(self.provider)
        interfaces = self.provider.get_all_bot_interfaces(self.bot_guid, filtered=True)

        setup = BotFineTuneSetup(
            bot_guid=self.bot_guid,
            ticks=main_context.config_manager.read_ticks(),
            interfaces=interfaces)

        backtester.execute(setup)

    def add_menu_action(
            self,
            title: str,
            methods_chain: tuple[Callable[..., Any], ...]
        ) -> None:

        quit: tuple[Callable[..., Any], ...] = self.main_menu["Quit"]
        del self.main_menu["Quit"]

        self.main_menu[title] = methods_chain

        self.main_menu["Quit"] = quit

