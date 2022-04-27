from typing import Type
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file("./src/gui/interface_selector/interface_selector_screen.kv")


class InterfaceSelectorScreen(Screen):

    def update_bot_type(self, bot_type: Type) -> None:
        print(f"Bot type is {bot_type}")

