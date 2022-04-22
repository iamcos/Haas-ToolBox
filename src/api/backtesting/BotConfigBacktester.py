from collections import defaultdict
import json
import threading
from typing import Generator
from api.exceptions import BotBacktesterException

from api.bots.BotManager import BotManager
from api.wrappers.InterfaceWrapper import InterfaceWrapper
from api.config import bots_config_path
from api.models import Interfaces, ROI, GUID
from api.MainContext import main_context

from time import monotonic


from loguru import logger as log
from api.exceptions import BotException

"""
Config sample example:

    "0": {                                          # 0 is a sample counter
        "bot_config": {
            "Interval": 5,
            "Indicator Signal Consensus": false
        },

        "Indicator": {
            "Mad Hatter MACD": {                    # Name of interface
                "MACD Fast": 12,                    # Name of option and value
                "MACD Slow": 24,
                "MACD Signal": 5
            }
        },

        "Safety": {
        },

        "Insurance": {
        }
    }

"""

# finish: bool = False

# def signal_handler(signal, frame):
#     global finish
#     log.debug("Catching keyboard interrupt")
#     a = input("Do you really wnat to stop ?")
#     print(a)
#     print(f"{signal=}, {frame=}")
#     finish = True

# signal.signal(signal.SIGINT, signal_handler)


class BotConfigBacktester:
    def __init__(
        self,
        manager: BotManager,
        batch_size: int,
        top_bots_count: int
    ) -> None:
        self.manager: BotManager = manager

        self.batch_size: int = batch_size
        self.top_bots_count: int = top_bots_count
        self.config: dict = self._load_config_from_json()
        self.ticks = main_context.config_manager.read_ticks()

    def _load_config_from_json(self) -> dict:
        file_name: str = bots_config_path.format(
            bot_config_name=self.manager.bot_name())
        try:
            with open(file_name, "r") as f:
                return json.load(f)["tests"]
        except FileNotFoundError:
            raise BotBacktesterException(f"File not found in {file_name}")


    def start(self) -> None:
        with self.manager.new_bot():
            results: defaultdict[ROI, set[GUID]] = self._process_backtesting()
            self._delete_useless_bots(results)

    def _delete_useless_bots(self, backtest_results: dict[ROI, set[GUID]]) -> None:
        roi_to_delete = self._get_roi_to_delete(backtest_results)

        for roi in roi_to_delete:
            for guid in backtest_results[roi]:
                self.manager.delete_bot(guid)


    def _process_backtesting(self) -> defaultdict[ROI, set[GUID]]:
        finish: bool = False
        results: defaultdict[ROI, set[GUID]] = defaultdict(lambda: set())
        results[self.manager.bot_roi()].add(self.manager.bot_guid())

        def target():
            for _ in self._generate_backtested_bots():
                roi: ROI = self.manager.bot_roi()
                backtested_bot_guid: GUID = self.manager.bot_guid()
                results[roi].add(backtested_bot_guid)

                if finish:
                    self._delete_all_created_bots(results)
                    break

        t = threading.Thread(target=target)

        try:
            t.start()
            t.join()
            return results
        except (KeyboardInterrupt, BotException):
            finish = True
            t.join()
            raise BotBacktesterException(
                "Stopping backtesting, created bots will be deleted soon.")



    def _generate_backtested_bots(self) -> Generator[None, None, None]:
        for sample in self._get_bot_samples():
            self._reconfigure_bot(sample)

            start: float = monotonic()

            self.manager.backtest_bot(self.ticks)

            log.info(
                "ROI: {}, Time passed: {:.2f}s".format(
                    self.manager.bot_roi(),monotonic() - start))

            self.manager.set_bot(self.manager.clone_bot_and_save())
            yield

    def _delete_all_created_bots(
        self,
        results: defaultdict[ROI, set[GUID]]
    ) -> None:
        for guids in list(results.values()):
            for guid in guids:
                self.manager.delete_bot(guid)
        log.debug("Bots deleted")


    def _get_bot_samples(self) -> list[dict]:
        return [list(i.values())[0] for i in self.config[:self.batch_size]]

    def _get_roi_to_delete(
        self,
        backtest_results: dict[ROI, set[GUID]]
    ) -> list[ROI]:
        if not backtest_results:
            return []

        rois: list[ROI] = list(backtest_results.keys())

        res: set[ROI] = set(sorted(rois, reverse=True)[self.top_bots_count:])
        res.update([i for i in list(backtest_results.keys()) if i <= 0.0])

        return list(set(res))


    def _reconfigure_bot(self, sample: dict) -> None:
        for interface_type in self.manager.get_available_interface_types():
            if interface_type.__name__ in sample:
                interfaces: dict = sample[interface_type.__name__]

                for interface_name, options in interfaces.items():
                    interface: Interfaces = self._get_interface_by_name(
                        interface_name)
                    self._edit_options(options, interface)


    def _get_interface_by_name(self, interface_name: str) -> Interfaces:
        return [
            i
            for i in self.manager.get_all_interfaces()
            if InterfaceWrapper(i).name == interface_name
        ][0]

    def _edit_options(self, options: dict, interface: Interfaces) -> None:
        for option_title, value in options.items():
            option_num: int = self.manager.get_option_num(
                type(interface), option_title
            )

            self.manager.edit_interface(
                interface,
                option_num,
                value
            )

