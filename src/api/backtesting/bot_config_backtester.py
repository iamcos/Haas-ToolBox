import threading

from collections import defaultdict
from typing import Generator, Iterable
from api.backtesting.bot_editor import BotEditor
from api.bot_manager import ApiV3BotManager, BotManager
from api.domain.dtos import BotConfigSetup

from api.providers.bot_api_provider import BotApiProvider

from api.wrappers.interface_wrapper import InterfaceWrapper
from api.domain.types import Bot, Interface, ROI, GUID, InterfaceOption, OptionValue

from time import monotonic

from loguru import logger as log
from api.exceptions import BotException


"""
Config sample example:

    "0": {                                          # 0 is a sample id
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

ConfigBacktestResult = dict[ROI, set[GUID]]


class BotConfigBacktester:
    def __init__(
        self,
        api: BotApiProvider,
        editor: BotEditor,
        setup: BotConfigSetup
    ) -> None:
        self._api = api
        self._setup: BotConfigSetup = setup
        self._editor: BotEditor = editor
        self._manager = self._setup_bot_manager()

    def _setup_bot_manager(self) -> BotManager:
        manager: BotManager = ApiV3BotManager(self._api)
        manager.set_bot(self._setup.bot_guid)
        return manager

    def start(self) -> None:
        log.info("Starting config backtesting")
        with self._manager.new_bot():
            results: defaultdict[ROI, set[GUID]] = self._process_backtesting()
            self._delete_useless_bots(results)

    def _process_backtesting(self) -> defaultdict[ROI, set[GUID]]:
        finish: bool = False
        results: defaultdict[ROI, set[GUID]] = defaultdict(lambda: set())
        results[self._manager.roi()].add(self._manager.guid())

        def target():
            for _ in self._generate_backtested_bots():
                roi: ROI = self._manager.roi()
                backtested_bot_guid: GUID = self._manager.guid()
                results[roi].add(backtested_bot_guid)

                if finish:
                    break

        t = threading.Thread(target=target)

        try:
            t.start()
            t.join()
        except (KeyboardInterrupt, BotException):
            finish = True
            log.warning("Stopping backtesting...")
            t.join()

        return results

    def _delete_useless_bots(self, result: ConfigBacktestResult ) -> None:
        roi_to_delete = self._get_roi_to_delete(result)

        for roi in roi_to_delete:
            for guid in result[roi]:
                self._api.delete_bot(guid)

    def _generate_backtested_bots(self) -> Generator[None, None, None]:
        for sample in self._get_bot_samples():
            modes, interfaces = self._decompose_sample(sample)
            self._reconfigure_bot(interfaces)

            start: float = monotonic()
            self._api.backtest_bot(self._setup.bot_guid, self._setup.ticks)
            time: float = monotonic() - start
            roi: ROI = self._manager.roi()

            log.info(f"ROI: {roi}, Time passed: {time:.2f}s")

            clone: Bot = self._api.clone_and_save_bot(self._setup.bot_guid)
            self._manager.set_bot(clone)

            yield

    def _decompose_sample(self, sample: dict) -> tuple[dict, list[dict]]:
        modes: dict = sample['modes']
        interfaces: list[dict] = []

        for key, value in sample.items():
            if key != "modes":
                interfaces.append({key: value})

        return (modes, interfaces)

    def _delete_all_created_bots(
        self,
        results: defaultdict[ROI, set[GUID]]
    ) -> None:
        for guids in list(results.values()):
            for guid in guids:
                self._api.delete_bot(guid)

        log.info("Bots deleted")


    def _get_bot_samples(self) -> list[dict]:
        config = self._setup.config
        batch_size = self._setup.batch_size
        return [list(i.values())[0] for i in config[:batch_size]]

    def _get_roi_to_delete(
        self,
        backtest_results: dict[ROI, set[GUID]]
    ) -> list[ROI]:
        if not backtest_results:
            return []

        rois: list[ROI] = list(backtest_results.keys())

        top_bots_count: int = self._setup.top_bots_count
        res: set[ROI] = set(sorted(rois, reverse=True)[top_bots_count:])
        res.update([i for i in list(backtest_results.keys()) if i <= 0.0])

        return list(set(res))


    def _reconfigure_bot(self, interfaces: list[dict]) -> None:
        for interface in interfaces:
            for interface_name in [*interface]:
                log.debug(f"{interface_name=}, {interface[interface_name]=}")
                options = interface[interface_name]
                self._edit_options(interface_name, options)


    def _get_interface_by_name(self, interface_name: str) -> Interface:
        return [
            i
            for i in self._api.get_all_bot_interfaces(self._setup.bot_guid)
            if InterfaceWrapper(i).name == interface_name
        ][0]

    def _edit_options(
        self,
        interface_type: str,
        interfaces: dict 
    ) -> None:
        for interface_name, options in interfaces.items():
            for option_name, option_value in options.items():
                log.debug(f"{option_name=}, {option_value=}")
                self._editor.edit_option_by_value(
                    interface_name,
                    option_name,
                    option_value
                )

