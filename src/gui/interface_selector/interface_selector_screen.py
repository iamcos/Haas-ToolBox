from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager
from api.wrappers.InterfaceWrapper import InterfaceWrapper
from gui.default_widgets import LabelButton, ScrollingGridLayout, SubtitleLabel


Builder.load_file("./src/gui/interface_selector/interface_selector_screen.kv")



class InterfaceSelectorScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
        self.interface_list = self.create_buttons_grid()
        self.ids.scroll_view.add_widget(self.interface_list)

    def setup(self, bot_manager: BotManager) -> None:
        self.bot_manager = bot_manager
        self.update_buttons()

    def update_buttons(self) -> None:
        print(f"Updating buttons")
        self.clear_buttons()
        self.generate_buttons()
        self.ids.scroll_view.add_widget(self.interface_list)


    def clear_buttons(self) -> None:
        self.ids.scroll_view.remove_widget(self.interface_list)
        self.interface_list = self.create_buttons_grid()
        print(f"Buttons cleared")

    def generate_buttons(self) -> None:
        types = self.bot_manager.get_available_interface_types()

        for type in types:
            label = SubtitleLabel(text=type.__name__)
            block = ScrollingGridLayout()
            self.interface_list.add_widget(label)

            for interface in self.bot_manager.get_interfaces_by_type(type):
                block.add_widget(
                        LabelButton(
                            text=InterfaceWrapper(interface).name,
                            on_release=self.process_interface(interface)))

            self.interface_list.add_widget(block)

    def create_buttons_grid(self) -> ScrollingGridLayout:
        return ScrollingGridLayout()

    def process_interface(self, interface):
        def inner(_):
            print(f"Choosed {interface}")
            print(f"Hello from innter")
        return inner

