

class TA:
	
	def __init__(self):
		md = md()
		bot = self.return_botlist[0]
		md.get_market_data(
			self.bot.priceMarket,self.bot.interval,int(self.read_ticks() / self.bot.interval)
			)
