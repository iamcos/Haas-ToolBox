from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager


Builder.load_file("./src/gui/bot_menu/bot_menu_screen.kv")


class BotMenuScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
    
    def prepare(self, bot_manager: BotManager) -> None:
        self.bot_manager = bot_manager

