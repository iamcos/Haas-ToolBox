from api.backtesting.BotBacktester import BotBacketster
from gui.backtesting.widgets import BacktestingInfoLayout
from gui.default_widgets import LogsLayout, TextLabel
from concurrent.futures import ThreadPoolExecutor
from time import monotonic
from typing import Callable, Optional
from loguru import logger as log


class SingleBacktester:
    def __init__(
        self,
        backtester: BotBacketster,
        logger: LogsLayout,
        backtesting_info: BacktestingInfoLayout
    ) -> None:
        self.backtester: BotBacketster = backtester
        self.logger: LogsLayout = logger
        self.backtesting_info: BacktestingInfoLayout = backtesting_info

        self.backtesting_actions: dict[tuple[str, str], list[Callable]]
        self.hotkeys: set[str]
        self.executor = ThreadPoolExecutor(max_workers=1)

        self._init_backtesting_actions_dict()
        self._init_backtesting_hotkeys()

    def process_button_release(self, instanse) -> None:
        for key, actions in self.backtesting_actions.items():
            if key[0] == instanse.text:
                self.logger.info(key[0])
                for action in actions:
                    self.executor.submit(self._task, action)

    def process_hotkey_release(self, hotkey: str) -> None:
        if hotkey in self.hotkeys:
            for key, actions in self.backtesting_actions.items():
                if key[1] == hotkey:
                    for action in actions:
                        log_row: TextLabel = self.logger.info(key[0])
                        self.executor.submit(self._task, action, log_row)

    def stop_backtesting(self) -> None:
        self.backtester.stop_backtesting()
            

    def _init_backtesting_actions_dict(self) -> None:
        self.backtesting_actions = {
            ("Backtest up", "k"): [self.backtester.backtest_up],
            ("Backtest down", "j"): [self.backtester.backtest_down],
            ("Length x2", "l"): [self.backtester.backtesting_length_x2],
            ("Length /2", "h"): [self.backtester.backtesting_length_devide2],
            ("Backtest up x10", "Shift + k"): self._run_in_range(
                self.backtester.backtest_up),
            ("Backtest down x10", "Shift + j"): self._run_in_range(
                self.backtester.backtest_down),
        }

    def _init_backtesting_hotkeys(self) -> None:
        self.hotkeys = {key[1] for key in list(self.backtesting_actions)}
    
    # TODO: Move default value to config
    def _run_in_range(self, action: Callable, range_: int = 10) -> list[Callable]:
        return [action for _ in range(range_)]

    def _task(self, action: Callable, log_row: Optional[TextLabel] = None):
        log.debug("Starting task")
        start: float = monotonic()
        res = action()
        end = monotonic() - start

        log.debug(f"{res=}")

        match res:
            case None:
                return
            case value, roi:
                self.logger.info(
                    f"ROI: [{roi}]; Value: [{value}]; Time: [{end:.2f}s]",
                    log_row)
                self.backtesting_info.update(value, roi)
            case ticks:
                self.logger.info(f"Ticks: {ticks}", log_row)

