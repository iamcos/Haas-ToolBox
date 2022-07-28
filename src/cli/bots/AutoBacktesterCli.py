from typing import Protocol


class AutoBacktesterCli(Protocol):
    def start(self) -> None: ...
