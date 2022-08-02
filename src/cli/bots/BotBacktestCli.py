from InquirerPy.prompts.list import ListPrompt
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from api.loader import main_context
from api.backtesting.backtesting_cache import BacktestingCache, SetBacktestingCache
from api.domain.dtos import BacktestSetupInfo
from api.providers.bot_api_provider import BotApiProvider
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption

from api.domain.types import GUID, Interface, InterfaceOption
from api.backtesting.bot_backtester import ApiV3BotBacketster, BotBacktester
from api.backtesting.fine_tune_backtester import FineTuneBacktester
from loguru import logger as log


class BacktestCliException(Exception): pass


class BotBacktestCli:
    def __init__(self, provider: BotApiProvider) -> None:
        cache: BacktestingCache = SetBacktestingCache()
        self.ticks: int = main_context.config_manager.read_ticks()

        log.info(f"Ticks: {self.ticks}")

        self.backtester: BotBacktester = ApiV3BotBacketster(
                provider, cache, self.ticks)
        self.provider: BotApiProvider = provider

    def process_backtest(
        self,
        bot_guid: GUID,
        interface: Interface,
        option: InterfaceOption
    ) -> None:
        # TODO: Why and where ?
        if option.step is None:
            raise BacktestCliException("Step must be not None")

        self.info: BacktestSetupInfo = BacktestSetupInfo(
            bot_guid,
            interface,
            option,
            self.ticks
        )

        self.backtester.setup(self.info)

        action = self._get_backtest_promt(option, self.backtester, bot_guid)

        res = action.execute()

        while res != "Select another parameter":
            backtest_data = res()

            log.info(f"{backtest_data=}")
            res = self._get_backtest_promt(
                backtest_data.option, self.backtester, bot_guid
            ).execute()

        self.backtester.set_best_result()


    def _get_backtest_promt(
        self,
        option: IndicatorOption,
        backtester: BotBacktester,
        bot_guid: GUID
    ) -> ListPrompt:

        actions = list([
            {
                "name": "backtest up",
                "value": backtester.backtest_up
            },
            {
                "name": "backtest down",
                "value": backtester.backtest_down
            },
            {
                "name": "Fine tune",
                "value": lambda: FineTuneBacktester(backtester).execute(self.info)
            },
            {
                "name": "backtesting length X 2",
                "value": backtester.backtesting_length_x2
            },
            {
                "name": "backtesting length / 2",
                "value": backtester.backtesting_length_devide2
            },
        ])


        return inquirer.select(
            message="Backtesting !",
            choices=[
                Separator(
                    f"{option.title}: "
                    f"{option.value} |"
                    f" step: {option.step} |"
                    f" ROI: {self.provider.get_refreshed_bot(bot_guid).roi}%"
                ),
                *actions,
                "Select another parameter"
            ],
        )

