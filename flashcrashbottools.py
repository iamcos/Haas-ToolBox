import datetime
import time

import inquirer
import pandas as pd
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from numpy import arange

from haas import Haas


class FlashCrashBot(Haas):
		def __init__(self):
				Haas.__init__(self)
				self.ticks = Haas().read_ticks()
				# self.current_menu = None
				self.bot = None
				self.pricespread = None
				self.percentageboost = None
				self.multiplyer = None
				self.multiplyer_min = None
				self.multiplyer_max = None
		
		
		def read_limits(self):
				for i in ['pricespread','percentageboost','multiplyer','multiplyer_min','multiplyer_max']:
						self
		def bt(self):

				bt = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.ticks)
				
				orders_df = self.trades_to_df(bt.result)
				
				if len(orders_df.index) > 0:
						filled_orders = orders_df[orders_df.orderStatus == 5]
						print(f'ROI: {bt.result.roi}, Total Gain: {bt.result.totalProfits}, '
						      f'Completed Orders: {len(bt.result.completedOrders)}, '
						      )
				
				if bt.errorCode.value == 1021:
						for i in range(5):
								time.sleep(5)
								bt = self.c.customBotApi.backtest_custom_bot(self.bot.guid,int(self.ticks))
				
				return bt.result
		
		def read_limits(self):
				try:
						self.pricespread = [self.config['FCB_LIMITS'].get('pricespread_start'),self.config['FCB_LIMITS'].get(
								'pricespread_end'),self.config['FCB_LIMITS'].get('pricespread_step')]
				except Exception as e:
						print(e)
				
				try:
						self.percentageboost = [self.config['FCB_LIMITS'].get('percentageboost_start'),self.config['FCB_LIMITS'].get(
								'percentageboost_end'),self.config['FCB_LIMITS'].get('percentageboost_step')]
				except Exception as e:
						print(e)
				try:
						self.multiplyer = [self.config['FCB_LIMITS'].get('multiplyer_start'),self.config['FCB_LIMITS'].get(
								'multiplyer_end'),self.config['FCB_LIMITS'].get('multiplyer_step')]
				except Exception as e:
						print(e)
				try:
						self.multiplyer_min = [self.config['FCB_LIMITS'].get('multiplyer_min_start'),self.config['FCB_LIMITS'].get(
								'multiplyer_min_end'),self.config['FCB_LIMITS'].get('multiplyer_min_step')]
				except Exception as e:
						print(e)
				try:
						self.multiplyer_max = [self.config['FCB_LIMITS'].get('multiplyer_max_start'),self.config['FCB_LIMITS'].get(
								'multiplyer_max_end'),self.config['FCB_LIMITS'].get('multiplyer_max_step')]
				except Exception as e:
						print(e)
		
		def setup_fcb(self,print_errors=False):
				
				accountguid = self.bot.accountId
				botguid = self.bot.guid
				botname = self.bot.name
				primarycoin = self.bot.priceMarket.primaryCurrency
				secondarycoin = self.bot.priceMarket.secondaryCurrency
				fee = self.bot.currentFeePercentage
				baseprice = self.c.marketDataApi.get_price_ticker(self.bot.priceMarket.priceSource,
				                                                  self.bot.priceMarket.primaryCurrency,
				                                                  self.bot.priceMarket.secondaryCurrency,
				                                                  # self.bot.priceMarket.contractName)
				                                                  self.bot.priceMarket.contractName).result.currentBuyValue
				
				# print(baseprice.__dict__)
				pricespread = self.bot.priceSpread
				priceSpreadType = EnumFlashSpreadOptions(self.bot.priceSpreadType).value
				buyamount = self.bot.totalBuyAmount
				sellamount = self.bot.totalSellAmount
				amountspread = self.bot.amountSpread
				# refilldelay = self.bot.refillDelay
				refilldelay = 0
				percentageboost = self.bot.percentageBoost
				minpercentage = self.bot.minPercentage
				maxpercentage = self.bot.maxPercentage
				safetyenabled = self.bot.safetyEnabled
				safetytriggerlevel = self.bot.safetyTriggerLevel
				safetymovein = self.bot.safetyMoveInMarket
				safetymoveout = self.bot.safetyMoveOutMarket
				followthetrend = self.bot.followTheTrend
				followthetrendchannelrange = self.bot.followTheTrendChannelRange
				followthetrendchanneloffset = self.bot.followTheTrendChannelOffset
				followthetrendtimeout = self.bot.followTheTrendTimeout
				
				amounttype = self.bot.amountType
				
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
					
						# print('result: ',do.errorCode,do.errorMessage)
						return do.result
				bt_results = []
				if self.bot.priceSpreadType <= 1:
						if self.pricespread:
								for p in arange(float(self.pricespread[0]),float(self.pricespread[1]),float(self.pricespread[2])):
										# print('p',p)
										fcb_setup = setup_fcb(pricespread=round(p,2))
										bt_results.append([self.bt().roi,self.bt().totalProfits,len(self.bt(
												
												).completedOrders),round(p,
										                                                                                               2)])
						df_results = pd.DataFrame(bt_results,columns=['roi','total Profits','Orders','pricespread',])
				if self.bot.priceSpreadType == 2:
						for p in arange(float(self.pricespread[0]),float(self.pricespread[1]),float(self.pricespread[2])):
								for b in arange(float(self.percentageboost[0]),float(self.percentageboost[1]),
								                float(self.percentageboost[2])):
										resp = setup_fcb(pricespread=round(p,2),percentageboost=round(b,2))
										bt_results.append([self.bt().roi,self.bt().totalProfits,len(self.bt(
												
												).completedOrders),round(p,
										                                                                                             2),round(b,2)])
						df_results = pd.DataFrame(bt_results,columns=['roi','total Profits','Orders','pricespread','percentageboost'])
				if self.bot.priceSpreadType == 3:
						for multiplyer in arange(float(self.multiplyer[0]),float(self.multiplyer[1]),float(self.multiplyer[2])):
								for min in arange(float(self.multiplyer_min[0]),float(self.multiplyer_min[1]),
								                  float(self.multiplyer_min[2])):
										for max in arange(float(self.multiplyer_max[0]),float(self.multiplyer_max[1]),
										                  float(self.multiplyer_max[2])):
												fcb_setup = setup_fcb(minpercentage=round(min,2),maxpercentage=round(max,2),
												                      percentageboost=round(multiplyer,2))
										
												bt_results.append([self.bt().roi,self.bt().totalProfits,
												                   len(self.bt().completedOrders),round(
														multiplyer,2),round(min,2),
												                   round(max,2)])
						df_results = pd.DataFrame(bt_results,columns=['roi','total Profits','Orders','multiplyer','min','max'])
				
	
				filename = f'FCB_{self.bot.name.replace("/","_")}_{datetime.date.today().month}-{datetime.date.today().day}' \
				           f'.csv'
				df_results.sort_values(by="total Profits",ascending=False,inplace=True)
				df_results.drop_duplicates()
				df_results.reset_index(inplace=True,drop=True)
				df_results.to_csv(filename)
				
				return df_results
		
		def slots_to_df(self,bot):

				open_slots = [
						{
								"price":bot.slots[x]['Price'],
								"amount":bot.slots[x]['Amount'],
								"orderType":bot.slots[x]['Type'],
								'active': bot.slots[x]['ActiveSlot'],
								}
						for x in bot.slots
						]
				# for x in self.bot.completed
				
				slots_df = pd.DataFrame(open_slots)
				return slots_df
		
		def set_price_spread_range(self):
				
				choices = [
						inquirer.Text('start','Enter Spread Start range: '),
						inquirer.Text('end','Enter Spread End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.pricespread = [answers['start'],answers['end'],answers['step']]
				try:
						self.config.add_section("FCB_LIMITS")
				except Exception as e:
						print(e)
				self.config.set('FCB_LIMITS','pricespread_start',self.pricespread[0])
				self.config.set('FCB_LIMITS','pricespread_end',self.pricespread[1])
				self.config.set('FCB_LIMITS','pricespread_step',self.pricespread[2])
				self.write_file()
		def set_percentage_range(self):
				
				choices = [
						inquirer.Text('start','Enter percentage Start range: '),
						inquirer.Text('end','Enter percentage End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.percentageboost = [answers['start'],answers['end'],answers['step']]
				print(self.percentageboost,self.bot)
		
				try:
						self.config.add_section("FCB_LIMITS")
				except Exception as e:
						print(e)
				self.config.set('FCB_LIMITS','percentageboost_start',self.percentageboost[0])
				self.config.set('FCB_LIMITS','percentageboost_end',self.percentageboost[1])
				self.config.set('FCB_LIMITS','percentageboost_step',self.percentageboost[2])
				self.write_file()
		def set_multiplier_range(self):
				
				choices = [
						inquirer.Text('start','Enter multiplyer Start range: '),
						inquirer.Text('end','Enter multiplyer End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer,self.bot)
		
				try:
						self.config.add_section("FCB_LIMITS")
				except Exception as e:
						print(e)
				self.config.set('FCB_LIMITS','multiplyer_start',self.multiplyer[0])
				self.config.set('FCB_LIMITS','multiplyer_end',self.multiplyer[1])
				self.config.set('FCB_LIMITS','multiplyer_step',self.multiplyer[2])
				self.write_file()
				
		def set_min_range(self):
				
				choices = [
						inquirer.Text('start','Enter min % Start range: '),
						inquirer.Text('end','Enter min % End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer_min = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer_min,self.bot)
		
				try:
						self.config.add_section("FCB_LIMITS")
				except Exception as e:
						print(e)
				self.config.set('FCB_LIMITS','multiplyer_min_start',self.multiplyer_min[0])
				self.config.set('FCB_LIMITS','multiplyer_min_end',self.multiplyer_min[1])
				self.config.set('FCB_LIMITS','multiplyer_min_step',self.multiplyer_min[2])
				self.write_file()
				
		def set_max_range(self):
				
				choices = [
						inquirer.Text('start','Enter max % Start range: '),
						inquirer.Text('end','Enter max % End range:'),
						inquirer.Text('step','Enter Step: ')]
				
				answers = inquirer.prompt(choices)
				self.multiplyer_max = [answers['start'],answers['end'],answers['step']]
				print(self.multiplyer_max,self.bot)
		
				try:
						self.config.add_section("FCB_LIMITS")
				except Exception as e:
						print(e)
				self.config.set('FCB_LIMITS','multiplyer_max_start',self.multiplyer_max[0])
				self.config.set('FCB_LIMITS','multiplyer_max_end',self.multiplyer_max[1])
				self.config.set('FCB_LIMITS','multiplyer_max_step',self.multiplyer_max[2])
				self.write_file()
		def fcb_menu(self):
				self.read_limits()
				
				while True:
						menu_items = []
						
						if self.bot is None:
								
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
