from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager


Builder.load_file("./src/gui/backtesting/single_backtester_screen.kv")


class ActionTextLabel(Label):
    pass


class ActionHotkeyLabel(Label):
    pass


class SingleBacktesterScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
        self.interface_option: IndicatorOption

    def setup(
        self,
        bot_manager: BotManager,
        interface_option: IndicatorOption
    ) -> None:
        self.bot_manager = bot_manager
        self.interface_option = interface_option

