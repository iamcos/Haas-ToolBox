from numpy.ma import arange
from haas import Haas
from marketdata import MarketData as md
import pandas as pd
import pandas_ta as ta
import talib
from talib import MA_Type


class TA:
	
		md = md()
		bot = self.return_botlist[0]
		md.get_market_data(
		self.bot.priceMarket,interval,int(self.read_ticks() / interval)
		)