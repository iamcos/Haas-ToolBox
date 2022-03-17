from typing import DefaultDict, NamedTuple
from api.bots.BotManager import InterfaceGuid


class BotRoiData(NamedTuple):
    value: str | int
    ticks: int
    option_num: int
    roi: float


class BacktestsCache:
    def __init__(self) -> None:
        self.roi_values: DefaultDict[
            InterfaceGuid, set[BotRoiData]] = DefaultDict(lambda: set())

    def add_data(self, data: BotRoiData) -> None:
        pass
