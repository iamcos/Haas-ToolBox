from typing import Any, Iterable, Protocol
from api.backtesting.backtesting_cache import BacktestingCache

from api.domain.dtos import BacktestSample


class BacktestingStrategy(Protocol):
    def set_step(self, step: Any) -> None: ...
    def count_up(self, value: str, used_values: Iterable) -> str: ...
    def count_down(self, value: str, used_values: Iterable) -> str: ...


class FloatBacktestingStrategy:
    def set_step(self, step: float) -> None:
        self._step: float = step

    def count_up(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: float = self._smart_round(value)

        while new_value in used_values:
            new_value += self._step

        return str(new_value)

    def count_down(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: float = self._smart_round(value)

        while new_value in used_values:
            new_value -= self._step

        return str(new_value)

    def _smart_round(self, value: str) -> float:
        numbers_after_dot: int = len(str(self._step)[2:])
        return round(float(value), numbers_after_dot)

    def _check_value(self, value: Any) -> None:
        checkers = (
            lambda v: v is None,
            lambda v: type(v) is str and not (value
                .replace(".", "")
                .replace(",", "")
                .isdigit()),
        )

        for checker in checkers:
            if checker(value):
                raise ValueError(f"Passed not a float like value: {value}")

