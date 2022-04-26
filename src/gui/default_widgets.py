import re
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


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

