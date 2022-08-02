from typing import Protocol, Optional
from api.domain.dtos import BacktestSample


class BacktestingCache(Protocol):
    def add(self, sample: BacktestSample) -> None: ...
    def get_top_samples(self, count: int = 1) -> list[BacktestSample]: ...
    def get_used_samples(self, ticks: int) -> list[BacktestSample]: ...
    def get_used_values(self, ticks: int) -> list[str]: ...
    def clear(self) -> None: ...


class SetBacktestingCache:
    def __init__(self) -> None:
        self._cache: set[BacktestSample] = set()
        self.start_sample: Optional[BacktestSample] = None

    def add(self, sample: BacktestSample) -> None:
        if self.start_sample is None:
            self.start_sample = sample

        self._cache.add(sample)

    def get_top_samples(self, count: int = 1) -> list[BacktestSample]:
        sorted_cache: list[BacktestSample] = sorted(
                self._cache, key=lambda x: x.roi, reverse=True)

        sorted_cache = sorted_cache[:count]

        if sorted_cache[0].roi > 0:
            return sorted_cache

        if self.start_sample is not None:
            return [self.start_sample]

        return []

    def get_used_samples(self, ticks: int) -> list[BacktestSample]:
        return [s for s in self._cache if s.ticks == ticks]

    def get_used_values(self, ticks: int) -> list[str]:
        return [s.option.value for s in self._cache if s.ticks == ticks]

    def clear(self) -> None:
        self._cache = set()
        self.start_sample = None

