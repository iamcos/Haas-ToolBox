from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from api.loader import main_context
from cli.bots.BotCli import BotCli
from cli.bots.scalper.ScalperRangeBacktesterCli import ScalperRangeBacktesterCli


class ScalperCli(BotCli):
    def __init__(self) -> None:
        super().__init__(ScalperBot)

        config_manager = main_context.config_manager

        def sclaper_range_backtesting_cli():
            return ScalperRangeBacktesterCli(
                    self.bot_guid, self.provider, config_manager).start()

        self.add_menu_action(
            "Backtesting in range",
            tuple([sclaper_range_backtesting_cli])
        )

