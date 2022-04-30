from typing import Callable, Type
from collections import defaultdict
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager
from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from gui.default_widgets import LabelButton, ScrollingGridLayout


Builder.load_file("./src/gui/bot_menu/single_bot_menu_screen.kv")


class SingleBotMenuScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bot_manager: BotManager
        self.bot_actions: ScrollingGridLayout = ScrollingGridLayout()
        self.ids.scroll_view.add_widget(self.bot_actions)

        self.main_options: dict[str, Callable] = {
            "Select interface": self.select_interface,
            "Select another bot": self.select_another_bot,
        }

        self.additional_options = defaultdict(dict)
        self.additional_options[MadHatterBotManager] = {
            "Config backtesting": self.config_backtesting
        }
        self.additional_options[ScalperBotManager] = {
            "Range backtesting": self.range_backtesting
        }
    

    def prepare(self, bot_manager: BotManager) -> None:
        print(f"{bot_manager=}")
        self.bot_manager = bot_manager
        self._clear_buttons()
        self._generate_buttons()

    def _clear_buttons(self) -> None:
        self.ids.scroll_view.remove_widget(self.bot_actions)
        self.bot_actions = ScrollingGridLayout()

    def _generate_buttons(self) -> None:
        bot_manager_type: Type = type(self.bot_manager)
        additional_options = self.additional_options[bot_manager_type]

        for label, action in additional_options.items():
            self.bot_actions.add_widget(
                LabelButton(text=label, on_release=action)
            )

        for label, action in self.main_options.items():
            self.bot_actions.add_widget(
                LabelButton(text=label, on_release=action)         
            )

        self.ids.scroll_view.add_widget(self.bot_actions)


    def select_interface(self, _: LabelButton) -> None:
        self.manager.get_screen("interface_selector").setup(self.bot_manager)
        self.manager.current = "interface_selector"

    def select_another_bot(self, _: LabelButton) -> None:
        self.manager.current = "bot_selector"

    def config_backtesting(self, _: LabelButton) -> None:
        print(f"Confgi backtesting")

    def range_backtesting(self, _: LabelButton) -> None:
        print(f"Range backtesting")

