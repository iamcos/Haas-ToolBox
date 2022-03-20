from abc import abstractmethod
from typing import Any, Callable, Optional, Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse


# TODO: Add all bots types
Bot = TradeBot | MadHatterBot
Interfaces = Indicator | Safety | Insurance

class BotApiProvider():
    @abstractmethod
    def get_all_bots(self) -> tuple[Bot]: pass

    @abstractmethod
    def get_all_interfaces(self, guid: str) -> tuple[Interfaces]: pass

    @abstractmethod
    def get_interfaces_by_type(
        self,
        guid: str,
        t: Type[Interfaces]
    ) -> tuple[Interfaces]: pass

    @abstractmethod
    def get_refreshed_bot(self, guid: str) -> Bot: pass

    @abstractmethod
    def get_edit_interface_method(self, t: Interfaces) -> Callable: pass

    @abstractmethod
    def get_backtest_method(self) -> Callable: pass

    @abstractmethod
    def process_error(
        self,
        response: Optional[HaasomeClientResponse] = None,
        message: str = ""
    ) -> Any: pass

    @abstractmethod
    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        pass

