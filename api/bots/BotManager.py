import itertools
from typing import Type, Any

from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from api.bots.InterfaceWrapper import InterfaceWrapper
from api.bots.BacktestsCache import BotRoiData

from api.bots.BotApiProvider import Bot, BotApiProvider, Interfaces
from api.bots.BacktestsCache import BacktestsCache, BotRoiData
from api.bots.BotWrapper import BotWrapper
from api.bots import bot_provider_factory
from loguru import logger as log



# FIXME: made _wbot public
class BotManager():
    def __init__(self, t: Type[Bot]) -> None:
        self._wbot: BotWrapper = BotWrapper()
        self.backtests_cache = BacktestsCache()
        self.provider: BotApiProvider = bot_provider_factory.get_provider(t)
        self.bot_name_from_class: str = t.__name__

    def bot_not_selected(self) -> bool:
        return self._wbot.bot_is_not_set()

    def set_bot(self, bot: Bot) -> None:
        self._wbot.bot = bot

    def get_available_bots(self) -> tuple[Bot]:
        return self.provider.get_all_bots()

    def get_interfaces_by_type(self, t: Type[Interfaces]) -> tuple[Interfaces]:
        return self.provider.get_interfaces_by_type(self._wbot.guid, t)

    def get_all_interfaces(self) -> tuple[Interfaces, ...]:
        res: list[Interfaces] = []
        for i in self.provider.get_available_interface_types():
            res.extend(self.get_interfaces_by_type(i))
        return tuple(res)

    def refresh_bot(self) -> None:
        self._wbot.bot = self.provider.get_refreshed_bot(self._wbot.bot.guid)

    def bot_name(self) -> str:
        return self.bot_name_from_class

    def get_available_interface_types(self) -> tuple[Type[Interfaces], ...]:
        return self.provider.get_available_interface_types()

    def update_option(self, option: IndicatorOption) -> IndicatorOption:
        cmp = lambda o : o.title == option.title
        res = next(filter(cmp, self._get_all_bot_options()), None)

        self.provider.process_error(res, f"Option {option.title} couldn't be found")
        log.info(f"Update option: {vars(res)}")
        return res

    def _get_all_bot_options(self) -> tuple[IndicatorOption]:
        self.refresh_bot()
        return tuple(itertools.chain(*[
            InterfaceWrapper(i).options
            for i in self.provider.get_all_interfaces(self._wbot.guid)
        ]))

    def save_max_result(self, interface: Interfaces, option_num: int) -> None:
        res = self.backtests_cache.get_best_result(
            InterfaceWrapper(interface).guid, option_num
        )

        log.info(f"Best result: {res}")
        self.edit_interface(interface, option_num, res.value)
        self.refresh_bot()

    def edit_interface(self, interface: Interfaces, param_num: int, value: Any):
        self.provider.edit_interface(
            interface,
            param_num,
            value,
            self._wbot.guid
        )

    def backtest_bot(self, ticks: int):
        res: HaasomeClientResponse = self.provider.get_backtest_method()(
            self._wbot.guid, ticks
        )

        self.provider.process_error(
            res, "Error while backtesting bot")

    def bot_roi(self) -> float:
        self.refresh_bot()
        return self._wbot.roi

    def save_roi(self, data: BotRoiData) -> None:
        roi: float = self.bot_roi()
        data = data._replace(roi=roi)
        self.backtests_cache.add_data(data)

    def get_option_num(
        self,
        interface_type: Type[Interfaces],
        option_title: str
    ) -> int:
        for i in self.get_interfaces_by_type(interface_type):
            for j, option in enumerate(InterfaceWrapper(i).options):
                if option.title == option_title:
                    return j

        self.provider.process_error(
            message=f"Option num not found for {option_title}")

    def clone_bot_and_save(self) -> Bot:
        return self.provider.clone_bot_and_save(self._wbot.bot)

    def delete_bot(self, bot_guid: None | str = None) -> None:
        if bot_guid is None:
            self.provider.delete_bot(self._wbot.guid)
        else:
            self.provider.delete_bot(bot_guid)

