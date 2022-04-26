from api.models import Config
from typing import Type
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("./src/gui/settings/settings_screen.kv")
my_config = Config()


class SettingsSection(GridLayout):
    pass


class SettingsScreen(Screen):
    config = ObjectProperty(my_config)
    
    __events__ = ("on_save", )
    
    def on_save(self) -> None:
        print("Saving config...")
        print(my_config)

    def set_property(self, value: str, name: str, type: Type) -> None:
        try:
            setattr(self.config, name, type(value))
            print(f"Attr saved {getattr(self.config, name)}")
            self.ids[name].background_color = (1, 1, 1)
            self.ids[name].text = str(getattr(self.config, name))
        except ValueError:
            print(f"Wrong format: {value=}, {name=}, {type=}")
            self.ids[name].background_color = (1, 0, 0)

