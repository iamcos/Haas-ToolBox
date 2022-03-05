from cli.bots.BotCli import BotCli
from loguru import logger as log


class MadHatterCli(BotCli):
    def __init__(self) -> None:
        pass

    def menu(self) -> None:
        log.info("Starting working with MadHatterBot")
