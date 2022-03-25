from InquirerPy.prompts.list import ListPrompt
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption
from api.bots.BotManager import BotManager

from api.models import Interfaces
from api.bots.BotBacktester import BotBacketster


class BacktestCliException(Exception): pass


class BotBacktestCli:
    def __init__(self, manager: BotManager) -> None:
        self.manager: BotManager = manager

    def process_backtest(
        self,
        interface: Interfaces,
        selected_option: IndicatorOption
    ) -> None:

        if selected_option.step is None:
            raise BacktestCliException("Step must be not None")

        backtest_methods = BotBacketster(
            self.manager,
            interface,
            selected_option,
            selected_option.value,
            str(selected_option.step)
        )

        action = self._get_backtest_promt(selected_option, backtest_methods)

        res = action.execute()
        while res != "Select another parameter":
            res()
            selected_option = self.manager.update_option(selected_option)
            res = self._get_backtest_promt(
                selected_option, backtest_methods
            ).execute()

        backtest_methods.stop_backtesting()


    def _get_backtest_promt(
        self,
        option: IndicatorOption,
        backtest_methods: BotBacketster

    ) -> ListPrompt:

        actions = list([
            {
                "name": "backtest up",
                "value": backtest_methods.backtest_up
            },
            {
                "name": "backtest down",
                "value": backtest_methods.backtest_down
            },
            {
                "name": "backtest 10 steps up",
                "value": backtest_methods.backtest_steps_up
            },
            {
                "name": "backtest 10 steps down",
                "value": backtest_methods.backtest_steps_down
            },
            {
                "name": "backtesting length X 2",
                "value": backtest_methods.backtesting_length_x2
            },
            {
                "name": "backtesting length \\/ 2",
                "value": backtest_methods.backtesting_length_devide2
            },
        ])


        return inquirer.select(
            message="Backtesting !",
            choices=[
                Separator(
                    f"{option.title}: "
                    f"{option.value} |"
                    f" step: {self.manager.update_option(option).step} |"
                    f" ROI: {self.manager.bot_roi()}%"
                ),
                *actions,
                "Select another parameter"
            ],
        )

