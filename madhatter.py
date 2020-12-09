import datetime
import json

import inquirer
import pandas as pd
from alive_progress import alive_bar
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.HaasomeClient import HaasomeClient
from inquirer.themes import GreenPassion
from ratelimit import limits,sleep_and_retry

from haas import Haas
from optimisation import Optimize
from marketdata import MarketData

class MadHatterBot(Haas,Optimize):
		def __init__(self):
				Haas.__init__(self)
				self.c = HaasomeClient(self.ip,self.secret)
				self.ticks = self.read_ticks()
				self.stoploss_range = None
				self.num_configs = None
				self.limit = None
				self.config_storage = dict()
				self.configs = None
				self.current_config = None
				self.extended_range = None
				self.ranges = self.set_ranges()
				self.intervals_list = [1,2,3,4,5,6,10,12,15,20,30,45,60,90,120,150,180,240,300,600,1200,2400,]
				self.columns = ["interval","signalconsensus","fcc","resetmiddle","allowmidsells","matype","rsil","rsib","rsis","bbl","devup","devdn","macdfast","macdslow","macdsign",]
				self.possible_profit = None
		

		def create_mh(self,input_bot,name):
				new_mad_hatter_bot = self.c.customBotApi.new_mad_hatter_bot_custom_bot(
						input_bot.accountId,
						input_bot.botType,
						name,
						input_bot.priceMarket.primaryCurrency,
						input_bot.priceMarket.secondaryCurrency,
						input_bot.priceMarket.contractName,
						)
				# print(new_mad_hatter_bot.errorCode, new_mad_hatter_bot.errorMessage)
				# print(new_mad_hatter_bot.result)
				return new_mad_hatter_bot.result
		
		@sleep_and_retry
		@limits(calls=3,period=2)
		def return_botlist(self):
				bl = self.c.customBotApi.get_all_custom_bots()
				# print(bl.errorMessage)
				botlist = [x for x in bl.result if x.botType == 15]
				# print(botlist)
				return botlist
		
		def bot_config(self,bot):
				botdict = {
						"roi":float(bot.roi),
						"interval":int(bot.interval),
						"signalconsensus":bool(bot.useTwoSignals),
						"resetmiddle":bool(bot.bBands["ResetMid"]),
						"allowmidsells":bool(bot.bBands["AllowMidSell"]),
						"matype":bot.bBands["MaType"],
						"fcc":bool(bot.bBands["RequireFcc"]),
						"rsil":str(bot.rsi["RsiLength"]),
						"rsib":str(bot.rsi["RsiOversold"]),
						"rsis":str(bot.rsi["RsiOverbought"]),
						"bbl":str(bot.bBands["Length"]),
						"devup":str(bot.bBands["Devup"]),
						"devdn":str(bot.bBands["Devdn"]),
						"macdfast":str(bot.macd["MacdFast"]),
						"macdslow":str(bot.macd["MacdSlow"]),
						"macdsign":str(bot.macd["MacdSign"]),
						"trades":int(len(bot.completedOrders)),
						"obj":bot
						}
				# "pricesource": EnumPriceSource(bot.priceMarket.priceSource).name,
				# "primarycoin": bot.priceMarket.primaryCurrency,
				# "secondarycoin": bot.priceMarket.secondaryCurrency,
				df = pd.DataFrame.from_dict([botdict])
				
				return df
		
		def set_ranges(self):
				class UtilClass():
						pass
				
				ranges = UtilClass()
				ranges.bot = UtilClass()
				ranges.indicators = UtilClass()
				ranges.safeties = UtilClass()
				
				interval = [
						1,
						2,
						3,
						4,
						5,
						6,
						10,
						12,
						15,
						20,
						30,
						45,
						60,
						90,
						120,
						150,
						180,
						240,
						300,
						600,
						1200,
						2400,
						]
				
				signalconsensus = allowmidsells = resetmiddle = requirefcc = True,False
				
				stoploss = 0.5,5.0,0.1
				intervals = UtilClass()
				intervals.list = interval
				
				ranges.bot.intervals = intervals
				ranges.bot.signalconsensus = signalconsensus
				
				bBands = UtilClass()
				bBands.matype = 0,9,1
				bBands.length = 7,9,1
				bBands.devup = 1.0,1.2,0.1
				bBands.devdown = 1.0,1.2,0.1
				
				rsi = UtilClass()
				rsi.length = 2,21,1
				rsi.buy = 51,99,1
				rsi.sell = 2,49,1
				
				macd = UtilClass()
				macd.fast = 2,59,1
				macd.slow = 40,80,1
				macd.signal = 3,21,1
				
				ranges.indicators.bBands = bBands
				ranges.indicators.rsi = rsi
				ranges.indicators.macd = macd
				ranges.safeties.stoploss = stoploss
				
				self.ranges = ranges
				
				# ranges = jsonpickle.encode(ranges,unpicklable=False)
				return ranges
		
		def setup_bot_from_csv(self,bot,config,print_errors=False):
		
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(  # this way less api calls is being made
								bot.guid,EnumMadHatterIndicators.BBANDS,0,int(config["bbl"])
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								1,
								config["devup"],
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								2,
								config["devdn"],
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								3,
								config["matype"],
								)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								5,
								bool(config["fcc"]),
								)
						if print_errors == True:
								print('bBands FCC',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								6,
								bool(config["resetmiddle"]),
								)
						if print_errors == True:
								# print('bot.bBands["ResetMid"]','type: ',type(bot.bBands["ResetMid"]),bot.bBands["ResetMid"], \
								#       'bool(config["fcc"]: ',bool(config["resetmiddle"]))
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								7,
								bool(config["allowmidsells"]),
								)
						if print_errors == True:
								# print('bot.bBands["AllowMidSell"]','type: ',type(bot.bBands["AllowMidSell"]),bot.bBands[
								# 		"AllowMidSell"],'bool(config['
								#                     '"resetmiddle"]: ',bool(config[
								# 		                                            "resetmiddle"]))
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								0,
								config["rsil"],
								)
						if print_errors == True:
								print('bool(config["fcc"]: ',bool(config["fcc"]))
								print('bBands',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								1,
								config["rsib"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,EnumMadHatterIndicators.RSI,2,config["rsis"]
								)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								0,
								config["macdfast"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								1,
								config["macdslow"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								2,
								config["macdsign"],
								)
						if print_errors == True:
								print('macd',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
								botName=bot.name,
								botGuid=bot.guid,
								accountGuid=bot.accountId,
								primaryCoin=bot.priceMarket.primaryCurrency,
								secondaryCoin=bot.priceMarket.secondaryCurrency,
								contractName=bot.priceMarket.contractName,
								leverage=bot.leverage,
								templateGuid=bot.customTemplate,
								position=bot.coinPosition,
								fee=bot.currentFeePercentage,
								tradeAmountType=bot.amountType,
								tradeAmount=bot.currentTradeAmount,
								useconsensus=bot.useTwoSignals,
								disableAfterStopLoss=bot.disableAfterStopLoss,
								interval=config.interval,
								includeIncompleteInterval=bot.includeIncompleteInterval,
								mappedBuySignal=bot.mappedBuySignal,
								mappedSellSignal=bot.mappedSellSignal,
								)
						if print_errors == True:
								print('macd',do.errorCode,do.errorMessage)
						
						do = self.c.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
								botName=bot.name,
								botGuid=bot.guid,
								accountGuid=bot.accountId,
								primaryCoin=bot.priceMarket.primaryCurrency,
								secondaryCoin=bot.priceMarket.secondaryCurrency,
								contractName=bot.priceMarket.contractName,
								leverage=bot.leverage,
								templateGuid=bot.customTemplate,
								position=bot.coinPosition,
								fee=bot.currentFeePercentage,
								tradeAmountType=bot.amountType,
								tradeAmount=bot.currentTradeAmount,
								useconsensus=bot.useTwoSignals,
								disableAfterStopLoss=bot.disableAfterStopLoss,
								interval=config.interval,
								includeIncompleteInterval=bot.includeIncompleteInterval,
								mappedBuySignal=bot.mappedBuySignal,
								mappedSellSignal=bot.mappedSellSignal,
								)
						if print_errors == True:
								print('macd',do.errorCode,do.errorMessage)
						print('MH FROM CSV',do.errorCode,do.errorMessage)
						updated_bot = do
						try:
								print('updated_bot',updated_bot.errorCode,updated_bot.errorMessage)
						except Exception as e:
								print(e)
						
						return do

		
		# print(bot.name, ' Has been configured')
		# Indicator parameters have been set
		# calling it setup_bot_from_obj. It checks each parameter against new config.
		# updated_bot = self.c.customBotApi.get_custom_bot(self.bot.guid,self.bot.botType)
		
		def setup_bot_from_obj(self,bot,config,print_errors=False):
				
				if bot.bBands["Length"] != config.bBands["Length"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,EnumMadHatterIndicators.BBANDS,0,config.bBands["Length"]
								)
				if print_errors == True:
						print('interval',do.errorCode,do.errorMessage)
				if bot.bBands["Devup"] != config.bBands["Devup"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								1,
								config.bBands["Devup"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.bBands["Devdn"] != config.bBands["Devdn"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								2,
								config.bBands["Devdn"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.bBands["MaType"] != config.bBands["MaType"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								3,
								config.bBands["MaType"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.bBands["AllowMidSell"] != config.bBands["AllowMidSell"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								5,
								config.bBands["AllowMidSell"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.bBands["RequireFcc"] != config.bBands["RequireFcc"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								6,
								config.bBands["fcc"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.rsi["RsiLength"] != config.rsi["RsiLength"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								0,
								config.rsi["RsiLength"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.rsi["RsiOverbought"] != config.rsi["RsiOverbought"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								1,
								config.rsi["RsiOverbought"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.rsi["RsiOversold"] != config.rsi["RsiOversold"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,EnumMadHatterIndicators.RSI,2,config.rsi["RsiOversold"]
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.macd["MacdFast"] != config.macd["MacdFast"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								0,
								config.macd["MacdFast"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.macd["MacdSlow"] != config.macd["MacdSlow"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								1,
								config.macd["MacdSlow"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.macd["MacdSign"] != config.macd["MacdSign"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								2,
								config.macd["MacdSign"],
								)
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.interval != config.interval:
						do = self.c.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
								botName=bot.name,
								botGuid=bot.guid,
								accountGuid=bot.accountId,
								primaryCoin=bot.priceMarket.primaryCurrency,
								secondaryCoin=bot.priceMarket.secondaryCurrency,
								contractName=bot.priceMarket.contractName,
								leverage=bot.leverage,
								templateGuid=bot.customTemplate,
								position=bot.coinPosition,
								fee=bot.currentFeePercentage,
								tradeAmountType=bot.amountType,
								tradeAmount=bot.currentTradeAmount,
								useconsensus=bot.useTwoSignals,
								disableAfterStopLoss=bot.disableAfterStopLoss,
								interval=config.interval,
								includeIncompleteInterval=bot.includeIncompleteInterval,
								mappedBuySignal=bot.mappedBuySignal,
								mappedSellSignal=bot.mappedSellSignal,
								).result
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
				if bot.useTwoSignals != config.useTwoSignals:
						do = self.c.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
								botName=bot.name,
								botGuid=bot.guid,
								accountGuid=bot.accountId,
								primaryCoin=bot.priceMarket.primaryCurrency,
								secondaryCoin=bot.priceMarket.secondaryCurrency,
								contractName=bot.priceMarket.contractName,
								leverage=bot.leverage,
								templateGuid=bot.customTemplate,
								position=bot.coinPosition,
								fee=bot.currentFeePercentage,
								tradeAmountType=bot.amountType,
								tradeAmount=bot.currentTradeAmount,
								useconsensus=bot.useTwoSignals,
								disableAfterStopLoss=bot.disableAfterStopLoss,
								interval=config.interval,
								includeIncompleteInterval=bot.includeIncompleteInterval,
								mappedBuySignal=bot.mappedBuySignal,
								mappedSellSignal=bot.mappedSellSignal,
								).result
				if print_errors == True:
						print(do.errorCode,do.errorMessage)
		
		def bt(self):
				
				if self.num_configs > len(self.configs.index):
						self.num_configs == len(self.configs.index)
						print(f'config limit bigger than configs in config file, setting it to {self.num_configs}')
				print('index',self.configs.index)
				print('the configs',self.configs)
				
				bt_results = self.iterate_csv(self.configs[0:self.num_configs],self.bot)
				obj_file_name = f'./bt_results/{self.bot.name.replace("/","_")}_{datetime.date.today().month}' \
				                f'_{datetime.date.today().day}.obj'
				objects = bt_results.obj
				objects.to_pickle(obj_file_name)
				to_csv = bt_results.drop("obj",axis=1)
				
				filename = (
								str(self.bot.name.replace("/","_"))
								+ str("_")
								+ str(datetime.date.today().month)
								+ str("-")
								+ str(datetime.date.today().day)
								+ str("_")
								+ str(len(bt_results))
								+ str(".csv")
				)
				to_csv.sort_values(by="roi",ascending=False,inplace=True)
				to_csv.drop_duplicates()
				to_csv.reset_index(inplace=True,drop=True)
				to_csv.to_csv(filename)
				
				bt_results.sort_values(by="roi",ascending=False,inplace=True)
				bt_results.drop_duplicates()
				bt_results.reset_index(inplace=True,drop=True)
				self.store_results(bt_results)
		
		
		
		def setup_mh_bot(self):
				bot = self.bot
				configs = self.config_storage[bot.guid]
				if self.limit > len(configs.index):
						self.limit = len(configs.index)
				# print('set configs limit', self.limit)
				for c in range(self.limit):
						name = f"{bot.name} {c} {configs.roi.iloc[c]}%"
						self.setup_bot_from_csv(bot,configs.iloc[c],print_errors=False)
						self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
						self.c.customBotApi.clone_custom_bot_simple(bot.accountId,bot.guid,name)
		
		def iterate_csv(self,configs,bot):
				try:
						configs["obj"] = None
						best_roi = 0
						configs.roi[0:-1] = 0
						cols = ["interval","signalconsensus","fcc","resetmiddle","allowmidsells","matype","rsil","rsib","rsis","bbl","devup","devdn","macdfast","macdslow","macdsign","trades","roi","obj"]
						for c in configs.columns:
								if c not in cols:
										configs.drop(c,axis=1,inplace=True)
						try:
								bot.currentTradeAmount = 10000
						except Exception as e:
								print("Iterate CSV exception",e)
						with alive_bar(len(configs.index),title=f"{self.bot.name} backtesting. ") as bar:
								
								for i in configs.index:
										try:
												print(	f'Current Backtest ROI:  {bt.roi} % 	best ROI: {best_roi}%.')
												self.calculate_possible_roi()
												print(f'Market growth during BT period: {self.possible_profit}')
												
										
												print("\nTop 10 configs so far:\n")
												print(configs.sort_values(by="roi",ascending=False).drop('obj',axis=1)[0:10])
										except:
											pass
										config = configs.iloc[i]
										s = self.setup_bot_from_csv(bot,config)
										bt = self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
										bt = bt.result
										if bt.roi > best_roi:
												best_roi = bt.roi
										configs["roi"].iloc[i] = bt.roi
										try:
												configs['trades'].iloc[i] = len(bot.completedOrders)
										except:
												configs['trades'].iloc[i] = None
										configs["obj"].iloc[i] = bt
										self.bot = bt
										bar()
						
						return configs
				except (KeyboardInterrupt,SystemExit):
						filename = (
										str(b.name.replace("/","_"))
										+ str("_")
										+ str(datetime.date.today().month)
										+ str("-")
										+ str(datetime.date.today().day)
										+ str("_")
										+ str(len(configs.index))
										+ str(".csv"))
						print("Iterate CSV exception,saving current progress to CSV file")
						configs.to_csv(filename)
		
		def set_configs_limit(self):
				try:
						num_configs = [
								inquirer.Text(
										"num_configs",
										message="Type the number of configs you wish to apply from a given file: ",
										)
								]
						self.num_configs = int(inquirer.prompt(num_configs,theme=GreenPassion())["num_configs"])
				except ValueError:
						print(
								"Invalid input value for the number of configs to apply from a given file. Please type a "
								"digit:"
								)
						num_configs = [
								inquirer.Text(
										"num_configs",
										message="Type the number of configs you wish to apply from a given file: ",
										)
								]
				
				try:
						self.config.add_section("MH_LIMITS")
				except:
						pass
				self.config.set("MH_LIMITS",'number_of_configs_to_apply',str(self.num_configs))
				self.write_file()
				self.read_limits()
		
		def set_create_limit(self):
				create_limit = [
						inquirer.Text("limit",message="Type a number how many top bots to create ")
						]
				create_limit_response = inquirer.prompt(create_limit,theme=GreenPassion())["limit"]
				self.limit = int(create_limit_response)
				self.config.set("MH_LIMITS",'limit_to_create',str(self.limit))
				self.write_file()
				self.read_limits()
		
		def read_limits(self):
				try:
						self.num_configs = int(self.config['MH_LIMITS'].get('number_of_configs_to_apply'))
				except Exception as e:
						print(e)
				
				try:
						self.limit = int(self.config['MH_LIMITS'].get('limit_to_create'))
				except Exception as e:
						print(e)
				try:
						self.stoploss_range = [float(self.config['MH_LIMITS'].get('stoploss_range_start')),float(self.config[
								'MH_LIMITS'].get(
								'stoploss_range_stop')),float(self.config['MH_LIMITS'].get('stoploss_range_step'))]
				except Exception as e:
						print(e)
				try:
						self.selected_intervals = json.loads(self.config['MH_LIMITS'].get('selected_intervals'))
				except Exception as e:
						print(e)
		
		def menu(self):
				live_menu = [
										# 'test',
										"Select Bots",
										"Select config file",
										"Set configs limit",
										"Set create limit",
										'Stoploss',
										"Config optimisation",
										"Change backtesting date",
										# 'Completed Backtests',
										"Start Backtesting",
										"Main Menu",
										]
				dev_menu = [
										'test',
										"Select Bots",
										"Select config file",
										"Set configs limit",
										"Set create limit",
										'Stoploss',
										"Config optimisation",
										"Change backtesting date",
										"Start Backtesting",
										'Completed Backtests',
										"Main Menu",
										]
				
				self.read_limits()
				menu = [
						inquirer.List(
								"response",
								message=f"Create: {self.limit}, Configs: {self.num_configs}",
								choices= live_menu if self.live else dev_menu
								)
						]
				
				while True:
						response = inquirer.prompt(menu,theme=GreenPassion())["response"]
						if response == "Select Bots":
								bot = self.bot_selector(15,multi=True)
						elif response == "Select config file":
								file = pd.read_csv(self.file_selector())
						elif response == "Set configs limit":
								self.set_configs_limit()
						
						elif response == "Set create limit":
								self.set_create_limit()
						
						elif response == 'Change backtesting date':
								self.write_date()
						
						elif response == 'test':
								self.bbl_menu()
						
						elif response == 'Completed Backtests':
								menu = [inquirer.List('response','Chose',choices=
								[
										'Select bot from db',
										'Print results',
										'Save results to file',
										'Back'
										])]
								while True:
										response = inquirer.prompt(menu)['response']
										
										if response == 'Select bot from db':
												if self.config_storage:
														guids = list(self.config_storage.keys())
														bl = [(x.name,x) for x in self.c.customBotApi.get_all_custom_bots(
																
																).result
														      if x.botType == 15 if bot.guid in guids]
														menu = [inquirer.List('response','Select Bot',choices=bl)]
														while True:
																bot = inquirer.prompt(menu)['response']
										
										if response == 'Print results':
												self.print_completed_configs()
										
										elif response == 'Save results to file':
												pass
										elif response == 'Back':
												break
						
						
						elif response == 'Stoploss':
								stoploss_menu = [inquirer.List('stoploss','Stoploss menu:',
								                               choices=
								                               [
										                               "Set stoploss range",
										                               "Find stoploss",
										                               'Back',
										                               ])]
								while True:
										response = inquirer.prompt(stoploss_menu)['stoploss']
										if response == 'Find stoploss':
												if not self.bots:
														self.get_first_bot()
												for b in self.bots:
														self.bot = b
														self.find_stoploss()
										
										elif response == "Set stoploss range":
												self.set_stoploss_range()
										
										elif response == 'Back':
												break
						
						elif response == "Config optimisation":
								self.bruteforce_menu()
						elif response == "Start Backtesting":
								if not self.configs:
										self.configs = pd.read_csv('./bots.csv')
								for b in self.bots:
								
										self.bot = b
										
										self.bt()
										self.setup_mh_bot()
						
						
						elif response == "Main Menu":
								break
		
		def get_first_bot(self):
				bl = self.c.customBotApi.get_all_custom_bots()
				botlist = [x for x in bl.result if x.botType == 15]
				self.bots = botlist[0:1]
				for b in self.bots:
						self.bot = b
		
		def set_configs_file(self):
				if self.configs is None:
						self.configs = pd.read_csv('./bots.csv')
						self.num_configs = 2
		
		def test_bt_couple_of_bot_ranges(self):
				self.get_first_bot()
				self.set_configs_file()
				self.configs = self.configs[0:5]
				self.configs.reset_index(inplace=True,drop=True)
				self.bt()
				self.setup_mh_bot()


		def calculate_possible_roi(self):
				print('calculating possible profit for current bot...')
				interval = self.bot.interval
				marketdata = MarketData().get_market_data(self.bot.priceMarket,interval,int(self.read_ticks() / interval))
				lowest = marketdata.Close.min()
				highest  = marketdata.Open.max()
				idxmi = marketdata.Close.idxmin()
				
				idxma = marketdata.Open.idxmax()
				if idxmi<idxma:
						first =lowest
						second = highest
				else:
						first = idxmi
						second = idxma

				print(f'low: {lowest} {idxmi} - index and high: {highest} {idxma} - index')
				percentage = (float(first) / float(second)) * float(100)
				print(f'{} is possible profit')
				self.possible_profit = round(percentage,2)
if __name__ == "__main__":
		mh = MadHatterBot()
		mh.menu()
		
		"""
				def apply_configs_menu(self):
				options = [
						"Select Bot",
						"Select file with configs",
						"Apply configs",
						"Main Menu",
				]
				config_questions = [inquirer.List("response", "Select an option: ", options)]

				while True:
						response = inquirer.prompt(config_questions,theme=GreenPassion())
						if response["response"] in options:
								ind = options.index(response["response"])
						if ind == 0:
								bot = self.bot_selector()
						elif ind == 1:
								file = pd.read_csv(self.file_selector())
						elif ind == 2:
								# print(self.configs)

								configs = self.configs.sort_values(by="roi", ascending=False)
								configs.drop_duplicates()
								configs.reset_index(inplace=True, drop=True)
								while True:
										print(configs)
										print(
												"To apply bot type config number from the left column and hit return."
										)
										print("To return to the main menu, type q and hit return")
										resp = input("Config number: ")
										try:
												if int(resp) >= 0:

														self.setup_bot_from_csv(
																self.bot, configs.iloc[int(resp)]
														)
														# print(Haas().read_ticks)
														self.bt_bot(self.bot, Haas().read_ticks())
												else:
														break
										except ValueError as e:
												break

						elif ind == 3:
								break
								
								
										# bt = self.c.customBotApi.backtest_custom_bot_on_market(
										# 		bot.accountId,
										# 		bot.guid,
										# 		int(depth),
										# 		bot.priceMarket.primaryCurrency,
										# 		bot.priceMarket.secondaryCurrency,
										# 		bot.priceMarket.contractName,
										# 		)
								
>>>
 # new_bot = self.c.customBotApi.clone_custom_bot_simple(b.accountId, b.guid, name)
								# new_bot = self.c.customBotApi.new_custom_bot(b.accountId, b.botType, name,
								#                                                   b.priceMarket.primaryCurrency,
								#                                                   b.priceMarket.secondaryCurrency,
								#                                                   b.priceMarket.contractName)
		
		
			def optimize(self):
				configs = self.config_storage[self.bot.guid]
				config = configs.iloc[0]
				cols = [
						"interval",
						"signalconsensus",
						"fcc",
						"resetmiddle",
						"allowmidsells",
						"matype",
						"rsil",
						"rsib",
						"rsis",
						"bbl",
						"devup",
						"devdn",
						"macdfast",
						"macdslow",
						"macdsign",
						"trades",
						"roi",
						]
				intervals = [1,2,3,4,5,6,10,12,15,20,30,45,60,90,120,150,180,240,360,720,1440,2880]
				for i in config.columns:
						if i == 'interval':
								time_intervals_to_test = arange(i)
		
			def finetune(self):
				if self.bot is None:
						bl = self.c.customBotApi.get_all_custom_bots()
						botlist = [x for x in bl.result if x.botType == 15]
						bot = botlist[0]
						print(bot.guid,bot.botType)
						bot = self.c.customBotApi.backtest_custom_bot_on_market(
																bot.accountId,
																bot.guid,
																1,
																bot.priceMarket.primaryCurrency,
																bot.priceMarket.secondaryCurrency,
																bot.priceMarket.contractName,
																).result
						print(bot)
						self.bot = bot
				menu = []
				steps = 4
				config = self.bot_config(self.bot)
				print(config)
				
				rsil_minus_range = [x for x in range(int(config.rsil.iloc[0]),int(config.rsil.iloc[0])-4, -1) if x >1]
				rsil_plus_range = [x for x in range(int(config.rsil.iloc[0]),int(config.rsil.iloc[0])+4, 1) if x < 60]
				
				rsil_total_range = [x for x in range(2,100,1)]
				rsil = int(config.rsil.loc[0])
				if rsil in [0,1,2]:
					rsil_neighbours_in_total_range = rsil_total_range[rsil-steps:rsil+steps]
					print(rsil_neighbours_in_total_range)
				elif rsil-steps <=0:
						rsil_neighbours_in_total_range = rsil_total_range[rsil:rsil + steps*2]
						print(rsil_neighbours_in_total_range)
			
	
		"""
