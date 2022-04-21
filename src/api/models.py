import numpy as np
from typing import NamedTuple, Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot


InterfaceGuid = str

Bot = TradeBot | MadHatterBot | ScalperBot

Interfaces = Indicator | Safety | Insurance

ROI = float
GUID = str


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

