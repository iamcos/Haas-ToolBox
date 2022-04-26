from gui.settings.settings_screen import SettingsScreen
from gui.menu.menu_screen import MenuScreen
from gui.bot_selector.bot_selector_screen import BotSelectorScreen
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class HaasToolBoxApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(BotSelectorScreen(name='bot_selector'))

        return sm

