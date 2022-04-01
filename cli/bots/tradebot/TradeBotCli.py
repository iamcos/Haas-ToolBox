from haasomeapi.dataobjects.tradebot.TradeBot import TradeBot
from cli.bots.BotCli import BotCli


class TradeBotCli(BotCli):
    def __init__(self) -> None:
        super().__init__(TradeBot)

