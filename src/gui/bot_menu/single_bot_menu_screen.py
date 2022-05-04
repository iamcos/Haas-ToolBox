from typing import Type
from kivy.lang import Builder

from api.bots.BotManager import BotManager
from api.bots.mad_hatter.MadHatterBotManager import MadHatterBotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from gui.bot_menu.base_bot_menu_screen import BaseBotMenuScreen
from gui.default_widgets import LabelButton
from loguru import logger as log


Builder.load_file("./src/gui/bot_menu/single_bot_menu_screen.kv")


class SingleBotMenuScreen(BaseBotMenuScreen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager

        self.add_main_option("Select interface", self.select_interface)
        self.add_main_option("Select another bot", self.select_another_bot)

        self.add_additional_option(
            MadHatterBotManager,
            {"Config backtesting": self.config_backtesting}
        )

        self.add_additional_option(
            ScalperBotManager,
            {"Range backtesting": self.range_backtesting}
        )

    def prepare(self, bot_manager: BotManager) -> None:
        self.bot_manager = bot_manager
        bot_manager_type: Type = type(self.bot_manager)
        self.generate_buttons(bot_manager_type)

    def select_interface(self, _: LabelButton) -> None:
        self.manager.get_screen("interface_selector").setup(self.bot_manager)
        self.manager.current = "interface_selector"

    def select_another_bot(self, _: LabelButton) -> None:
        self.manager.current = "bot_selector"

    def config_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Config backtesting")

    def range_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Range backtesting")
