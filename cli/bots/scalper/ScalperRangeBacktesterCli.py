from api.bots.BotManager import BotManager
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.bots.scalper.ScalperRangeBacktesterApi import ScalperRangeBacktesterApi, BacktestRange, SclaperBacktestSample
from api.scripts.inquirer_wrappers import input_float
from loguru import logger as log
from typing import cast



class ScalperRangeBacktesterCli:

    def __init__(self, manager: BotManager) -> None:
        self.backtester: ScalperRangeBacktesterApi = \
                ScalperRangeBacktesterApi(cast(ScalperBotManager, manager))

        self.default_target_percentage: BacktestRange = BacktestRange(
            0.4,
            0.6,
            0.1
        )

        self.default_stop_loss: BacktestRange = BacktestRange(
            96,
            99,
            0.1
        )

    def start(self) -> None:
        target_percentage: BacktestRange = self._get_target_percentage_range()
        stop_loss: BacktestRange = self._get_stop_loss_range()

        log.info(f"{target_percentage=}, {stop_loss=}")
        self.backtester.backtest(
            SclaperBacktestSample(target_percentage, stop_loss)
        )


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
            f"Input start for {interface_name}: ",
            default_values.end
        )

        step: float = input_float(
            f"Input start for {interface_name}: ",
            default_values.step
        )

        return BacktestRange(start, end, step)


