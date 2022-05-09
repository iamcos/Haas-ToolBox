from api.backtesting.BotBacktester import BotBacketster
from api.bots.BotManager import BotManager
from api.models import Interfaces
from api.wrappers.InterfaceWrapper import InterfaceWrapper
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import \
    IndicatorOption
from kivy.core.window import Window
from kivy.lang import Builder
from loguru import logger as log
from kivy.uix.screenmanager import Screen
from gui.backtesting.widgets import BacktestingInfoLayout
from gui.default_widgets import LogsLayout
from gui.backtesting.single_backtester import SingleBacktester


Builder.load_file("./src/gui/backtesting/single_backtester_screen.kv")


class SingleBacktesterScreen(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.gui_backtester: SingleBacktester

        self.backtesting_info: BacktestingInfoLayout = BacktestingInfoLayout()
        self.logs_layout: LogsLayout = LogsLayout()

        self.ids.info_grid_layout.add_widget(self.backtesting_info)
        self.ids.info_grid_layout.add_widget(self.logs_layout)

        (Window
            .request_keyboard(self._keyboard_released, self) # type: ignore
            .bind(on_key_down=self._process_shortcut))

    def setup(
        self,
        bot_manager: BotManager,
        interface: Interfaces,
        option: IndicatorOption
    ) -> None:
        backtester = BotBacketster(bot_manager, interface, option)
        self.gui_backtester = SingleBacktester(
                backtester, self.logs_layout, self.backtesting_info)

        self._setup_backtesting_actions()

        self.logs_layout.clear()
        self.backtesting_info.update(
            option.value,
            bot_manager.bot_roi(),
            InterfaceWrapper(interface).name)

    def back_to_option_selector(self) -> None:
        log.debug("Going to interface option selection")
        self.gui_backtester.stop_backtesting()
        self.manager.get_screen("interface_option_selector").update_data()
        self.manager.current = "interface_option_selector"


    def _setup_backtesting_actions(self) -> None:
        if not self.ids.hotkeys_layout.has_hotkeys():
            actions = {
                k: self.gui_backtester.process_button_release
                for k, _ in self.gui_backtester.backtesting_actions.items()
            }
            self.ids.hotkeys_layout.add_actions(actions)


    def _keyboard_released(self):
        self.focus = False

    def _process_shortcut(self, window, keycode, text, modifiers):
        # TODO: Find better option for setting hotkeys
        if self.manager.current != "single_backtester":
            return

        if "shift" in modifiers:
            text = f"Shift + {text}"

        self.gui_backtester.process_hotkey_release(text)

