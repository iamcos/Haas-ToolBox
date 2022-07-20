from typing import Any, Iterable, Protocol


class BacktestingStrategy(Protocol):
    def set_step(self, step: Any) -> None: ...
    def count_up(self, value: str, used_values: Iterable) -> str: ...
    def count_down(self, value: str, used_values: Iterable) -> str: ...


class FloatBacktestingStrategy:
    def set_step(self, step: Any) -> None:
        self._check_value(step);
        self._step: float = float(step)

    def count_up(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: float = self._smart_round(value)
        print(f"{new_value=}, {used_values=}")

        while str(new_value) in used_values:
            new_value += self._step

        return str(new_value)

    def count_down(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: float = self._smart_round(value)

        while str(new_value) in used_values:
            new_value -= self._step

        return str(new_value)

    def _smart_round(self, value: str) -> float:
        # numbers_after_dot: int = len(str(self._step)[2:])
        # return round(float(value), numbers_after_dot)
        return float(value)

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


class IntBacktestingStrategy:
    def set_step(self, step: Any) -> None:
        self._check_value(step);
        self._step: int = int(step)

    def count_up(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: int = int(value)
        print(f"{value=}, {used_values=}")
        while str(new_value) in used_values:
            new_value += self._step

        return str(new_value)

    def count_down(self, value: str, used_values: Iterable) -> str:
        self._check_value(value)
        new_value: int = int(value)

        while str(new_value) in used_values:
            new_value -= self._step

        return str(new_value)

    def _check_value(self, value: Any) -> None:
        checkers = (
            lambda v: v is None,
            lambda v: type(v) is str and not value.isdigit(),
        )

        for checker in checkers:
            if checker(value):
                raise ValueError(f"Passed not a float like value: {value}")

