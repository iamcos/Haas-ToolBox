from haasomeapi.dataobjects.custombots.MadHatterBot import MadHatterBot
from cli.bots.BotCli import BotCli


class MadHatterCli(BotCli):
    def __init__(self) -> None:
        super().__init__(MadHatterBot)

