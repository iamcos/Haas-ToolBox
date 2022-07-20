from __future__ import annotations
from typing import Optional, Protocol
from dataclasses import dataclass
from api import factories

from api.backtesting.backtesting_cache import BacktestingCache
from api.backtesting.backtesting_strategy import BacktestingStrategy
from api.providers.bot_api_provider import BotApiProvider
from api.exceptions import BotBacktesterException
from api.domain.types import GUID, ROI, Interface, InterfaceOption
from api.domain.dtos import BacktestResult, BacktestSample, BacktestSetupInfo
from api.loader import log
from time import monotonic


def timeit(func):
    def inner(*args, **kwargs):
        start: float = monotonic()
        res = func(*args, **kwargs)
        time = "Time passed: {:.2f}s".format((monotonic() - start))
        log.info(time)
        return res
    return inner


class BotBacktester(Protocol):

    def setup(self, info: BacktestSetupInfo) -> None: ...

    def backtest_up(self) -> None: ...

    def backtest_down(self) -> None: ...

    def backtesting_length_x2(self) -> int: ...

    def backtesting_length_devide2(self) -> int: ...

    def stop_backtesting(self) -> None: ...


class ApiV3BotBacketster:

    def __init__(
        self, 
        provider: BotApiProvider,
        cache: BacktestingCache
    ) -> None:
        self.provider: BotApiProvider = provider
        self.cache: BacktestingCache = cache

        self.backtesting_strategy: BacktestingStrategy
        self.info: BacktestSetupInfo

    def setup(self, info: BacktestSetupInfo) -> None:
        self.backtesting_strategy = (factories.get_backtesting_strategy(
                                         info.option.value))
        self.info = info
        self.backtesting_strategy.set_step(self.info.option.step) # type: ignore

    @timeit
    def backtest_up(self) -> BacktestResult:
        log.info("Backtesting up")

        value = self.backtesting_strategy.count_up(
            self.info.option.value,
            self.cache.get_used_values(self.info.ticks))

        self.info.option.value = value

        return self._backtest()

    @timeit
    def backtest_down(self) -> BacktestResult:
        log.info("Backtesting down")

        value = self.backtesting_strategy.count_down(
            self.info.option.value,
            self.cache.get_used_values(self.info.ticks))

        self.info.option.value = value

        return self._backtest()

    def backtesting_length_x2(self) -> int:
        self.info.ticks = self.info.ticks * 2
        log.info(f"{self.info.ticks=}")
        return self.info.ticks

    def backtesting_length_devide2(self) -> int:
        self.info.ticks = self.info.ticks // 2
        log.info(f"{self.info.ticks=}")
        return self.info.ticks

    def stop_backtesting(self) -> None:
        # FIXME: Add saving top results
        self.cache.get_top_samples()

    def _backtest(self) -> BacktestResult:
        self.provider.update_bot_interface_option(
            self.info.option, self.info.bot_guid)

        self.provider.backtest_bot(self.info.bot_guid, self.info.ticks)

        roi: ROI = self.provider.get_refreshed_bot(self.info.bot_guid).roi

        log.info(
            f"{self.info.option.title} "
            f": {self.info.option.value} ROI:{roi}%")

        sample = BacktestSample(
                    self.info.interface.guid,
                    self.info.option,
                    self.info.ticks,roi)

        self.cache.add(sample)

        return BacktestResult(self.info.option.value, roi)

