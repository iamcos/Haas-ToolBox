from typing import Any, Callable, DefaultDict, NamedTuple, Optional, Union

from haasomeapi.apis.TradeBotApi import TradeBotApi
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumErrorCode import EnumErrorCode

from api.MainContext import main_context
from loguru import logger as log


Interfaces = Union[Indicator, Safety, Insurance]
InterfaceGuid = str


class TradeBotManager:
    def __init__(self):
        self._tradebot: Optional[TradeBot] = None
        self.tradebot_api: TradeBotApi = main_context.trade_bot_api
        self.roi_values: DefaultDict[
            InterfaceGuid, set[TradeBotRoiData]] = DefaultDict(lambda : set())

    def tradebot_not_selected(self) -> bool:
        return self._tradebot is None

    def set_tradebot(self, tradebot: TradeBot):
        self._tradebot = tradebot

    def get_available_tradebots(self) -> list[TradeBot]:
        """
        Gets bots objects from Haas online server
        """
        response: HaasomeClientResponse = self.tradebot_api.get_all_trade_bots()

        if response.errorCode is EnumErrorCode.SUCCESS:
            return response.result
        else:
            raise TradeBotException(
                "Error while getting tradebots list: "
                f"{response.errorCode=} "
                f"{response.errorMessage=}"
            )

    def get_available_interfaces(self, indicator: str) -> tuple[Interfaces]:
        """
        Gets values of all indicators, insurances and safeties
        from current tradebot
        """
        return tuple(getattr(self._tradebot, indicator).values())

    def refresh_bot(self) -> None:
        """
        Gets new trade object from API and sets it to field
        """
        if self._tradebot is None:
            raise TradeBotException("Can't refresh bot, cause it is None")

        response = self.tradebot_api.get_trade_bot(self._tradebot.guid)

        if response.errorCode is EnumErrorCode.SUCCESS:
            self._tradebot = response.result
        else:
            raise TradeBotException(
                "Error while refreshing bot: "
                f"{response.errorCode=} "
                f"{response.errorMessage=}"
            )

    def bot_roi(self) -> float:
        if self._tradebot is None:
            raise TradeBotException("Can't get ROI because tradebot is None")

        self.refresh_bot()
        return self._tradebot.roi

    def update_option(self, option: IndicatorOption) -> IndicatorOption:
        self.refresh_bot()

        for some_option in self._get_all_bot_options():
            if option.title == some_option.title:
                return some_option

        log.error(f"Option {option.title} could not be found in TradeBot options")

        return option

    def _get_all_bot_options(self) -> list[IndicatorOption]:
        if self._tradebot is None:
            raise TradeBotException("Can't get indicator options list from None")

        all_indicator_options: list[IndicatorOption] = []

        for i in self._tradebot.safeties.values():
            all_indicator_options.extend(i.safetyInterface)

        for i in self._tradebot.indicators.values():
            all_indicator_options.extend(i.indicatorInterface)

        for i in self._tradebot.insurances.values():
            all_indicator_options.extend(i.insuranceInterface)

        return all_indicator_options

    def edit_interface(self, interface: Interfaces, param_num: int, value: Any):

        if self._tradebot is None:
            raise TradeBotException("Can't edit interface of None TradeBot")

        edit_func: Union[None, Callable] = None

        if type(interface) is Safety:
            edit_func = self.tradebot_api.edit_bot_safety_settings
        elif type(interface) is Indicator:
            edit_func = self.tradebot_api.edit_bot_indicator_settings
        elif type(interface) is Insurance:
            edit_func = self.tradebot_api.edit_bot_insurance_settings

        if edit_func is None:
            raise TradeBotException(f"Not a Trade Bot interface: {interface}")


        res: HaasomeClientResponse = edit_func(
            self._tradebot.guid,
            interface.guid,
            param_num,
            value
        )

        if res.errorCode is not EnumErrorCode.SUCCESS:
            raise TradeBotException(
                "Error while getting edit bot interface settings: "
                f"{res.errorCode=} "
                f"{res.errorMessage=}"
            )

    def backtest_bot(self, interval: int):
        if self._tradebot is None:
            raise TradeBotException("Can't backtest None tradebot")

        res: HaasomeClientResponse = self.tradebot_api.backtest_trade_bot(
            self._tradebot.guid, interval
        )

        if res.errorCode is not EnumErrorCode.SUCCESS:
            raise TradeBotException(
                "Error while backtesting bot: "
                f"{res.errorCode=} "
                f"{res.errorMessage=}"
            )

    def save_roi(
        self,
        value: Union[str, int],
        ticks: int,
        option_num: int,
        interface_guid: str
    ) -> None:

        roi: float = self.bot_roi()

        if roi > 0:
            self.roi_values[interface_guid].add(
                TradeBotRoiData(value, ticks, option_num, self.bot_roi())
            )

    def save_max_result(
        self,
        option_num: int,
        interface_guid: str
        # params: _CurrentOptionParameters
    ) -> None:
        self.tradebot_api.edit_bot_indicator_settings
        pass


class TradeBotException(Exception):
    pass


class TradeBotRoiData(NamedTuple):
    value: Union[str, int]
    ticks: int
    option_num: int
    roi: float

