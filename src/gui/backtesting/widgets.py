from api.models import ROI
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from typing import Callable, Optional
from gui.default_widgets import BorderWidget


Builder.load_file("./src/gui/backtesting/widgets.kv")


class BacktestingInfoLayout(BoxLayout, BorderWidget):
    """Class for backtesting info layout"""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.option_value = BacktestingInfoLabel()
        self.bot_roi = BacktestingInfoLabel()
        self.interface_name = BacktestingInfoLabel()

        self.add_widget(self.interface_name)
        self.add_widget(self.option_value)
        self.add_widget(self.bot_roi)

    def update(
        self,
        option_value: str,
        bot_roi: ROI,
        interface_name: Optional[str] = None
    ) -> None:
        self.option_value.text = f"Value: {option_value}"
        self.bot_roi.text = f"ROI: {bot_roi}%"
        if interface_name is not None:
            self.interface_name.text = interface_name



class BacktestingInfoLabel(Label):
    """Class for text in backtesting info"""
    pass


class PlotLayout(BoxLayout, BorderWidget):
    """Class for showing plot of backtesting"""
    pass


class HotKeysLayout(GridLayout, BorderWidget):
    """Class for showing buttons and hotkeys"""
    def add_actions(self, actions: dict[tuple[str, str], Callable]) -> None:
        for (text, hotkey), action in actions.items():
            self.add_widget(ActionButtonLabel(
                text=text, on_release=action))
            self.add_widget(ActionHotkeyLabel(
                text=f"[ {hotkey} ]"))


class ActionButtonLabel(Button):
    """Class for backtesting button"""
    pass


class ActionHotkeyLabel(Label):
    """Class for backtesting hotkey"""
    pass

