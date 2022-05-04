from concurrent.futures import ThreadPoolExecutor
from time import monotonic
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget
from api.backtesting.BotBacktester import BotBacketster

from api.bots.BotManager import BotManager
from typing import Callable

from api.models import ROI, Interfaces
from api.wrappers.InterfaceWrapper import InterfaceWrapper
from loguru import logger as log


Builder.load_file("./src/gui/backtesting/single_backtester_screen.kv")


class BorderWidget(Widget):
    """Class for drawing borders around window"""
    pass


class BacktestingInfoLayout(BoxLayout, BorderWidget):
    """Class for backtesting info layout"""
    pass


class BacktestingInfoLabel(Label):
    """Class for text in backtesting info"""
    pass


class PlotLayout(BoxLayout, BorderWidget):
    """Class for showing plot of backtesting"""
    pass


class LogsLayout(ScrollView, BorderWidget):
    """Class for showing logs of backtesting"""
    pass


class LogsText(Label):
    """Class for logs text"""
    pass


class HotKeysLayout(GridLayout, BorderWidget):
    """Class for showing buttons and hotkeys"""
    pass


class ActionButtonLabel(Button):
    """Class for backtesting button"""
    pass


class ActionHotkeyLabel(Label):
    """Class for backtesting hotkey"""
    pass


class SingleBacktesterScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.bot_manager: BotManager
        self.interface: Interfaces
        self.interface_option: IndicatorOption
        self.backtester: BotBacketster
        self.backtesting_actions: dict[tuple[str, str], Callable]
        self.logs_text: LogsText
        self.task_runner = BacktestingRunner()
        self.hotkeys: set[str] = {key[1] for key in list(self.backtesting_actions)}

        keyboard = Window.request_keyboard(self._keyboard_released, self) # type: ignore
        keyboard.bind(on_key_down=self._keyboard_on_key_down)

    def setup(
        self,
        bot_manager: BotManager,
        interface: Interfaces,
        interface_option: IndicatorOption
    ) -> None:
        self.bot_manager = bot_manager
        self.interface = interface
        self.interface_option = interface_option
        self.backtester = BotBacketster(
                bot_manager, interface, interface_option)

        self.backtesting_actions = {
            ("Backtest up", "k"): self.backtester.backtest_up,
            ("Backtest down", "j"): self.backtester.backtest_down,
            ("Length x2", "l"): self.backtester.backtesting_length_x2,
            ("Length /2", "h"): self.backtester.backtesting_length_devide2,
            ("Backtest up x10", "Shift + k"): self.backtester.backtest_up,
            ("Backtest down x10", "Shift + j"): self.backtester.backtest_up,
        }

        self.setup_backtesting_info()
        self.setup_plot()
        self.setup_logs()
        self.setup_backtesting_actions()

    def setup_backtesting_info(self) -> None:
        layout: BacktestingInfoLayout = BacktestingInfoLayout()

        layout.add_widget(BacktestingInfoLabel(
            text=InterfaceWrapper(self.interface).name))
        self.current_value = BacktestingInfoLabel(
            text=f"Value: {self.interface_option.value}")
        self.current_roi = BacktestingInfoLabel(
            text=f"ROI: {self.bot_manager.bot_roi()}%")
        layout.add_widget(self.current_value)
        layout.add_widget(self.current_roi)

        self.ids.info_grid_layout.add_widget(layout)

    def setup_plot(self) -> None:
        layout: PlotLayout = PlotLayout()
        self.graph = layout
        self.ids.info_grid_layout.add_widget(layout)

    def setup_logs(self) -> None:
        layout: LogsLayout = LogsLayout()
        text:LogsText = LogsText(text="")
        layout.add_widget(text)

        self.logs_text = text
        self.ids.info_grid_layout.add_widget(layout)

    def setup_backtesting_actions(self) -> None:
        for text, hotkey in list(self.backtesting_actions):
            self.ids.hotkeys_layout.add_widget(ActionButtonLabel(
                text=text, on_release=self.process_button_release))
            self.ids.hotkeys_layout.add_widget(ActionHotkeyLabel(
                text=f"[ {hotkey} ]"))

    def process_button_release(self, instanse) -> None:
        for key, value in self.backtesting_actions.items():
            if key[0] == instanse.text:
                self.log(key[0])
                self.task_runner.run_task(self.task, value)

    def process_hotkey_release(self, hotkey: str) -> None:
        for key, value in self.backtesting_actions.items():
            if key[1] == hotkey:
                self.log(key[0])
                self.task_runner.run_task(self.task, value)

    def task(self, action: Callable):
        start: float = monotonic()
        value, roi = action()
        end = monotonic() - start

        self.log(f"ROI: [{roi}]; Value: [{value}]; Time: [{end:.2f}s]")
        self.current_value.text = f"Value: {value}"
        self.current_roi.text = f"ROI: {roi}"


    def backtesting_range_action_wrapper(
        self,
        action: Callable,
        range_: int = 10
    ) -> Callable:
        def inner(_) -> None:
            for _ in range(range_):
                roi, value = action()
                print(f"{roi=}, {value=}")
        return inner
            
    def _keyboard_released(self):
        self.focus = False

    def _keyboard_on_key_down(self, window, keycode, text, modifiers):
        # TODO: Find better option for setting hotkeys
        if self.manager.current != "single_backtester":
            return

        if "shift" in modifiers:
            text = f"Shift + {text}"

        if text in self.hotkeys:
            self.process_hotkey_release(text)

    def log(self, text: str) -> None:
        self.logs_text. text += f"{text}\n"

    def draw_plot(self, roi: ROI) -> None:
        print(f"Drawing plot for {roi=}")

    def back_to_option_selector(self) -> None:
        self.manager.current = "interface_option_selector"
        log.debug("Going to interface option selection")


# FIXME: Move to separeta module
class BacktestingRunner:
    def __init__(self) -> None:
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.futures = []


    def run_task(self, task: Callable, *args) -> None:
        self.futures.append(self.executor.submit(task, *args))
