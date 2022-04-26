from typing import Type
from haasomeapi.dataobjects.custombots.FlashCrashBot import FlashCrashBot
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file("./src/gui/bot_selector/bot_selector_screen.kv")


bot_types_map: dict[str, Type] = {
    "trade": TradeBot,
    "mad_hatter": MadHatterBot,
    "scalper": ScalperBot,
    "flash_crash": FlashCrashBot,
}


class BotTypeButton(Button):
    pass


class BotSelectorScreen(Screen):

    def choose_bot(self, name: str) -> None:
        print(f"Type is {bot_types_map[name]}, {name=}")

