from api.bots.BotConfigBacktester import BotConfigBacktester
from api.bots.BotManager import BotManager
from loguru import logger as log
from api.MainContext import main_context
from InquirerPy import inquirer

from api.scripts.config_manager import ConfigManager


class BotConfigBacktestCli:
    def __init__(self, manager: BotManager):
        self.config: ConfigManager = main_context.config_manager
        self.manager: BotManager = manager

    def start(self) -> None:
        log.info("Config backtesting")
        batch_size: int = self._get_batch_size()
        top_bots_count: int = self._get_top_bots_count()
        log.info(
            f"{batch_size=}, {top_bots_count=}"
            f" You can change values in ./api/config/config.ini"
        )
        BotConfigBacktester(self.manager, batch_size, top_bots_count).start()


    def _get_batch_size(self) -> int:
        if self.config.config_backtesting_batch_size != -1:
            return self.config.config_backtesting_batch_size
        else:
            batch_size: int = self._ask_for_batch_size()
            self.config.set_config_backtesting_batch_size(batch_size)
            return batch_size

    def _get_top_bots_count(self) -> int:
        if self.config.config_backtesting_top_bots_count != -1:
            return self.config.config_backtesting_top_bots_count
        else:
            top_bots_count: int = self._ask_for_top_bots_count()
            self.config.set_config_backtesting_top_bots_count(top_bots_count)
            return top_bots_count

    def _ask_for_batch_size(self) -> int:
        return int(inquirer.text(
            message="Input batch size for config backtesting",
            default="50"
        ).execute())

    def _ask_for_top_bots_count(self) -> int:
        return int(inquirer.text(
            message="Input count of backtested bots to create",
            default="5"
        ).execute())

