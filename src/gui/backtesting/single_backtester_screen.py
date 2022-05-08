from concurrent.futures import ThreadPoolExecutor
from time import monotonic
from typing import Callable, Optional

from api.backtesting.BotBacktester import BotBacketster
from api.bots.BotManager import BotManager
from api.models import Interfaces
from api.wrappers.InterfaceWrapper import InterfaceWrapper
from gui.default_widgets import TextLabel
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
    IndicatorOption
from kivy.core.window import Window
from kivy.lang import Builder
from loguru import logger as log
from kivy.uix.screenmanager import Screen
from gui.backtesting.widgets import BacktestingInfoLayout
from gui.default_widgets import LogsLayout


Builder.load_file("./src/gui/backtesting/single_backtester_screen.kv")


# FIXME: Move to separeta module
class TaskRunner:
    def __init__(self) -> None:
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.futures = []

    def run_task(self, task: Callable, *args) -> None:
        self.futures.append(self.executor.submit(task, *args))


class GuiBacktester:
    def __init__(
        self,
        backtester: BotBacketster,
        logger: LogsLayout,
        backtesting_info: BacktestingInfoLayout
    ) -> None:
        self.backtester: BotBacketster = backtester
        self.logger: LogsLayout = logger
        self.backtesting_info: BacktestingInfoLayout = backtesting_info

        self.backtesting_actions: dict[tuple[str, str], Callable]
        self.hotkeys: set[str]
        self.task_runner = TaskRunner()

        self._init_backtesting_actions_dict()
        self._setup_backtesting_hotkeys()

    def _init_backtesting_actions_dict(self) -> None:
        self.backtesting_actions = {
            ("Backtest up", "k"): self.backtester.backtest_up,
            ("Backtest down", "j"): self.backtester.backtest_down,
            ("Length x2", "l"): self.backtester.backtesting_length_x2,
            ("Length /2", "h"): self.backtester.backtesting_length_devide2,
            ("Backtest up x10", "Shift + k"): self.run_in_range(
                self.backtester.backtest_up),
            ("Backtest down x10", "Shift + j"): self.run_in_range(
                self.backtester.backtest_down),
        }
    
    # TODO: Move default value to config
    def run_in_range(self, action: Callable, range_: int = 10) -> Callable:
        def inner():
            for _ in range(range_):
                self._task(action)
        return inner

    def _task(self, action: Callable, log_row: Optional[TextLabel] = None):
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

    def _setup_backtesting_hotkeys(self) -> None:
        self.hotkeys = {key[1] for key in list(self.backtesting_actions)}

    def process_button_release(self, instanse) -> None:
        for key, action in self.backtesting_actions.items():
            if key[0] == instanse.text:
                self.logger.info(key[0])
                self.task_runner.run_task(self._task, action)

    def process_hotkey_release(self, hotkey: str) -> None:
        if hotkey in self.hotkeys:
            for key, action in self.backtesting_actions.items():
                if key[1] == hotkey:
                    log_row: TextLabel = self.logger.info(key[0])
                    self.task_runner.run_task(self._task, action, log_row)

    def backtesting_range_action_wrapper(
        self,
        action: Callable,
        range_: int = 10
    ) -> Callable:
        return lambda: [action() for _ in range(range_)]

    def stop_backtesting(self) -> None:
        self.backtester.stop_backtesting()
            



class SingleBacktesterScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.gui_backtester: GuiBacktester

        self.backtesting_info: BacktestingInfoLayout = BacktestingInfoLayout()
        self.logs_layout: LogsLayout = LogsLayout()

        self.ids.info_grid_layout.add_widget(self.backtesting_info)
        self.ids.info_grid_layout.add_widget(self.logs_layout)

        (Window
            .request_keyboard(self._keyboard_released, self) # type: ignore
            .bind(on_key_down=self._backtesting_shortcuts))

    def setup(
        self,
        bot_manager: BotManager,
        interface: Interfaces,
        option: IndicatorOption
    ) -> None:
        backtester = BotBacketster(bot_manager, interface, option)
        self.gui_backtester = GuiBacktester(
                backtester, self.logs_layout, self.backtesting_info)

        self._setup_backtesting_actions()

        self.logs_layout.clear()
        self.backtesting_info.update(
            option.value,
            bot_manager.bot_roi(),
            InterfaceWrapper(interface).name)

    def _setup_backtesting_actions(self) -> None:
        actions = {
            k: self.gui_backtester.process_button_release
            for k, _ in self.gui_backtester.backtesting_actions.items()
        }
        self.ids.hotkeys_layout.add_actions(actions)

    def _keyboard_released(self):
        self.focus = False

    def _backtesting_shortcuts(self, window, keycode, text, modifiers):
        # TODO: Find better option for setting hotkeys
        if self.manager.current != "single_backtester":
            return

        if "shift" in modifiers:
            text = f"Shift + {text}"

        self.gui_backtester.process_hotkey_release(text)

    def back_to_option_selector(self) -> None:
        log.debug("Going to interface option selection")
        self.gui_backtester.stop_backtesting()
        self.manager.get_screen("interface_option_selector").update_data()
        self.manager.current = "interface_option_selector"


