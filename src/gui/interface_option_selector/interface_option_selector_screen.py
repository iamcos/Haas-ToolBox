from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.models import Interfaces
from api.bots.BotManager import BotManager
from gui.default_widgets import LabelButton, ScrollingGridLayout
from typing import Callable, Any


Builder.load_file(
    "./src/gui/interface_option_selector/interface_option_selector_screen.kv")


class InterfaceOptionSelectorScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
        self.interface: Interfaces
        self.grid: ScrollingGridLayout = ScrollingGridLayout()
        self.ids.scroll_view.add_widget(self.grid)

    def setup(self, bot_manager: BotManager, interface: Interfaces) -> None:
        self.bot_manager = bot_manager
        self.interface = interface
        self.clear_buttons()
        self.generate_buttons(interface)

    def clear_buttons(self) -> None:
        self.ids.scroll_view.remove_widget(self.grid)
        self.grid = ScrollingGridLayout()

    def generate_buttons(self, interface: Interfaces) -> None:
        for option in self.bot_manager.interface_options(interface):
            print(f"{option.title=}, {option.value=}")
            self.grid.add_widget(
                LabelButton(
                    text=f"{option.title}: {option.value}",
                    on_release=self.process_option(option)
                )
            )
        self.ids.scroll_view.add_widget(self.grid)

    def process_option(self, option: IndicatorOption) -> Callable[[Any], None]:
        def inner(_):
            print(f"Choosed {option.title}: {option.value}")
            self.manager.get_screen("single_backtester").setup(
                self.bot_manager,
                self.interface,
                option
            )
            self.manager.current = "single_backtester"
        return inner
