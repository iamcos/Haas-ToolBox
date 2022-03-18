from __future__ import annotations
from datetime import datetime
from functools import cmp_to_key
from typing import NamedTuple
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.bots.BacktestsCache import BotRoiData
from api.bots.BoostedInterface import BoostedInterface
from api.bots.BotManager import BotManager
from api.bots.trade.TradeBotManager import Interfaces, TradeBotException
from loguru import logger as log
from api.MainContext import main_context


class BotBacketster:

    def __init__(
            self,
            manager: BotManager,
            interface: Interfaces,
            option: IndicatorOption,
            value: str,
            step: str
    ) -> None:
        self.manager = manager
        self.interface = interface
        self.option = option
        self.value = value
        self.step = step
        self.ticks = main_context.config_manager.read_ticks()

        self.used_values: set[_CurrentOptionParameters] = set()
        self.option_num: int = self._get_param_num_of_option()

    def calculate_ticks(self, start_date, interval) -> int:
        delta = datetime.now() - start_date
        delta_minutes = delta.total_seconds() / 60 / interval
        return delta_minutes

    def stop_backtesting(self) -> None:
        max_result: _CurrentOptionParameters = max(
            self.used_values,
            key=cmp_to_key(_compare)
        );

        print(f"{max_result=}")

        self.manager.save_max_result()

    def backtest_up(self) -> None:
        log.info("Backtesting up")

        new_value: int = self._calculate_next_value_up()

        self.manager.edit_interface(self.interface, self.option_num, new_value)
        self.manager.backtest_bot(self.ticks)

        log.info(
            f"{self.option.title}"
            f" : {self.value} ROI:{self.manager.bot_roi()}%")

        self.manager.save_roi(self._get_bot_roi_data())

        self.used_values.add(_CurrentOptionParameters(
            self.manager.bot_roi(),
            self.ticks,
            self.step,
            str(self.value)
        ))

    def backtest_down(self) -> None:
        log.info("Backtesting down")

        self._calculate_next_value_down()

        self.manager.edit_interface(self.interface, self.option_num, self.value)
        self.manager.backtest_bot(self.ticks)

        log.info(
            f"{self.option.title}"
            f" : {self.value} ROI:{self.manager.bot_roi()}%")

        self.manager.save_roi(self._get_bot_roi_data())

    def backtesting_length_x2(self) -> None:
        self.ticks = self.ticks * 2
        log.info(f"{self.ticks=}")

    def backtesting_length_devide2(self) -> None:
        self.ticks = self.ticks // 2
        log.info(f"{self.ticks=}")

    def backtest_steps_down(self, steps: int = 10) -> None:
        for _ in range(steps):
            self.backtest_down()

    def backtest_steps_up(self, steps: int = 10) -> None:
        for _ in range(steps):
            self.backtest_up()

    def _get_param_num_of_option(self) -> int:
        for i, option in enumerate(self._get_indicator_options()):
            if option.title == self.option.title:
                return i

        raise TradeBotException(
            f"Can't find option num of {self.option.title} "
            f"in indicator options {self._get_indicator_options()}"
        )

    def _calculate_next_value_up(self) -> int:
        current_value: int = int(self._smart_round()) + int(float(self.step))

        while current_value in self.used_values:
            log.info(f"{current_value=} already used")
            current_value: int = int(
                float(current_value)
            ) + int(
                float(self.step)
            )

        self.value = current_value

        self.used_values.add(_CurrentOptionParameters(
            self.manager.bot_roi(),
            self.ticks,
            self.step,
            str(self.value)
        ))

        return current_value

    def _calculate_next_value_down(self) -> int:
        current_value: int = int(self._smart_round()) - int(float(self.step))

        while current_value in self.used_values:
            log.info(f"{current_value=} already used")
            current_value = int(
                float(current_value)
            ) - int(
                float(self.step)
            )

        self.value = current_value

        self.used_values.add(_CurrentOptionParameters(
            self.manager.bot_roi(),
            self.ticks,
            self.step,
            str(self.value)
        ))

        return current_value

    def _smart_round(self) -> float:
        numbers_after_dot: int = len(str(self.step)[2:])
        return round(float(self.value), numbers_after_dot)

    def _get_indicator_options(self) -> tuple[IndicatorOption]:
        return BoostedInterface(self.interface).options

    def _get_bot_roi_data(self) -> BotRoiData:
        return BotRoiData(
            self.value,
            self.ticks,
            self.option_num,
            self.interface.guid
        )


class _CurrentOptionParameters(NamedTuple):
    roi: float
    ticks: int
    step: str
    parameter_value: str

def _compare(a: _CurrentOptionParameters, b: _CurrentOptionParameters) -> int:
    if a.roi > b.roi:
        return 1
    return -1


    # def _iterate_parameter(
    #         self, interface,
    #         selectedInterfaceParmeter,
    #         param_num,
    # ) -> None:

    #     value_roi = []
    #     value = self._get_param_value(selectedInterfaceParmeter)
    #     step = self._get_param_step(selectedInterfaceParmeter)

    # if action == "Select another parameter":
    #     if len(value_roi) > 0:
    #         value = sorted(value_roi, key=lambda x: x[0], reverse=True)
    #         log.info(value)
    #         self.manager.edit_param_value(interface, param_num, value)
    # elif action == "Set best value by ROI":
    #     if len(value_roi) > 0:
    #         value = sorted(value_roi, key=lambda x: x[0], reverse=True)
    #         self.manager.edit_param_value(interface, param_num, value)
    #         log.info(value)
