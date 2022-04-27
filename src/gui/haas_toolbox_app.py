from gui.bot_menu.single_bot_menu_screen import SingleBotMenuScreen
from gui.bot_selector.bot_selector_screen import BotSelectorScreen
from gui.bot_type_selector.bot_type_selector_screen import BotTypeSelectorScreen
from gui.interface_selector.interface_selector_screen import InterfaceSelectorScreen
from gui.settings.settings_screen import SettingsScreen
from gui.menu.menu_screen import MenuScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class HaasToolBoxApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(BotTypeSelectorScreen(name="bot_type_selector"))
        sm.add_widget(BotSelectorScreen(name="bot_selector"))
        sm.add_widget(InterfaceSelectorScreen(name="interface_selector"))
        sm.add_widget(SingleBotMenuScreen(name="single_bot_menu"))

        return sm

