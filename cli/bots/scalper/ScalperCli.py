from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from cli.bots.BotCli import BotCli
from cli.bots.scalper.ScalperRangeBacktesterCli import ScalperRangeBacktesterCli


class ScalperCli(BotCli):
    def __init__(self) -> None:
        super().__init__(ScalperBot)

        self.add_menu_action(
            "Backtesting in range",
            tuple([ScalperRangeBacktesterCli(self.manager).start])
        )

