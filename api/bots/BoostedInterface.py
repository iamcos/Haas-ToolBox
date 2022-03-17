from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.bots.BotManager import Interfaces


class BoostedInterface:
    def __init__(self, interface: Interfaces) -> None:
        self.interface: Interfaces = interface

    def indicator_options(self) -> tuple[IndicatorOption]:
        match self.interface:
            case Safety():
                return tuple(self.interface.safetyInterface)
            case Insurance():
                return tuple(self.interface.insuranceInterface)
            case Indicator():
                return tuple(self.interface.indicatorInterface)
        raise BoostedInterfaceException(
            f"Passes not an interface: {self.interface}")


class BoostedInterfaceException(Exception):
    pass
