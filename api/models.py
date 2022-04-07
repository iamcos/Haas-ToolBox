from typing import NamedTuple
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot


class UsedOptionParameters(NamedTuple):
    roi: float
    ticks: int
    step: str
    parameter_value: str


InterfaceGuid = str

# TODO: Add all bots types
Bot = TradeBot | MadHatterBot | ScalperBot

Interfaces = Indicator | Safety | Insurance

ROI = float
GUID = str

