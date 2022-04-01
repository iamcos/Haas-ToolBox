from functools import cmp_to_key
from typing import DefaultDict, NamedTuple


InterfaceGuid = str


class BotRoiData(NamedTuple):
    value: str | int
    ticks: int
    option_num: int
    intreface_guid: str
    roi: float = 0.0


class BacktestsCache:
    def __init__(self) -> None:
        self.roi_values: DefaultDict[
            InterfaceGuid, set[BotRoiData]] = DefaultDict(lambda: set())

    def add_data(self, data: BotRoiData) -> None:
        self.roi_values[data.intreface_guid].add(data)

    def get_best_result(
        self,
        interface_guid: InterfaceGuid,
        option_num: int
    ) -> BotRoiData:

        values = [
            i
            for i in self.roi_values[interface_guid]
            if i.option_num == option_num
        ]

        return max(
            values,
            key=cmp_to_key(
                lambda a, b: 1 if a.roi > b.roi else -1
            )
        )

