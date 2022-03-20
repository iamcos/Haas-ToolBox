from abc import abstractmethod
from typing import Type, Any

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.bots.BacktestsCache import BotRoiData

from api.bots.BotApiProvider import Bot, Interfaces
from api.model.models import UsedOptionParameters

InterfaceGuid = str


class BotManager():
    @abstractmethod
    def bot_not_selected(self) -> bool: pass

    @abstractmethod
    def set_bot(self, bot: Bot) -> None: pass

    @abstractmethod
    def get_available_bots(self) -> list[Bot]: pass

    @abstractmethod
    def get_interfaces_by_type(
        self,
        t: Type[Interfaces]
    ) -> tuple[Interfaces, ...]: pass

    # TODO: Create basic impl by using get_interfaces_by_type
    @abstractmethod
    def get_all_interfaces(self) -> tuple[Interfaces, ...]: pass

    @abstractmethod
    def refresh_bot(self) -> None: pass

    @abstractmethod
    def bot_name(self) -> str: pass

    @abstractmethod
    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        pass

    @abstractmethod
    def update_option(self, option: IndicatorOption) -> IndicatorOption: pass

    @abstractmethod
    def save_max_result(self, interface: Interfaces, option_num: int): pass

    @abstractmethod
    def edit_interface(self, interface: Interfaces, option_num: int, value: Any): pass

    @abstractmethod
    def backtest_bot(self, ticks: int) -> None: pass

    @abstractmethod
    def bot_roi(self) -> float: pass

    @abstractmethod
    def save_roi(self, data: BotRoiData) -> float: pass

