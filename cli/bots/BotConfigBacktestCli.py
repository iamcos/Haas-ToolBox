from api.bots.BotManager import BotManager
from loguru import logger as log


class BotConfigBacktestCli:
    def __init__(self, manager: BotManager):
        self.manager: BotManager = manager


    def start(self) -> None:
        log.info("Config backtesting")
        pass

