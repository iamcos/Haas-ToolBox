from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.models import Interfaces


class InterfaceWrapper:
    def __init__(self, interface: Interfaces) -> None:
        self.interface: Interfaces = interface

    @property
    def options(self) -> tuple[IndicatorOption]:
        match self.interface:
            case Safety():
                return tuple(self.interface.safetyInterface)
            case Insurance():
                return tuple(self.interface.insuranceInterface)
            case Indicator():
                return tuple(self.interface.indicatorInterface)
        raise BoostedInterfaceException(
            f"Passes not an interface: {self.interface}")

    @property
    def name(self) -> str:
        match self.interface:
            case Safety():
                return self.interface.safetyName
            case Insurance():
                return self.interface.insuranceName
            case Indicator():
                return self.interface.indicatorName
        raise BoostedInterfaceException(
            f"Passes not an interface: {self.interface}")

    @property
    def guid(self) -> str:
        return self.interface.guid


class BoostedInterfaceException(Exception):
    pass
