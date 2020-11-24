from numpy import arange
from haas import Haas
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
import inquirer
import time
import pandas as pd

class FlashCrashBot(Haas):
		def __init__(self):
				Haas.__init__(self)
				self.ticks = Haas().read_ticks()
				# self.current_menu = None
				self.bot = None
				self.pricespread = [0.9,1.5,0.3]
				self.percentageboost = [0.1,0.5,0.1]
				self.multiplyer = [0.5,1.5,0.3]
				self.multiplyer_min = [0.5,1.5,0.3]
				self.multiplyer_max = [2,3,0.2]
		
		def bt(self):
				bt_results = []
				
				bt = self.c.customBotApi.backtest_custom_bot_on_market(self.bot.accountId,
				                                                       self.bot.guid,
				                                                       self.ticks,
				                                                       self.bot.priceMarket.primaryCurrency,
				                                                       self.bot.priceMarket.secondaryCurrency,
				                                                       self.bot.priceMarket.contractName,
				                                                       )
				print('bt',bt.errorCode,bt.errorMessage,bt.result.roi,' % ','Orders: ',
				      len(bt.result.completedOrders))
				if bt.errorCode.value == 1021:
						for i in range(5):
								time.sleep(5)
								bt = self.c.customBotApi.backtest_custom_bot(bot.guid,int(self.ticks))
								print('bt_loop',bt.errorCode,bt.errorMessage)
				
				bt_results.append([bt.result.roi,len(bt.result.completedOrders)])
				
				return bt_results
		
		def setup_fcb(self,bot):
				
				accountguid = bot.accountId
				botguid = bot.guid
				botname = bot.name
				primarycoin = bot.priceMarket.primaryCurrency
				secondarycoin = bot.priceMarket.secondaryCurrency
				fee = bot.currentFeePercentage
				baseprice = self.c.marketDataApi.get_price_ticker(bot.priceMarket.priceSource,bot.priceMarket.primaryCurrency,
				                                                  bot.priceMarket.secondaryCurrency,
				                                                  # bot.priceMarket.contractName)
				                                                  bot.priceMarket.contractName).result.currentBuyValue
				
				# print(baseprice.__dict__)
				pricespread = bot.priceSpread
				priceSpreadType = EnumFlashSpreadOptions(bot.priceSpreadType).value
				buyamount = bot.totalBuyAmount
				sellamount = bot.totalSellAmount
				amountspread = bot.amountSpread
				refilldelay = bot.refillDelay
				percentageboost = bot.percentageBoost
				minpercentage = bot.minPercentage
				maxpercentage = bot.maxPercentage
				safetyenabled = bot.safetyEnabled
				safetytriggerlevel = bot.safetyTriggerLevel
				safetymovein = bot.safetyMoveInMarket
				safetymoveout = bot.safetyMoveOutMarket
				followthetrend = bot.followTheTrend
				followthetrendchannelrange = bot.followTheTrendChannelRange
				followthetrendchanneloffset = bot.followTheTrendChannelOffset
				followthetrendtimeout = bot.followTheTrendTimeout
				
				amounttype = bot.amountType
				
				def setup_fcb(accountguid=accountguid,botguid=botguid,botname=botname,primarycoin=primarycoin,
				              secondarycoin=secondarycoin,fee=fee,baseprice=baseprice,priceSpreadType=priceSpreadType,
				              pricespread=pricespread,amountspread=amountspread,amounttype=amounttype,buyamount=buyamount,
				              sellamount=sellamount,refilldelay=refilldelay,safetyenabled=safetyenabled,
				              safetytriggerlevel=safetytriggerlevel,safetymovein=safetymovein,safetymoveout=safetymoveout,
				              followthetrend=followthetrend,followthetrendchannelrange=followthetrendchannelrange,
				              followthetrendchanneloffset=followthetrendchanneloffset,
				              followthetrendtimeout=followthetrendtimeout,percentageboost=percentageboost,
				              minpercentage=minpercentage,maxpercentage=maxpercentage,):
						do = self.c.customBotApi.setup_flash_crash_bot(
								accountguid=accountguid,
								botguid=botguid,
								botname=botname,
								primarycoin=primarycoin,
								secondarycoin=secondarycoin,
								fee=fee,
								baseprice=baseprice,
								priceSpreadType=priceSpreadType,
								pricespread=pricespread,
								amountspread=amountspread,
								amounttype=amounttype,
								buyamount=buyamount,
								sellamount=sellamount,
								refilldelay=refilldelay,
								safetyenabled=safetyenabled,
								safetytriggerlevel=safetytriggerlevel,
								safetymovein=safetymovein,
								safetymoveout=safetymoveout,
								followthetrend=followthetrend,
								followthetrendchannelrange=followthetrendchannelrange,
								followthetrendchanneloffset=followthetrendchanneloffset,
								followthetrendtimeout=followthetrendtimeout,
								percentageboost=percentageboost,
								minpercentage=minpercentage,
								maxpercentage=maxpercentage,
								)
						print('result: ',do.errorCode,do.errorMessage)
						return do.result
				
				if bot.priceSpreadType == 0 or 1:
						if self.pricespread:
								for p in arange(float(self.pricespread[0]),float(self.pricespread[1]),float(self.pricespread[2])):
										print('p',p)
										fcb_setup = setup_fcb(pricespread=p)
										bt_results = self.bt()
				if bot.priceSpreadType == 2:
						for p in arange(float(self.pricespread[0]),float(self.pricespread[1]),float(self.pricespread[2])):
								for b in arange(float(self.percentageboost[0]),float(self.percentageboost[1]),
								                float(self.percentageboost[2])):
										resp = setup_fcb(pricespread=p,percentageboost=b)
										bt_results = self.bt()
				
				if bot.priceSpreadType == 3:
						for min in arange(float(self.multiplyer_min[0]),float(self.multiplyer_min[1]),
						                  float(self.multiplyer_min[2])):
								for max in arange(float(self.multiplyer_max[0]),float(self.multiplyer_max[1]),
								                  float(self.multiplyer_max[2])):
										fcb_setup = setup_fcb(minpercentage=min,maxpercentage=max)
										bt_results = self.bt()
				
				df = pd.DataFrame(bt_results)
				print(df)
				return
		
		def set_price_spread_range(self):
				
				choices = [
						inquirer.Text('start','Enter Spread Start range: '),
						inquirer.Text('end','Enter Spread End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.pricespread = [answers['start'],answers['end'],answers['step']]
		
		def set_percentage_range(self):
				
				choices = [
						inquirer.Text('start','Enter percentage Start range: '),
						inquirer.Text('end','Enter percentage End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.percentageboost = [answers['start'],answers['end'],answers['step']]
				print(self.percentageboost,self.bot)
		
		def set_multiplier_range(self):
				
				choices = [
						inquirer.Text('start','Enter multiplyer Start range: '),
						inquirer.Text('end','Enter multiplyer End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer,self.bot)
		
		def set_min_range(self):
				
				choices = [
						inquirer.Text('start','Enter min % Start range: '),
						inquirer.Text('end','Enter min % End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer_min = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer_min,self.bot)
		
		def set_max_range(self):
				
				choices = [
						inquirer.Text('start','Enter max % Start range: '),
						inquirer.Text('end','Enter max % End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer_max = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer_max,self.bot)
		
		def fcb_menu(self):
				while True:
						menu_items = []
						
						if self.bot == None:
								
								print(self.bot,'BOT')
								menu_items = ['Select Bot','Quit']
								menu = [inquirer.List('resp','FlashCrash Tools',menu_items)]
								resp = inquirer.prompt(menu)['resp']
						
						
						elif self.bot.botType == 6:
								menu_items = ['Select another bot']
								
								if self.bot.priceSpreadType == 0 or self.bot.priceSpreadType == 1:
										menu_items.append('Set price spread range')
								if self.bot.priceSpreadType == 2:
										menu_items.append('Set price spread range')
										menu_items.append('Set percentage range')
								if self.bot.priceSpreadType == 3:
										menu_items.append('Set multiplyer range')
										menu_items.append('Set mib %')
										menu_items.append('Set max %')
								
								menu_items.append('Set BT date')
								menu_items.append('Backtest')
								menu_items.append('Quit')
								menu = [inquirer.List('resp','Do stuff',menu_items)]
								
								resp = inquirer.prompt(menu)['resp']
						
						if resp == 'Set price spread range':
								self.set_price_spread_range()
						
						if resp == "Set percentage range":
								self.set_percentage_range()
						
						if resp == "Set multiplyer range":
								self.set_multiplier_range()
						if resp == "Set mib %":
								self.set_min_range()
						if resp == "Set max %":
								self.set_max_range()
						
						if resp == "Set BT date":
								self.write_date()
						if resp == "Backtest":
								self.setup_fcb(self.bot)
						if resp == 'Quit':
								break
								# pass
						if resp == 'Select Bot' or 'Select another bot':
								self.bot_selector(6)
								print('self.bot',self.bot)
								self.fcb_menu()
						
						return resp


def test():
		h = FlashCrashBot()
		# print(h.__dict__)
		h.fcb_menu()


if __name__ == '__main__':
		test()
