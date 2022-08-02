import random

from api.backtesting.fine_tune_backtester import FineTuneBacktester
from api.domain.dtos import BacktestSetupInfo, InterfaceFineTuneSetup
from api.domain.types import InterfaceOption
from api.wrappers.interface_wrapper import InterfaceWrapper
from api.loader import log
from dataclasses import dataclass


@dataclass(frozen=True)
class InterfaceFineTuneBacktester:
    _fine_tune_backtester: FineTuneBacktester

    def execute(self, setup: InterfaceFineTuneSetup) -> None:
        directed_options = self._direct_options(setup);

        for option in directed_options:
            setup_info = BacktestSetupInfo(
                setup.bot_guid,
                setup.interface,
                option,
                setup.ticks
            )

            self._fine_tune_backtester.execute(setup_info, setup.length)


    def _direct_options(
        self,
        setup: InterfaceFineTuneSetup
    ) -> list[InterfaceOption]:

        w_interface = InterfaceWrapper(setup.interface)
        options: tuple[InterfaceOption, ...] = w_interface.options

        if setup.direction is None:
            setup.direction = self._generate_random_direction(options);
        
        log.info(f"Backtesting direction: {setup.direction}")

        directed_options: list[InterfaceOption] = [];

        for title in setup.direction:
            option = next((o for o in options if o.title == title))
            directed_options.append(option)

        return directed_options

    def _generate_random_direction(
        self,
        options: tuple[InterfaceOption, ...]
    ) -> list[str]:
        titles: list[str] = [o.title for o in options]
        random.shuffle(titles) 
        return titles

