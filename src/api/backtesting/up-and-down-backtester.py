from dataclasses import dataclass
from api.backtesting.bot_backtester import BotBacktester
from api.domain.dtos import BacktestResult, UpAndDownBacktesterSetup


# TODO: Convert to Command pattern
@dataclass(frozen=True)
class UpAndDownBacktester:
    _bot_backtester: BotBacktester

    def execute(self, setup: UpAndDownBacktesterSetup) -> BacktestResult:
        cache: set[BacktestResult] = set()
        counter: int = 0
        result: BacktestResult

        while counter < setup.length * 2:
            if counter % 2 == 0:
                result = self._bot_backtester.backtest_up()
            else:
                result = self._bot_backtester.backtest_down()

            cache.add(result)
            counter += 1

        return self._best_roi_option(cache)

    def _best_roi_option(self, cache: set[BacktestResult]) -> BacktestResult:
        result: BacktestResult = cache.pop()
        cache.add(result)

        for item in cache:
            if item.roi > result.roi:
                result = item

        return result

