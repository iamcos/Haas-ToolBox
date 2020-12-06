from haas import Haas
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient
from marketdata import MarketData
from haasomeapi.enums.EnumErrorCode import EnumErrorCode


class SignalHandler(Haas):
		def __init__(self):
				Haas.__init__(self)
				self.c = HaasomeClient(self.ip,self.secret)
				self.marketdata = None
				self.exchange = None
				self.ticker = None
				self.primarycoin = None
				self.secondarycoin = None
		
		def identify_exchange(self,exchange):
		
		