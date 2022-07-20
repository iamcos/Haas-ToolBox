from collections import defaultdict
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption

from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.domain.types import GUID, ROI
from api.loader import main_context, log
from api.domain.dtos import SclaperBacktestSample
from typing import Generator, Iterable
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator

from api.providers.bot_api_provider import BotApiProvider


class ScalperRangeBacktesterApi:

    def __init__(self, api: BotApiProvider) -> None:
        self._api: BotApiProvider = api
        self.ticks: int = main_context.config_manager.read_ticks()

        self.cache: defaultdict[ROI, list[tuple[float, float]]] = \
                defaultdict(list)

    def backtest(self, sample: SclaperBacktestSample, bot_guid: GUID) -> None:
        option1: IndicatorOption = IndicatorOption()
        option2: IndicatorOption = IndicatorOption()

        for data in self._perm_generator(sample):
            log.info(f"Target percentage: {data[0]}, stop loss: {data[1]}")

            self._update_data(data, bot_guid)
            self._api.backtest_bot(bot_guid, self.ticks)

            roi: ROI = self._api.get_refreshed_bot(bot_guid).roi

            log.info(f"Result ROI: {roi}")

            self.cache[roi].append(data)

        self._create_result_bot(bot_guid)


    def _perm_generator(
        self,
        sample: SclaperBacktestSample
    ) -> Generator[tuple[float, float], None, None]:

        for i in sample.target_percentage.get_range():
            for j in sample.stop_loss.get_range():
                yield (round(i, 1), round(j, 1))

    def _create_result_bot(self, bot_guid: GUID) -> None:
        top_roi: ROI = max(list(self.cache.keys()))

        self._update_data(self.cache[top_roi][0], bot_guid)

        self._api.backtest_bot(bot_guid, self.ticks)

    def _update_data(self, data: Iterable, bot_guid: GUID) -> None:
        for value in data:
            option: IndicatorOption = IndicatorOption()
            option.value = str(value)
            self._api.update_bot_interface_option(option, bot_guid)

