from collections import defaultdict

from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.MainContext import main_context
from api.models import SclaperBacktestSample
from typing import Generator
from loguru import logger as log
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator

from api.models import ROI


class ScalperRangeBacktesterApi:

    def __init__(self, manager: ScalperBotManager) -> None:
        self.manager: ScalperBotManager = manager
        self.cache: defaultdict[ROI, list[tuple[float, float]]] = \
                defaultdict(list)
        self.ticks = main_context.config_manager.read_ticks()

    def backtest(
        self,
        sample: SclaperBacktestSample
    ) -> None:

        for (target_percentage, stop_loss) in self.perm_generator(sample):
            log.info(f"{target_percentage=}, {stop_loss=}")

            self.manager.edit_interface(Indicator(), 1, target_percentage)
            self.manager.edit_interface(Safety(), 2, stop_loss)

            self.manager.backtest_bot(self.ticks)

            log.info(f"Result ROI: {self.manager.bot_roi()}")
            self.cache[self.manager.bot_roi()].append(
                (target_percentage, stop_loss)
            )

        self._create_result_bot()


    def perm_generator(
            self,
            sample: SclaperBacktestSample
        ) -> Generator[tuple[float, float], None, None]:
        for i in sample.target_percentage.get_range():
            for j in sample.stop_loss.get_range():
                yield (round(i, 1), round(j, 1))

    def _create_result_bot(self) -> None:
        top_roi: ROI = max(list(self.cache.keys()))

        self.manager.edit_interface(
            Indicator(),
            1,
            self.cache[top_roi][0][0]
        )
        self.manager.edit_interface(
            Safety(),
            2,
            self.cache[top_roi][0][1]
        )

        self.manager.backtest_bot(self.ticks)

