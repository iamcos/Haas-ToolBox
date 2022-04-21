from api.bots.BotConfigBacktester import BotConfigBacktester
from api.bots.BotManager import BotManager
from api.MainContext import main_context
from api.config_manager import ConfigManager
from cli.bots.AutoBacktesterCli import AutoBacktesterCli
from cli.inquirer_wrappers import input_int
from loguru import logger as log
from api.config import toolbox_settings_path


class BotConfigBacktestCli(AutoBacktesterCli):
    def __init__(self, manager: BotManager):
        self.config: ConfigManager = main_context.config_manager
        self.manager: BotManager = manager


    @classmethod
    def with_manager(cls, manager: BotManager) -> AutoBacktesterCli:
        return cls(manager)


    def start(self) -> None:
        log.info("Config backtesting")
        batch_size: int = self._get_batch_size()
        top_bots_count: int = self._get_top_bots_count()
        log.info(
            f"{batch_size=}, {top_bots_count=}"
            f" You can change values in {toolbox_settings_path}"
        )
        try:
            BotConfigBacktester(self.manager, batch_size, top_bots_count).start()
        except FileNotFoundError:
            log.warning("Add your own config or wait until we create it")

    @staticmethod
    def get_name() -> str:
        return "Backtesing by config"

    def _get_batch_size(self) -> int:
        if self.config.config_backtesting_batch_size != -1:
            return self.config.config_backtesting_batch_size
        else:
            batch_size: int = input_int(
                "Input batch size for config backtesting",
                50
            )

            self.config.set_config_backtesting_batch_size(batch_size)
            return batch_size

    def _get_top_bots_count(self) -> int:
        if self.config.config_backtesting_top_bots_count != -1:
            return self.config.config_backtesting_top_bots_count
        else:
            top_bots_count: int = input_int(
                "Input count of backtested bots to create",
                5
            )
            self.config.set_config_backtesting_top_bots_count(top_bots_count)
            return top_bots_count

