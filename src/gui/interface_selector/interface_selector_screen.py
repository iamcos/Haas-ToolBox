from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager


Builder.load_file("./src/gui/interface_selector/interface_selector_screen.kv")


class InterfaceSelectorScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager

    def setup(self, bot_manager: BotManager) -> None:
        self.bot_manager = bot_manager
        self.update_buttons()

    def update_buttons(self) -> None:
        pass

