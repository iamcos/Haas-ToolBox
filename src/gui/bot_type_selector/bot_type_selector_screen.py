from gui.default_widgets import LabelButton
from typing import Type
from haasomeapi.dataobjects.custombots.FlashCrashBot import FlashCrashBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file("./src/gui/bot_type_selector/bot_type_selector_screen.kv")

bot_types_map: dict[str, Type] = {
    "Trade": TradeBot,
    "Mad-Hatter": MadHatterBot,
    "Scalper": ScalperBot,
    "Flash-Crash": FlashCrashBot,
}


class BotTypeSelectorScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._generate_bot_type_buttons()

    def _generate_bot_type_buttons(self) -> None:
        for bot_type in list(bot_types_map.keys()):
            self.ids.bot_types_grid.add_widget(
                LabelButton(text=bot_type, on_release=self.choose_bot_type)
            )

    def choose_bot_type(self, instance: LabelButton) -> None:
        text: str = instance.text
        bot_type: Type = bot_types_map[text]
        print(f"{bot_type=}, {text=}")

        self.manager.get_screen("bot_selector").prepare(bot_type)
        self.manager.current = "bot_selector"

