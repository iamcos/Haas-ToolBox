from typing import Type

from api.bots.BotManager import BotManager
from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.factories import bot_managers_factory
from api.models import Bot
from gui.bot_menu.base_bot_menu_screen import BaseBotMenuScreen
from gui.default_widgets import LabelButton
from kivy.lang import Builder
from loguru import logger as log


Builder.load_file("./src/gui/bot_menu/multiple_bot_menu_screen.kv")


class MultipleBotMenuScreen(BaseBotMenuScreen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bots: set[Bot] = set()

        self.add_additional_option(
            MadHatterBotManager,
            {"Config backtesting": self.config_backtesting}
        )

        self.add_additional_option(
            ScalperBotManager,
            {"Range backtesting": self.range_backtesting}
        )

    def prepare(self, bots: set[Bot]) -> None:
        self.bots.update(bots)
        bot: Bot = bots.pop()
        bots.add(bot)

        self.bot_manager = bot_managers_factory.get_bot_manager_by_bot(bot)
        bot_manager_type: Type[BotManager] = type(self.bot_manager)

        self.generate_buttons(bot_manager_type)

    def config_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Config backtesting")

    def range_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Range backtesting")
