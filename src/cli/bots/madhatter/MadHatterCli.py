from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from cli.bots.BotConfigBacktestCli import BotConfigBacktestCli
from cli.bots.BotCli import BotCli
from api.loader import main_context


class MadHatterCli(BotCli):
    def __init__(self) -> None:
        super().__init__(MadHatterBot)

        def config_backtest() -> None:
            return BotConfigBacktestCli(
                self.bot_guid,
                self.provider,
                main_context.config_manager
            ).start()

        self.add_menu_action(
            "Start backtesting by config",
            tuple([config_backtest])
        )

