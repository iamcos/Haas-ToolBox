from haasomeapi.dataobjects.custombots.ScalperBot import ScalperBot
from cli.bots.BotCli import BotCli


class SclaperCli(BotCli):
    def __init__(self) -> None:
        super().__init__(ScalperBot)

