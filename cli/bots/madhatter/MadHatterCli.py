from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from cli.bots.BotConfigBacktestCli import BotConfigBacktestCli
from cli.bots.BotCli import BotCli


class MadHatterCli(BotCli):
    def __init__(self) -> None:
        super().__init__(MadHatterBot)

        self.add_menu_action(
            "Start backtesting by config",
            tuple([BotConfigBacktestCli(self.manager).start])
        )
    
