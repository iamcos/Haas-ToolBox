from typing import NamedTuple, Union

from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety


class BotInterface(NamedTuple):
    name: str
    uppercase_name: str


InterfacesForCli = Union[Safety, Indicator, Insurance, Separator, str]
