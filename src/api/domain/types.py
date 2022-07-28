from typing import Protocol
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot


InterfaceGuid = str

Bot = TradeBot | MadHatterBot | ScalperBot

Interface = Indicator | Safety | Insurance

InterfaceOption = IndicatorOption

ROI = float

GUID = str

OptionValue = str | int | float | bool


class Logger(Protocol):
    def info(self, text: str, *args) -> None:
        ...

    def debug(self, text: str, *args) -> None:
        ...

    def wargning(self, text: str, *args) -> None:
        ...

    def error(self, text: str, *args) -> None:
        ...

