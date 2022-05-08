from api.models import ROI
import gui.colors as colors
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.lang import Builder
from gui.default_widgets import ScrollingGridLayout, TextLabel
from typing import Callable, Optional


Builder.load_file("./src/gui/backtesting/widgets.kv")


class BorderWidget(Widget):
    """Class for drawing borders around window"""
    pass


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


class LogsLayout(ScrollView, BorderWidget):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.scroll_y = 0
        self.logs_grid = ScrollingGridLayout()
        self.add_widget(self.logs_grid)

    def info(self, text: str, *args) -> TextLabel:
        if len(args) == 1:
            return self.update_old_log(text, *args)
        else:
            label: TextLabel = TextLabel(text=text)
            self.logs_grid.add_widget(label)

            if self.scroll_y != 0:
                self.scroll_y = 0
                self.scroll_to(label)

            return label

    def update_old_log(self, text: str, log_row: TextLabel) -> TextLabel:
        log_row.text += f" | {text}"
        log_row.color = colors.green
        return log_row
        

    def clear(self) -> None:
        for c in self.logs_grid.children:
            self.logs_grid.remove_widget(c)


class LogsText(Label):
    """Class for logs text"""
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

