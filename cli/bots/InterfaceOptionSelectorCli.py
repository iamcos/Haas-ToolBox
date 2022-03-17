from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from api.bots.BotManager import BotManager
from api.bots.BotApiProvider import Interfaces
from loguru import logger as log
from InquirerPy import inquirer

from api.bots.trade.TradeBotApiProvider import TradeBotException


class InterfaceOptionSelectorCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager
        self.bot_name: str = manager.bot_name()

    def select_option(self, interface: Interfaces) -> IndicatorOption:
        return self._parameter_selector(
            self._indicator_options(interface)
        )

    def _parameter_selector(
            self,
            indicator_options: list[IndicatorOption]
    ) -> IndicatorOption:

        choices: list[dict[str, str | IndicatorOption]] = [
            {
                "name": f"{i.title} : {i.value}",
                "value": i
            }
            for i in indicator_options
        ]

        selected_option: IndicatorOption = inquirer.select(
            message="Select Parameter",
            choices=choices,
        ).execute()

        log.info(f"{selected_option.__dict__=}")
        return selected_option

    def _indicator_options(
            self,
            source: Interfaces
    ) -> list[IndicatorOption]:
        if type(source) is Safety:
            return source.safetyInterface

        elif type(source) is Indicator:
            return source.indicatorInterface

        elif type(source) is Insurance:
            return source.insuranceInterface

        raise TradeBotException(
            f"No {self.bot_name} interface passed: {type(source)}"
        )

