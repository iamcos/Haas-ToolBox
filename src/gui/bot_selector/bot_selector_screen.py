from typing import Type
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from api.bots.BotManager import BotManager
from api.factories.bot_managers_factory import get_bot_manager
from api.models import Bot
from gui.default_widgets import LabelButton


Builder.load_file("./src/gui/bot_selector/bot_selector_screen.kv")
bot_name = (
        "{bot.name} "
        "{bot.priceMarket.primaryCurrency}/"
        "{bot.priceMarket.secondaryCurrency}"
)


class BotSelectorScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
        self.bots_map: dict[str, Bot]

    def prepare(self, bot_type: Type) -> None:
        print(f"Hello from prepare: {bot_type=}")

        self.bot_manager = get_bot_manager(bot_type)
        self.generate_bots_map()
        self.generate_bots_buttons()

    def generate_bots_map(self) -> None:
        self.bots_map = {}
        for bot in self.bot_manager.get_available_bots():
            name: str = bot_name.format(bot=bot)
            self.bots_map[name] = bot

    def generate_bots_buttons(self) -> None:
        for name in list(self.bots_map.keys()):
            self.ids.bots_grid.add_widget(LabelButton(
                text=name,
                on_release=self.choose_bot
            ))

    def choose_bot(self, instance: LabelButton) -> None:
        print(f"Choosing bot: {instance.text}")
        self.bot_manager.set_bot(self.bots_map[instance.text])
        self.manager.current = "bot_menu"

