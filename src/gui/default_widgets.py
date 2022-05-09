import re
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import gui.colors as colors


class Title(Widget):
    pass


class Subtitle(Widget):
    pass


class Text(Widget):
    pass


class BaseLabel(Label):
    pass


class TitleLabel(BaseLabel, Title):
    pass


class SubtitleLabel(BaseLabel, Subtitle):
    pass


class TextLabel(BaseLabel, Text):
    pass


class IntegerInput(TextInput):

    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if self.text.startswith("0"):
            s = re.sub(pat, "", substring[1:])
        else:
            s = re.sub(pat, '', substring)
        return super().insert_text(s, from_undo=from_undo)


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)


class MainWindow(BoxLayout):
    pass


class ScrollingGridLayout(GridLayout):
    pass


class LabelButton(Button):
    pass


class BorderWidget(Widget):
    """Class for drawing borders around window"""
    pass


class LogsText(Label):
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
        self.remove_widget(self.logs_grid)
        self.logs_grid = ScrollingGridLayout()
        self.add_widget(self.logs_grid)
        self.scroll_y = 0


