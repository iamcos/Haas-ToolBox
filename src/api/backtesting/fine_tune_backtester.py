from api.backtesting.bot_backtester import BotBacktester
from api.domain.dtos import BacktestResult, BacktestSetupInfo
from dataclasses import dataclass


@dataclass(frozen=True)
class FineTuneBacktester:
    _bot_backtester: BotBacktester

    def execute(
        self,
        setup: BacktestSetupInfo,
        length: int = 10
    ) -> BacktestResult:

        self._bot_backtester.setup(setup)

        for i in range(0, length * 2 + 1):
            if i % 2 == 0:
                self._bot_backtester.backtest_up()
            else:
                self._bot_backtester.backtest_down()

        return self._bot_backtester.set_best_result();

