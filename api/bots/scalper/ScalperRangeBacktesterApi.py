from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from api.bots.scalper.ScalperBotManager import ScalperBotManager
from api.MainContext import main_context
from typing import NamedTuple, Generator
from loguru import logger as log
import numpy as np

from api.models import ROI


class BacktestRange(NamedTuple):
    start: float
    end: float
    step: float

    def get_range(self) -> np.ndarray:
        return np.arange(self.start, self.end + self.step, self.step)


class SclaperBacktestSample(NamedTuple):
    target_percentage: BacktestRange
    stop_loss: BacktestRange


class ScalperRangeBacktesterApi:

    def __init__(self, manager: ScalperBotManager) -> None:
        self.manager: ScalperBotManager = manager
        self.cache: dict[ROI, tuple[float, float]] = {}
        self.ticks = main_context.config_manager.read_ticks()

    def backtest(
            self,
            sample: SclaperBacktestSample
        ) -> None:

        for (target_percentage, stop_loss) in self.perm_generator(sample):
            log.info(f"{target_percentage=}, {stop_loss=}")

            self.manager.edit_interface(Indicator(), 1, target_percentage)
            self.manager.edit_interface(Indicator(), 2, stop_loss)

            self.manager.backtest_bot(self.ticks)
            
            log.info(f"Result ROI: {self.manager.bot_roi()}")
            self.cache[self.manager.bot_roi()] = (target_percentage, stop_loss)

        res = sorted(list(self.cache.keys()))
        print(res)

    def perm_generator(
            self,
            sample: SclaperBacktestSample
        ) -> Generator[tuple[float, float], None, None]:
        for i in sample.target_percentage.get_range():
            for j in sample.stop_loss.get_range():
                yield (round(i, 1), round(j, 1))

