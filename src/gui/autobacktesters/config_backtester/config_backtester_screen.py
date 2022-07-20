from concurrent.futures.thread import ThreadPoolExecutor
from typing import Generator
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from api.backtesting.BotConfigBacktester import BotConfigBacktester
from api.bots.BotManager import BotManager
from api.factories.bot_managers_factory import get_bot_manager_by_bot
from loguru import logger as log

from api.models import Bot


Builder.load_file("./src/gui/autobacktesters/config_backtester/config_backtester_screen.kv")


class ConfigBacktesterScreen(Screen):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bots: set[Bot] = set()

    def setup(self, bots: set[Bot]) -> None:
        self.bots = bots
        self._update_screen()

    def start_backtesting(self) -> None:
        bots_count: int = len(self.bots)
        log.debug(f"Starting config backtesting for {bots_count} bots")

        if bots_count == 1:
            self.backtest_single_bot()
        else:
            self.backtest_multiple_bots()
        

    def _update_screen(self) -> None:
        self.ids.logs_layout.clear()

    def backtest_single_bot(self) -> None:
        bot_manager: BotManager = self._get_bot_manager()
        bot_manager.set_bot(self.bots.pop())

        exec = ThreadPoolExecutor(max_workers=1)
        backtester = BotConfigBacktester(bot_manager, 50, 5)
        backtester.set_logger(self.ids.logs_layout)
        exec.submit(backtester.start)

    def backtest_multiple_bots(self) -> None:
        exec = ThreadPoolExecutor(max_workers=1)
        for manager in self._bot_managers_generator():
            backtester = BotConfigBacktester(manager, 50, 5)
            backtester.set_logger(self.ids.logs_layout)
            exec.submit(backtester.start)


    def _bot_managers_generator(self) -> Generator[BotManager, None, None]:
        log.debug(f"{self.bots=}")
        bot_manager: BotManager = self._get_bot_manager()
        log.debug(f"{self.bots=}")

        for bot in self.bots:
            bot_manager.set_bot(bot)
            yield bot_manager

    def _get_bot_manager(self) -> BotManager:
        bot: Bot = self.bots.pop()
        self.bots.add(bot)
        return get_bot_manager_by_bot(bot)

