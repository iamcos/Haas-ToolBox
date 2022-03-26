import json

from api.bots.BotManager import BotManager
from api.bots.InterfaceWrapper import InterfaceWrapper
from api.models import Bot, Interfaces
from api.MainContext import main_context

from time import monotonic

from loguru import logger as log



"""
Sample example:

    "0": {                                          # 0 is a sample counter

        "bot_config": {                             # Keys in bot_config is
            "Interval": 5,                          # unique for each bot Type
            "Indicator Signal Consensus": false,
            "Require FCC": false,
            "Reset Middle": true,
            "Allow Mid Sells": false
        },


        "Indicator": {                              # Here can be
                                                    # Indicator/Insurance/Safety
                                                    # keys

            "Mad Hatter MACD": {                    # Name of interface

                "MACD Fast": 12,                    # Name of option and value
                "MACD Slow": 24,
                "MACD Signal": 5
            },

            "Mad Hatter RSI": {
                "Length": 6,
                "Buy level": 34.0,
                "Sell level": 65.0
            },

            "Mad Hatter BBands": {
                "MA Type": 4,
                "Length": 32,
                "Dev.Up": 0.5,
                "Dev.Down": 0.8
            }
        }

    }

"""

# TODO: Catch KeyboardInterrupt and delete all created bots
class BotConfigBacktester:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager

        # FIXME: Remove hardcoded name of config
        with open("./api/config/mad_hatter_config.json", "r") as f:
            self.config: list = json.load(f)["tests"]

        self.ticks = main_context.config_manager.read_ticks()

    def start_backtesting(self, batch_size: int, top_bots_count: int) -> None:
        self.config = self.config[:batch_size]
        backtest_cache: dict[float, str] = self._backtest()

        roi_to_delete = sorted(list(backtest_cache.keys()),
                                reverse=True)[top_bots_count:]

        for roi in roi_to_delete:
            log.info(f"ROI to delete: {roi}, GUID to delte {backtest_cache[roi]}")
            self.manager.delete_bot(backtest_cache[roi])

    def _backtest(self) -> dict[float, str]:
        backtest_cache: dict[float, str] = {}

        for sample in [list(i.values())[0] for i in self.config]:
            self._reconfigure_bot(sample)
            start: float = monotonic()

            self.manager.backtest_bot(self.ticks)

            log.info(f"{sample=}\n{self.manager.bot_roi()=}")
            log.info("Time passed: {:.2f}s".format(monotonic() - start))

            guid = self.manager.clone_bot_and_save().guid
            backtest_cache[self.manager.bot_roi()] = guid

        return backtest_cache

    def _reconfigure_bot(self, sample: dict) -> None:
        for interface_type in self.manager.get_available_interface_types():
            if interface_type.__name__ in sample:
                interfaces = sample[interface_type.__name__]

                for interface_name, options in interfaces.items():
                    interface: Interfaces = [
                        i
                        for i in self.manager.get_all_interfaces()
                        if InterfaceWrapper(i).name == interface_name
                    ][0]

                    for option_title, value in options.items():
                        option_num: int = self.manager.get_option_num(
                            interface_type, option_title
                        )

                        self.manager.edit_interface(
                            interface,
                            option_num,
                            value
                        )

