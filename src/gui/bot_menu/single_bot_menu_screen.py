from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from kivy.lang import Builder

from api.models import Bot
from api.type_specifiers import get_bot_type
from gui.bot_menu.base_bot_menu_screen import BaseBotMenuScreen
from gui.default_widgets import LabelButton
from loguru import logger as log


Builder.load_file("./src/gui/bot_menu/single_bot_menu_screen.kv")


class SingleBotMenuScreen(BaseBotMenuScreen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot: Bot

        self.add_main_option("Select interface", self.select_interface)
        self.add_main_option("Select another bot", self.select_another_bot)

        self.add_additional_option(
            MadHatterBot,
            {"Config backtesting": self.config_backtesting}
        )

        self.add_additional_option(
            ScalperBot,
            {"Range backtesting": self.range_backtesting}
        )

    def prepare(self, bot: Bot) -> None:
        self.bot = bot
        self.generate_buttons(bot)

    def select_interface(self, _: LabelButton) -> None:
        self.manager.get_screen("interface_selector").setup(self.bot)
        self.manager.current = "interface_selector"

    def select_another_bot(self, _: LabelButton) -> None:
        self.manager.current = "bot_selector"

    def config_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Config backtesting")
        self.manager.get_screen("config_backtester_screen").setup(self.bot)

    def range_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Range backtesting")
