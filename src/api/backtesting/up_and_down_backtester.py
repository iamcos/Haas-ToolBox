from api.backtesting.bot_backtester import BotBacktester
from api.domain.dtos import BacktestResult
from dataclasses import dataclass
from api.loader import log


# TODO: Convert to Command pattern
@dataclass(frozen=True)
class UpAndDownBacktester:
    _bot_backtester: BotBacktester

    def execute(self, length: int = 10) -> BacktestResult:
        cache: set[BacktestResult] = set()
        counter: int = 0
        result: BacktestResult

        while counter < length * 2:
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

        log.debug(f"Up&Down backtesting best result: {result}")
        self._bot_backtester.set_best_result()

        return result

