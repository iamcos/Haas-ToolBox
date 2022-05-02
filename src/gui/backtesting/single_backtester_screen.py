from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.widget import Widget

from api.bots.BotManager import BotManager


Builder.load_file("./src/gui/backtesting/single_backtester_screen.kv")


class BorderWidget(Widget):
    """Class for drawing borders around window"""
    pass


class BacktestingInfoLayout(BoxLayout, BorderWidget):
    """Class for backtesting info layout"""
    pass


class BacktestingInfoLabel(Label):
    """Class for text in backtesting info"""
    pass


class PlotLayout(BoxLayout, BorderWidget):
    """Class for showing plot of backtesting"""
    pass


class LogsLayout(ScrollView, BorderWidget):
    """Class for showing logs of backtesting"""
    pass


class LogsText(Label):
    """Class for logs text"""
    pass


class HotKeysLayout(GridLayout, BorderWidget):
    """Class for showing buttons and hotkeys"""
    pass


class ActionTextLabel(Label):
    """Class for backtesting button"""
    pass


class ActionHotkeyLabel(Label):
    """Class for backtesting hotkey"""
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




