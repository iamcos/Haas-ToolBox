from api.backtesting.scalper_range_backtester import ScalperRangeBacktesterApi
from api.domain.dtos import BacktestRange, SclaperBacktestSample
from api.domain.types import GUID
from api.providers.bot_api_provider import BotApiProvider
from cli.inquirer_wrappers import input_float
from api.config_manager import ConfigManager
from typing import Optional


class ScalperRangeBacktesterCli:

    def __init__(
        self,
        bot_guid: GUID,
        provider: BotApiProvider,
        config: ConfigManager
    ) -> None:
        ticks: int = config.read_ticks()
        self.backtester = ScalperRangeBacktesterApi(bot_guid, provider, ticks)
        self.config: ConfigManager = config

        # TODO: Add field to config
        self.default_target_percentage = BacktestRange(
            0.4,
            0.6,
            0.1
        )

        self.default_stop_loss = BacktestRange(
            96,
            99,
            1
        )

    def start(self) -> None:
        sample = self._get_backtesting_sample()
        self.backtester.backtest(sample)

    def _get_backtesting_sample(self) -> SclaperBacktestSample:
        sample: Optional[SclaperBacktestSample] = \
            self.config.scalper_range_backtest_sample

        if sample is None:
            target_percentage = self._get_target_percentage_range()
            stop_loss = self._get_stop_loss_range()
            sample = SclaperBacktestSample(target_percentage, stop_loss)
            self.config.set_scalper_range_backtest_sample(sample)

        return sample


    def _get_target_percentage_range(self) -> BacktestRange:
        return self._input_backtesting_range(
            "target percentage",
            self.default_target_percentage
        )

    def _get_stop_loss_range(self) -> BacktestRange:
        return self._input_backtesting_range(
            "stop loss",
            self.default_stop_loss
        )


    def _input_backtesting_range(
            self,
            interface_name: str,
            default_values: BacktestRange
        ) -> BacktestRange:

        start: float = input_float(
            f"Input start for {interface_name}: ",
            default_values.start
        )
        end: float = input_float(
            f"Input end for {interface_name}: ",
            default_values.end
        )

        step: float = input_float(
            f"Input step for {interface_name}: ",
            default_values.step
        )

        return BacktestRange(start, end, step)

