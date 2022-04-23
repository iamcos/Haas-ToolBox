from api.bots.BotManager import BotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.bots.scalper.ScalperRangeBacktesterApi import ScalperRangeBacktesterApi
from api.models import BacktestRange, SclaperBacktestSample
from cli.bots.AutoBacktesterCli import AutoBacktesterCli
from cli.inquirer_wrappers import input_float
from api.config_manager import ConfigManager
from api.MainContext import main_context
from typing import Optional, cast


class ScalperRangeBacktesterCli(AutoBacktesterCli):

    def __init__(self, manager: BotManager) -> None:
        self.backtester: ScalperRangeBacktesterApi = \
                ScalperRangeBacktesterApi(cast(ScalperBotManager, manager))

        self.config: ConfigManager = main_context.config_manager

        self.default_target_percentage: BacktestRange = BacktestRange(
            0.4,
            0.6,
            0.1
        )

        self.default_stop_loss: BacktestRange = BacktestRange(
            0.5,
            1.5,
            1
        )

    @classmethod
    def with_manager(cls, manager: BotManager) -> AutoBacktesterCli:
        return cls(manager)

    def start(self) -> None:
        self.backtester.backtest(
            self._get_backtesting_sample()
        )

    @staticmethod
    def get_name() -> str:
        return "Backtesting in range"

    def _get_backtesting_sample(self) -> SclaperBacktestSample:
        sample: Optional[SclaperBacktestSample] = \
            self.config.scalper_range_backtest_sample

        if sample is None:
            target_percentage: BacktestRange = \
                self._get_target_percentage_range()
            stop_loss: BacktestRange = self._get_stop_loss_range()

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


