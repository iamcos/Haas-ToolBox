from typing import Any, Type
from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from api.bots.BacktestsCache import BacktestsCache, BotRoiData
from api.bots.BotWrapper import BotWrapper

from api.bots.BotManager import BotManager, Interfaces
from api.bots.mad_hatter.MadHatterApiProvider import MadHatterApiProvider, MadHatterException
from itertools import chain
from api.bots.BoostedInterface import BoostedInterface


class MadHatterBotManager(BotManager):
    def __init__(self):
        self._wbot: BotWrapper = BotWrapper()
        self.provider = MadHatterApiProvider()
        self.backtests_cache = BacktestsCache()

    def bot_not_selected(self) -> bool:
        return self._wbot.bot_is_not_set()

    def set_bot(self, bot: MadHatterBot) -> None:
        print(f"Selectd bot: {bot}")
        self._wbot.bot = bot

    def get_available_bots(self) -> tuple[MadHatterBot]:
        return self.provider.get_all_bots()

    def get_interfaces_by_type(self, t: Type[Interfaces]) -> tuple[Interfaces]:
        return self.provider.get_interfaces_by_type(self._wbot.guid, t)

    # TODO: Implement edit interface method
    def refresh_bot(self) -> None:
        self._wbot.bot = self.provider.get_refreshed_bot(self._wbot.bot.guid)

    def backtest_bot(self, interval: int):
        res: HaasomeClientResponse = self.provider.get_backtest_method()(
            self._wbot.guid, interval
        )

        self.provider.process_error(
            res, "Error while backtesting bot")

    def save_roi(self, data: BotRoiData) -> None:
        roi: float = self.bot_roi()
        if roi > 0:
            data._replace(roi=roi)
            self.backtests_cache.add_data(data)

    def bot_roi(self) -> float:
        self.refresh_bot()
        return self._wbot.roi

    def bot_name(self) -> str:
        return "Mad Hatter Bot"

    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        return tuple([Indicator])

    def update_option(self, option: IndicatorOption) -> IndicatorOption:
        cmp = lambda o : o.title == option.title
        res = next(filter(cmp, self._get_all_bot_options()), None)

        if res is None:
            raise MadHatterException(f"Option {option.title} couldn't be found")
        return res

    def _get_all_bot_options(self) -> tuple[IndicatorOption]:
        self.refresh_bot()
        return tuple(chain(*[
            BoostedInterface(i).options
            for i in self.provider.get_all_interfaces(self._wbot.guid)
        ]))

    def edit_interface(self, interface: Interfaces, param_num: int, value: Any):
        edit_func = self.provider.get_edit_interface_method(interface)

        Indicator
        res: HaasomeClientResponse = edit_func(
            self._wbot.guid,
            param_num,
            value
        )

        self.provider.process_error(
            res, "Error while getting edit bot interface settings")

