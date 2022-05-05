from collections import defaultdict
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from api.bots.BotManager import BotManager
from gui.default_widgets import ScrollingGridLayout, LabelButton
from typing import Callable, Type


Builder.load_file("./src/gui/bot_menu/base_bot_menu_screen.kv")


AdditionalOptions = defaultdict[Type[BotManager], dict[str, Callable]]
MainOptions = dict[str, Callable]


class BaseBotMenuScreen(Screen):
    """
    Base class for any bot menu.
    Must be implemented 'prepare' method for
    executing 'generate_buttons' method
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bot_actions: ScrollingGridLayout = ScrollingGridLayout()
        self.ids.scroll_view.add_widget(self.bot_actions)

        self.main_options: MainOptions = {}
        self.additional_options: AdditionalOptions = defaultdict(dict)

    def add_main_option(self, title: str, action: Callable) -> None:
        self.main_options[title] = action

    # FIXME: use bot type, not manager
    def add_additional_option(
        self,
        type: Type[BotManager],
        actions: dict[str, Callable]
    ) -> None:
        for title, action in actions.items():
            self.additional_options[type][title] = action

    def generate_buttons(self, bot_manager_type: Type[BotManager]) -> None:
        self._clear_buttons()
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

    def _clear_buttons(self) -> None:
        self.ids.scroll_view.remove_widget(self.bot_actions)
        self.bot_actions = ScrollingGridLayout()
