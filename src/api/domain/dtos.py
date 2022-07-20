import re
import numpy as np
from dataclasses import dataclass
from typing import NamedTuple, Type
from api.domain.types import ROI, GUID, Interface, InterfaceOption


class UsedOptionParameters(NamedTuple):
    roi: float
    ticks: int
    step: str
    parameter_value: str


class BacktestRange(NamedTuple):
    start: float
    end: float
    step: float

    def get_range(self) -> np.ndarray:
        return np.arange(self.start, self.end + self.step, self.step)


class SclaperBacktestSample(NamedTuple):
    target_percentage: BacktestRange
    stop_loss: BacktestRange


class uri:

    pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}") # type: ignore

    def __init__(self, uri: str) -> None:
        if not re.search(self.pattern, uri):
            raise ValueError(f"Wrong uri forman {uri}")
        self.uri = uri

    def __str__(self) -> str:
        return self.uri

    __repr__ = __str__


@dataclass
class Config:
    server: uri = uri("127.0.0.1")
    secret: str = "123"
    year: int = 2022
    month: int = 4
    day: int = 22
    hour: int = 1
    min: int = 30
    target_percentage_start: float = 0.5
    target_percentage_end: float = 2.0
    target_percentage_step: float = 0.1
    stop_loss_start: float = 1.5 
    stop_loss_end: float = 5.0
    stop_loss_step: float = 0.2
    config_backtesting_top_bots_count: int = 5
    config_backtesting_batch_size: int = 50


class BacktestSample(NamedTuple):
    interface_guid: GUID
    option: InterfaceOption
    ticks: int
    roi: ROI


class InterfaceOptionInfo(NamedTuple):
    interface: Interface
    interface_guid: GUID
    option_num: int


@dataclass
class BacktestSetupInfo:
    bot_guid: GUID
    interface: Interface
    option: InterfaceOption
    ticks: int


class BacktestResult(NamedTuple):
    option: InterfaceOption
    value: str
    roi: ROI

