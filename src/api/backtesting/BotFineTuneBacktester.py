import random

from api.backtesting.interface_fine_tune_backtester import InterfaceFineTuneBacktester
from api.domain.dtos import BotFineTuneSetup, InterfaceFineTuneSetup
from api.domain.types import Interface
from api.loader import log
from api.wrappers.interface_wrapper import InterfaceWrapper
from dataclasses import dataclass


@dataclass(frozen=True)
class BotFineTuneBacktester:
    _interface_fine_tune_backtester: InterfaceFineTuneBacktester

    def execute(self, setup: BotFineTuneSetup) -> None:
        directed_setups = self._direct_setups(setup)
        
        for interface in directed_setups:
            interface_name = InterfaceWrapper(interface).name
            log.info(f"Fine tune for {interface_name}");
            interface_setup = InterfaceFineTuneSetup(
                bot_guid=setup.bot_guid,
                interface=interface,
                ticks=setup.ticks,
                length=setup.length
            )
            self._interface_fine_tune_backtester.execute(interface_setup)

    def _direct_setups(
        self,
        setup: BotFineTuneSetup
    ) -> list[Interface]:
        if setup.direction is None:
            names = [InterfaceWrapper(i).name for i in setup.interfaces]
            random.shuffle(names)
            setup.direction = names

        setups = list(setup.interfaces)

        for i, interface in enumerate(setup.interfaces):
            name: str = InterfaceWrapper(interface).name
            j: int = setup.direction.index(name)

            if i != j:
                setups[i], setups[j] = setups[j], setups[i]
                
        return setups

