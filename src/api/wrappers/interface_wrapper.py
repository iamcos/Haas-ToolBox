from functools import lru_cache
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.domain.types import Interface
from api.exceptions import BoostedInterfaceException


class InterfaceWrapper:
    def __init__(self, interface: Interface) -> None:
        self.interface: Interface = interface

    @property
    @lru_cache
    def options(self) -> tuple[IndicatorOption]:
        match self.interface:
            case Safety():
                return tuple(self.interface.safetyInterface)
            case Insurance():
                return tuple(self.interface.insuranceInterface)
            case Indicator():
                return tuple(self.interface.indicatorInterface)

        raise BoostedInterfaceException(
            f"Passed not an interface: {self.interface}")

    @property
    @lru_cache
    def name(self) -> str:
        match self.interface:
            case Safety():
                return self.interface.safetyName
            case Insurance():
                return self.interface.insuranceName
            case Indicator():
                return self.interface.indicatorName

        raise BoostedInterfaceException(
            f"Passed not an interface: {self.interface}")

    @property
    def guid(self) -> str:
        return self.interface.guid

