import json
from api.backtesting.bot_config_backtester import BotConfigBacktester
from api.backtesting.bot_editor import ApiProviderBotEditor, BotEditor
from api.config_manager import ConfigManager
from api.config import toolbox_settings_path, bots_config_path
from api.domain.dtos import BotConfigSetup
from api.domain.types import GUID
from api.exceptions import BotBacktesterException
from api.providers.bot_api_provider import BotApiProvider
from api.wrappers.bot_wrapper import BotWrapper
from cli.inquirer_wrappers import input_int
from loguru import logger as log


class BotConfigBacktestCli:
    def __init__(
        self,
        bot_guid: GUID,
        provider: BotApiProvider,
        config: ConfigManager
    ) -> None:
        self.bot_guid: GUID = bot_guid
        self.provider: BotApiProvider = provider
        self.config: ConfigManager = config

    def start(self, ticks: int = 1000) -> None:
        log.info("Config backtesting")

        batch_size: int = self._get_batch_size()
        top_bots_count: int = self._get_top_bots_count()

        log.info(
            f"{batch_size=}, {top_bots_count=}"
            f" You can change values in {toolbox_settings_path}"
        )

        setup = BotConfigSetup(
            self.bot_guid,
            batch_size,
            top_bots_count,
            ticks,
            self._load_config_from_json()
        ) 

        editor: BotEditor = ApiProviderBotEditor(self.provider, self.bot_guid)
        BotConfigBacktester(self.provider, editor, setup).start()

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

    def _load_config_from_json(self) -> dict:
        bot_wrapper = BotWrapper(
                self.provider.get_refreshed_bot(self.bot_guid))

        file_name: str = bots_config_path.format(
            bot_config_name=bot_wrapper.name)

        try:
            with open(file_name, "r") as f:
                return json.load(f)["tests"]
        except FileNotFoundError:
            raise BotBacktesterException(f"File not found in {file_name}")

