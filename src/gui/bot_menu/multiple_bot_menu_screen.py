from api.type_specifiers import get_bot_type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot

from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot

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
            MadHatterBot,
            {"Config backtesting": self.config_backtesting}
        )

        self.add_additional_option(
            ScalperBot,
            {"Range backtesting": self.range_backtesting}
        )

    def prepare(self, bots: set[Bot]) -> None:
        self.bots.update(bots)
        bot: Bot = bots.pop()
        bots.add(bot)

        self.generate_buttons(bot)

    def config_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Config backtesting")

    def range_backtesting(self, _: LabelButton) -> None:
        log.debug(f"Range backtesting")
