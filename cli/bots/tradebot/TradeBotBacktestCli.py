from InquirerPy.prompts.list import ListPrompt
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from haasomeapi.dataobjects.custombots.dataobjects.IndicatorOption import IndicatorOption

from api.bots.trade.TradeBotManager import Interfaces, TradeBotException, TradeBotManager
from api.bots.trade.TradeBotIndicatorOptionMethods import TradeBotIndicatorOptionMethods



class TradeBotBacktestCli:

    def __init__(self, manager: TradeBotManager) -> None:
        self.manager: TradeBotManager = manager


    def process_backtest(
        self,
        interface: Interfaces,
        selected_option: IndicatorOption
    ) -> None:

        if selected_option.step is None:
            raise TradeBotException("Step must be not None")

        backtest_methods = TradeBotIndicatorOptionMethods(
            self.manager,
            interface,
            selected_option,
            selected_option.value,
            selected_option.step
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
        raise NotImplementedError("No instructions for selecting another parameter")


    def _get_backtest_promt(
        self,
        option: IndicatorOption,
        backtest_methods: TradeBotIndicatorOptionMethods

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
                # Separator(f"Press right to backtest up"),
                # Separator(f"Press left to backtest down"),
                # Separator(f"Press ',' to backtest 10 steps down"),
                # Separator(f"Press '.' to backtest 10 steps up"),
                # Separator(f"Press '=' - backtesting length X 2"),
                # Separator(f"Press '-' - backtesting length \\/ 2")
            ],
        )

    # def _action_methods(
    #     self,
    #     backtest_methods: TradeBotIndicatorOptionMethods,
    #     selected_option: IndicatorOption
    # ) -> ListPrompt:
    #     # action = self._get_backtest_promt(selected_option)

    #     @action.register_kb("right")
    #     def _(_):
    #         backtest_methods.backtest_up()

    #     @action.register_kb("left")
    #     def _(_):
    #         backtest_methods.backtest_down()

    #     @action.register_kb("escape")
    #     def _(_):
    #         pass

    #     @action.register_kb("=")
    #     def _(_):
    #         backtest_methods.backtesting_length_x2()

    #     @action.register_kb("-")
    #     def _(_):
    #         backtest_methods.backtesting_length_devide2()

    #     @action.register_kb(",")
    #     def _(_):
    #         backtest_methods.backtest_10_steps_down()

    #     @action.register_kb(".")
    #     def _(_):
    #         backtest_methods.backtest_10_steps_up()

    #     return action

