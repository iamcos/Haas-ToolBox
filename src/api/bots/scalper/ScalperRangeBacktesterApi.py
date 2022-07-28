from collections import defaultdict
from time import monotonic
from haasomeapi.dataobjects.custombots.dataobjects.Safety import IndicatorOption
from typing import Generator
from loguru import logger as log
from api.domain.dtos import SclaperBacktestSample
from api.domain.types import GUID, ROI
from api.providers.bot_api_provider import BotApiProvider


Cache = defaultdict[ROI, list[tuple[float, float]]]


class ScalperRangeBacktesterApi:

    def __init__(
        self,
        bot_guid: GUID,
        provider: BotApiProvider,
        ticks: int
    ) -> None:
        self.cache: Cache = defaultdict(list)
        self._provider: BotApiProvider = provider
        self._bot_guid: GUID = bot_guid
        self.ticks: int = ticks

    @property
    def _bot_roi(self) -> ROI:
        return self._provider.get_refreshed_bot(self._bot_guid).roi

    def backtest(
        self,
        sample: SclaperBacktestSample
    ) -> None:

        for (target_percentage, stop_loss) in self._perm_generator(sample):
            log.info(f"{target_percentage=}, {stop_loss=}")

            self._update_options(target_percentage, stop_loss)

            start = monotonic()
            self._provider.backtest_bot(self._bot_guid, self.ticks)

            log.info(
                f"Result ROI: {self._bot_roi}. "
                f"Time passed: {monotonic() - start:.2f} s"
            )
            self.cache[self._bot_roi].append(
                (target_percentage, stop_loss)
            )

        self._create_result_bot()


    def _perm_generator(
            self,
            sample: SclaperBacktestSample
        ) -> Generator[tuple[float, float], None, None]:
        for i in sample.target_percentage.get_range():
            for j in sample.stop_loss.get_range():
                yield (round(i, 1), round(j, 1))

    def _create_result_bot(self) -> None:
        top_roi: ROI = max(list(self.cache.keys()))
        log.debug(f"All ROIs {list(self.cache.keys())}")

        target_percentage: float = self.cache[top_roi][0][0]
        stop_loss: float = self.cache[top_roi][0][1]
        self._update_options(target_percentage, stop_loss)

        log.debug(f"Top roi {top_roi}, stop_loss = {stop_loss},"
                    f"target_percentage = {target_percentage}")

        self._provider.backtest_bot(self._bot_guid, self.ticks)

    def _update_options(
        self,
        target_percentage: float,
        stop_loss: float
    ) -> None:
        target_percentage_option = IndicatorOption()
        target_percentage_option.title = "Target Percentage"
        target_percentage_option.value = str(target_percentage)

        stop_loss_option = IndicatorOption()
        stop_loss_option.title = "Stop Loss"
        stop_loss_option.value = str(stop_loss)

        log.debug(f"{vars(self._provider)=}")

        self._provider.update_bot_interface_option(
            self._bot_guid,
            "",
            target_percentage_option
        )

        self._provider.update_bot_interface_option(
            self._bot_guid,
            "",
            stop_loss_option
        )

