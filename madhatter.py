from numpy import arange
from haas import Haas
from ratelimit import limits,sleep_and_retry
import inquirer
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient

import datetime
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
import time
from alive_progress import alive_bar
from itertools import combinations as comb
from inquirer.themes import GreenPassion
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties

class MadHatterBot(Haas):
		def __init__(self):
				Haas.__init__(self)
				self.config = Haas().config
				self.c = HaasomeClient(self.ip,self.secret)
				self.ticks = Haas().read_ticks()
				self.stoploss_range = None
				self.num_configs = None
				self.limit = None
				self.config_storage = dict()
				self.configs = None
				self.current_config = None
		
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
		
		#
		# def make_bot_from_bot_config(self, config, name):
		#     botname = (
		#             str(config.priceMarket.primaryCurrency)
		#             + str(" / ")
		#             + str(config.priceMarket.secondaryCurrency)
		#             + str(" Roi ")
		#             + str(config.roi)
		#     )
		#     new_bot = self.create_mh(example_bot, botname)
		#     self.configure_mh_from_another_bot(config, new_bot)
		#     return new_bot.result
		
		def bruteforce_indicators(self,bot):
				
				d = self.bruteforce_rsi_corridor(bot)
		
		def bot_config(self,bot):
				botdict = {
						"roi":int(bot.roi),
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
						}
				# "pricesource": EnumPriceSource(bot.priceMarket.priceSource).name,
				# "primarycoin": bot.priceMarket.primaryCurrency,
				# "secondarycoin": bot.priceMarket.secondaryCurrency,
				df = pd.DataFrame.from_dict([botdict])
				
				return df
		
		def mad_hatter_base_parameters(self):
				ranges = {}
				ranges["interval"] = [
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
				ranges["signalconsensus"] = [bool(True),bool(False)]
				ranges["resetmiddle"] = ranges["signalconsensus"]
				ranges["allowmidsells"] = ranges["signalconsensus"]
				ranges["matype"] = list([0,1,2,3,4,5,6,7,8,9])
				ranges["fcc"] = ranges["signalconsensus"]
				
				ranges["rsil"] = list(range(2,21))
				ranges["rsib"] = list(range(2,49))
				ranges["rsis"] = list(range(51,99))
				ranges["bb"] = list(range(7,60))
				ranges["devup"] = list(arange(0.1,4.0))
				ranges["devdown"] = list(arange(0.1,4.0))
				ranges["macdfast"] = list(range(2,59,2))
				ranges["macdslow"] = list(range(40,80,2))
				ranges["macdsign"] = list(range(3,21,2))
				df = pd.DataFrame(botdict,index=range(len(botdict)))
				return df
				
				configure = self.setup(bot,df)
		
		
		
		
		
		
		def setup_bot_from_csv(self,bot,config,print_errors=False):
				
				try:
						# if params differ - applies new one.
						# if bot.bBands["Length"] != config["bbl"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(  # this way less api calls is being made
								bot.guid,EnumMadHatterIndicators.BBANDS,0,config["bbl"]
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						# if bot.bBands["Devup"] != config["devup"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								1,
								config["devup"],
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						# if bot.bBands["Devdn"] != config["devdn"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								2,
								config["devdn"],
								)
						if print_errors == True:
								print('bBands',do.errorCode,do.errorMessage)
						# if bot.bBands["MaType"] != config["matype"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								3,
								config["matype"],
								)
						
						# if bot.bBands["RequireFcc"] != bool(config["fcc"]):
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.BBANDS,
								5,
								bool(config["fcc"]),
								)
						if print_errors == True:
								print('bBands FCC',do.errorCode,do.errorMessage)
						
						# if bot.bBands["ResetMid"] != bool(config["resetmiddle"]):
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
						
						# if bot.bBands["AllowMidSell"] != bool(config["allowmidsells"]):
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
						
						# if bot.rsi["RsiLength"] != bool(config["rsil"]):
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								0,
								config["rsil"],
								)
						if print_errors == True:
								print('bool(config["fcc"]: ',bool(config["fcc"]))
								print('bBands',do.errorCode,do.errorMessage)
						
						# if bot.rsi["RsiOverbought"] != config["rsib"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.RSI,
								1,
								config["rsib"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						# if bot.rsi["RsiOversold"] != config["rsis"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,EnumMadHatterIndicators.RSI,2,config["rsis"]
								)
						
						# if bot.macd["MacdFast"] != config["macdfast"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								0,
								config["macdfast"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						# if bot.macd["MacdSlow"] != config["macdslow"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								1,
								config["macdslow"],
								)
						if print_errors == True:
								print('rsi',do.errorCode,do.errorMessage)
						
						# if bot.macd["MacdSign"] != config["macdsign"]:
						do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
								bot.guid,
								EnumMadHatterIndicators.MACD,
								2,
								config["macdsign"],
								)
						if print_errors == True:
								print('macd',do.errorCode,do.errorMessage)
						# if bot.interval != config['interval']:
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
						# if bot.useTwoSignals != bool(config['signalconsensus']):
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
				except Exception as e:
						print(e)
		
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
				
				bt_results = self.iterate_csv(self.configs[0:self.num_configs],self.bot,depth=self.ticks)
				
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
				bt_results.sort_values(by="roi",ascending=False,inplace=True)
				bt_results.drop_duplicates()
				bt_results.reset_index(inplace=True,drop=True)
				bt_results.to_csv(filename)
				
				self.config_storage[self.bot.guid] = bt_results
		
		def setup_mh_bot(self):
				bot = self.bot
				configs = self.config_storage[bot.guid]
				if self.limit > len(configs.index):
						self.limit = len(configs.index)
				# print('set configs limit', self.limit)
				for c in range(self.limit):
						name = f"{bot.name} {c} {configs.roi.iloc[c]}%"
						
						self.setup_bot_from_csv(bot,configs.iloc[c],print_errors=False)
						
						self.c.customBotApi.backtest_custom_bot(bot.guid,self.ticks)
						self.c.customBotApi.clone_custom_bot_simple(bot.accountId,bot.guid,name)
		
		def iterate_csv(self,configs,bot,depth):
				
				try:
						best_roi = 0
						configs.roi[0:-1] = 0
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
												print(
														"Current Backtest ROI: ",
														bt.roi,
														"%",
														"best ROI:",
														best_roi,
														"%",
														)
												print("\nTop 10 configs so far:\n")
												print(configs.sort_values(by="roi",ascending=False)[0:10])
										except:
												pass
										config = configs.iloc[i]
										s = self.setup_bot_from_csv(bot,config)
										# try:
										# 		print("setup bot from CSV",s.errorCode)
										# except Exception as e:
										# 		print("Setup exception",e)
										bt = self.c.customBotApi.backtest_custom_bot(bot.guid,self.ticks)
										
										try:
												print("Backtest Status: ",bt.errorCode)
												bt = bt.result
										except Exception as e:
												print("bt exception",e)
										if bt.roi > best_roi:
												best_roi = bt.roi
										configs["roi"][i] = bt.roi
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
						print("Iterate CSV exception,saving current progress")
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
						inquirer.Text("limit",message="Type how many top bots to create ")
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
		
		def set_stoploss_range(self):
				start = inquirer.text(message="Write stoploss range starting number: ")
				stop = inquirer.text(message="Write stoploss range ending number: ")
				step = inquirer.text(message="Write stoploss range stepping number: ")
				try:
						self.config.add_section("MH_LIMITS")
				except:
						pass
				self.config.set("MH_LIMITS",'stoploss_range_start',start)
				self.config.set("MH_LIMITS",'stoploss_range_stop',stop)
				self.config.set("MH_LIMITS",'stoploss_range_step',step)
				self.write_file()
				self.read_limits()
		
		def find_stoploss(self):
				bt_results = []
				start,stop,step = self.stoploss_range
				for i in arange(start,stop,step):
						do = self.c.customBotApi.set_mad_hatter_safety_parameter(self.bot.guid,EnumMadHatterSafeties(0),round(i,3))
						# print('Stoploss error message',do.errorCode,do.errorMessage)
						do2 = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.ticks)
						bt_results.append([do2.result.roi,i])
						print(f'Stoploss {i} : ROI {do2.result.roi}%')
				
				bt_results = pd.DataFrame(bt_results,columns=['roi','stoploss'])
				bt_results.sort_values(by="roi",ascending=False,inplace=True)
				bt_results.drop_duplicates()
				bt_results.reset_index(inplace=True,drop=True)
				print('Stoploss results: ',bt_results)
				print(f'Best result for bot {self.bot.name,0,bt_results.stoploss.iloc[0]} will be applied')
				do = self.c.customBotApi.set_mad_hatter_safety_parameter(self.bot.guid,0,bt_results.stoploss.iloc[0])
				do = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.ticks)
				
		def menu(self):
				self.read_limits()
				menu = [
						inquirer.List(
								"response",
								message=f"{self.limit}, {self.num_configs}",
								choices=[
										# 'Test combinations',
										"Select Bots",
										"Select config file",
										"Set configs limit",
										"Set create limit",
										"Set stoploss range",
										"Find best stoploss",
										"Change backtesting date",
										"Start Backtesting",
										"Main Menu",
										],
								)
						]
				
				while True:
						user_response = inquirer.prompt(menu,theme=GreenPassion())["response"]
						if user_response == "Select Bots":
								bot = self.bot_selector(15,multi=True)
						elif user_response == "Select config file":
								file = pd.read_csv(self.file_selector())
						elif user_response == "Set configs limit":
									self.set_configs_limit()
						
						elif user_response == "Set create limit":
								self.set_create_limit()
						
						elif user_response == 'Change backtesting date':
								self.write_date()
						
						elif user_response == 'Test combinations':
								self.finetune()
						elif user_response == 'Find best stoploss':
								for b in self.bots:
										self.bot = b
										self.find_stoploss()
						
						elif user_response =="Set stoploss range":
								self.set_stoploss_range()
						elif user_response == "Start Backtesting":
								if self.configs is None:
										self.configs = pd.read_csv('./bots.csv')
								for b in self.bots:
										self.bot = b
										self.bt()
										self.setup_mh_bot()

						
						elif user_response == "Main Menu":
								break
						

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
		"""
