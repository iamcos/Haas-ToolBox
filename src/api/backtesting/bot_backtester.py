from __future__ import annotations
from collections.abc import Callable
from typing import Any, Protocol

from copy import deepcopy

from api.backtesting.backtesting_cache import BacktestingCache
from api.backtesting.backtesting_strategy import BacktestingStrategy
from api.providers.bot_api_provider import BotApiProvider
from api.domain.types import ROI
from api.domain.dtos import BacktestResult, BacktestSample, BacktestSetupInfo
from api.loader import log
from time import monotonic

from api.wrappers.interface_wrapper import InterfaceWrapper


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
    def backtest_up(self) -> BacktestResult: ...
    def backtest_down(self) -> BacktestResult: ...
    def backtesting_length_x2(self) -> int: ...
    def backtesting_length_devide2(self) -> int: ...
    def set_best_result(self) -> BacktestResult: ...


class ApiV3BotBacketster:

    def __init__(
        self, 
        provider: BotApiProvider,
        cache: BacktestingCache,
        get_backtesting_strategy: Callable[[Any], BacktestingStrategy]
    ) -> None:
        self.provider: BotApiProvider = provider
        self.cache: BacktestingCache = cache
        self.get_backtesting_strategy: Callable[[Any], BacktestingStrategy] = \
                get_backtesting_strategy

        self.backtesting_strategy: BacktestingStrategy
        self.info: BacktestSetupInfo

    def setup(self, info: BacktestSetupInfo) -> None:
        log.info(f"Starting backtestion option {info.option.title}");
        self.backtesting_strategy = (self.get_backtesting_strategy(
                                         info.option.step))
        self.info = info

        option = deepcopy(info.option)
        roi: ROI = self.provider.get_refreshed_bot(info.bot_guid).roi

        sample = BacktestSample(
                    info.interface.guid,
                    option,
                    info.ticks,
                    roi)

        self.cache.add(sample)

        self.backtesting_strategy.set_step(self.info.option.step) # type: ignore

    @timeit
    def backtest_up(self) -> BacktestResult:
        log.info("Backtesting up")

        value = self.backtesting_strategy.count_up(
            self.info.option.value,
            self.cache.get_used_values(self.info.ticks))

        log.info(f"{value=}")

        self.info.option.value = value

        return self._backtest()

    @timeit
    def backtest_down(self) -> BacktestResult:
        log.info("Backtesting down")

        value = self.backtesting_strategy.count_down(
            self.info.option.value,
            self.cache.get_used_values(self.info.ticks))

        log.info(f"{value=}")

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

    def set_best_result(self) -> BacktestResult:
        sample: BacktestSample = self.cache.get_top_samples().pop()
        roi: ROI = self.provider.get_refreshed_bot(self.info.bot_guid).roi

        self.info.option = sample.option
        log.info(f"Setting best result for {sample.option.title} "
                f"with value: {sample.option.value} and ROI: {roi} ")
        self._backtest()

        return BacktestResult(sample.option, roi)

    def _backtest(self) -> BacktestResult:
        interface_name: str = InterfaceWrapper(self.info.interface).name
        self.provider.update_bot_interface_option(
            self.info.bot_guid,
            interface_name,
            self.info.option
        )

        self.provider.backtest_bot(self.info.bot_guid, self.info.ticks)

        roi: ROI = self.provider.get_refreshed_bot(self.info.bot_guid).roi

        log.info(
            f"{self.info.option.title} "
            f": {self.info.option.value} ROI:{roi}%")

        new_option = deepcopy(self.info.option)

        sample = BacktestSample(
                    self.info.interface.guid,
                    new_option,
                    self.info.ticks,roi)

        self.cache.add(sample)

        return BacktestResult(new_option, roi)

