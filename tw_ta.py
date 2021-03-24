from PySimpleGUI.PySimpleGUI import No
from tradingview_ta import TA_Handler, Interval, Exchange
from haas import Haas
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from ratelimit import limits,sleep_and_retry
from haasomeapi.enums.EnumOrderType import EnumOrderType
from haasomeapi.enums.EnumOrderBotTriggerType import EnumOrderBotTriggerType
from InquirerPy import inquirer
class TW_TA(Haas):

	def init(self,bot,tw_time_interval):

		self.Haas.__init(self)
		self.bot = None,
		self.symbol = None
		self.interval = None,
		self.refresh_rate = None
		self.rating = None,
		self.prev_trade = None,
		self.trade_amount = 10,
		self.rating_level = "Strong",
  



	def interval_to_seconds(self,interval):

		"""Turns interval into minutes

		Args:
				interval (string): Time Interval (ex: 1m, 5m, 15m, 1h, 4h, 1d, 1W, 1M)

		Returns:
				string: JSON object as a string.
		"""
	
		if interval == "1m":
				# 1 Minute
				data_interval = 1
		elif interval == "5m":
				# 5 Minutes
				data_interval = 5
		elif interval == "15m":
				# 15 Minutes
				data_interval = 15
		elif interval == "1h":
				# 1 Hour
				data_interval = 60
		elif interval == "4h":
				# 4 Hour
				data_interval = 240
		elif interval == "1d":
				# 4 Hour
				data_interval = 60*24
		elif interval == "1W":
				# 1 Week
				data_interval = 60*24*7
		elif interval == "1M":
				# 1 Month
				data_interval = 60*24*7*30
		
		return data_interval
 
	 
	
	def interval_check(self):
		
		print('Available TradingView time intervals:')
	
		# resp = input('1m,5m,15m, 1h,4h,1d,1w,1m:')
		self.interval = inquirer.select(message = 'Select time interval: ',choices = ['1m', '5m', '15m', '1h', '4h', '1d', '1W', '1M']).execute()
		self.refresh_rate = self.interval_to_seconds(self.interval)
		
		print("Interval haas ben set to", self.interval, 'Refresh rate to', self.refresh_rate)
		
	def amount_check(self):
 
			resp = input('Order size: ')
			self.trade_amount = float(resp)   
	
	def setup(self):
		self.bot_selector(4)
		self.bot = self.bots[0]
		self.interval_check()
		self.amount_check()
		self.symbol = f"{self.bot.priceMarket.primaryCurrency}{self.bot.priceMarket.secondaryCurrency}"
		self.exchange = f"{EnumPriceSource(self.bot.priceMarket.priceSource).name}"

	def setup_external(self):
  		self.bot_selector(4)
			self.bot = self.bots[0]
			self.amount_check()

	@sleep_and_retry
	@limits(calls=1,period=60)
	def monitor_ta_rating(self):
		""" Returns Tradingview rating for selected symbol over selected exchange in defined time interval
		"""
	
		handler = TA_Handler(		
			symbol=self.symbol,
			exchange=self.exchange,
			screener='crypto',
			interval=self.interval)
	
		analysis = handler.get_analysis() 
		summary = analysis.summary #quick analysis summary
		self.rating = summary['RECOMMENDATION'] # "Strong Buy/Sell retrival"
		if self.rating_level == 'Strong':
			if self.rating == "Strong_buy":
				self.rating = 'Buy',
				self.ratingnum = 1
			elif self.rating == "Strong_sell":
				self.rating = 'Sell',
				self.ratingnum = 0
		elif self.rating_level == 'Normal':
			if self.rating == "BUY" or 'Buy':
				self.rating = "Buy"
				self.ratingnum = 1
			elif self.rating == "Sell" or 'SELL':
				self.ratingnum = 0
				self.rating = "Sell"
			print(self.rating,self.ratingnum,self.rating_level)
	
	
	def rating_monitoring(self):
		while True:
			self.monitor_ta_rating()
			self.CL()
	
	def get_current_price(self):
		current_price = self.c.marketDataApi.get_price_ticker(EnumPriceSource(self.bot.priceMarket.priceSource).value,self.bot.priceMarket.primaryCurrency,self.bot.priceMarket.secondaryCurrency,self.bot.priceMarket.contractName).result.currentBuyValue
		print(current_price)
		self.current_price = current_price
		
	
	def add_order(self):
		trade_result = self.c.customBotApi.add_order_bot_order(self.bot.guid,dependson='',dependsonnotexecuted="",amount=float(self.trade_amount),price=float(self.current_price),direction= self.ratingnum,templateguid='LOCKEDNOTIMEOUTGUID',triggertype=2, triggerprice=float(self.current_price))
		self.bot = trade_result.result

			
	def CL(self):
		preorders = self.bot.preOrders
		if len(preorders)>0:
			print(preorders[0]['OrderTypeAsString'],preorders[-1]['OrderTypeAsString'],self.rating.capitalize())
			if preorders[-1]['OrderTypeAsString'] != self.rating.capitalize():
				self.add_order()
				preorders = self.bot.preOrders
		else:
			self.add_order()
	
def main_tw():
	twta = TW_TA()
	twta.setup()
	twta.rating_level = "Normal"
	twta.monitor_ta_rating()
	print(twta.bot.__dict__)
	twta.get_current_price()
	twta.rating_monitoring()

def main_external():
  	
if __name__ == '__main__':
	
