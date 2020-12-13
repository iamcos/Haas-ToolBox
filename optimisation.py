import inquirer
import pandas as pd
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from numpy.ma import arange


class Optimize():
		
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
				print(f'{self.bot.name} selected. Market data is being fetched, backtesting initiated...')
				bt_results = []
				self.c.customBotApi.set_mad_hatter_safety_parameter(self.bot.guid,EnumMadHatterSafeties(0),round(0,2))
				do = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.read_ticks())
				expected_roi = do.result.roi
				# bt_results.append([expected_roi,0])
				print(f'Target ROI: {expected_roi}% with stoploss set to 0')
				if not self.extended_range:
						start,stop,step = self.stoploss_range
				else:
						start,stop,step = self.extended_range
				for i in arange(start,stop,step):
						self.c.customBotApi.set_mad_hatter_safety_parameter(self.bot.guid,EnumMadHatterSafeties(0),round(i,2))
						
						do2 = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.read_ticks())
						bt_results.append([do2.result.roi,round(i,2)])
						print(f'Current stoploss {round(i,2)} : ROI {do2.result.roi}% with {expected_roi}% set as target')
				
				bt_results = pd.DataFrame(bt_results,columns=['roi','stoploss'])
				bt_results.sort_values(by="roi",ascending=False,inplace=True)
				bt_results.drop_duplicates()
				bt_results.reset_index(inplace=True,drop=True)
				print('Stoploss results: ',bt_results)
				print(f'Best result for bot {self.bot.name,bt_results.stoploss.iloc[0]}: {bt_results.roi.iloc[0]} is O.K.'
				      )
				if bt_results.roi.iloc[0] >= expected_roi:
						print(f'Stoploss {bt_results.stoploss.iloc[0]} does not interfiere with bot performance. Will be applied')
						do = self.c.customBotApi.set_mad_hatter_safety_parameter(self.bot.guid,0,bt_results.stoploss.iloc[0])
						do = self.c.customBotApi.backtest_custom_bot(self.bot.guid,self.read_ticks())
						self.extended_range = None
				else:
						print(f'{bt_results.stoploss.iloc[0]} produces {bt_results.roi.iloc[0]} which is smaller than '
						      f'{expected_roi}.')
						print('Within a given  range acceptible stoploss has not been found.')
						print(f'Expanding stoploss range by 5 steps.')
						start = stop + step
						stop = stop + step * 6
						self.extended_range = [start,stop,step]
						print(f'Stoploss search has been expanded by 5 more steps')
						self.find_stoploss()
		
		def intervals_menu(self):
				try:
						range = self.ranges.bot.intervals.selected
				except:
						range = self.ranges.bot.intervals.selected =	self.select_intervals()
				i_menu = [inquirer.List(
						'response',message=f'Selected intervals: { range} :',
						choices=[
								'Select Bots',
								'Select Intervals',
								'Backtest Selected Intervals',
								'Backtest all Intervals',
								'Back'
								]
						)]
				
				
				while True:
						response = inquirer.prompt(i_menu)['response']
						
						if response == "Select Intervals":
								self.ranges.bot.intervals.selected = self.select_intervals()

						
						elif response == "Backtest Selected Intervals":
								
								self.bt_intervals()
						
						elif response == 'Backtest all Intervals':
								self.ranges.bot.intervals.selected = self.ranges.bot.intervals.list
								self.bt_intervals()
						
						elif response == 'Select Bots':
								bot = self.bot_selector(15)
						elif response == 'Back':
								break
						elif response == 'test':
								pass
		
		def bt_intervals(self):
				try:
						if self.ranges.bot.intervals.selected:
								if self.bot:
										
										bot = self.bot
										self.bt_interval(bot)
						
								if self.bots:
										for bot in self.bots:
												bot = self.bot
												self.bt_interval(bot)
								else:
										self.bots=[self.bot]
						else:
								print('Select Intervals first')
								self.select_intervals()
								self.bt_intervals()
				except Exception as e:
						print('error in bt_intervals',e)
						self.ranges.bot.intervals.selected = self.select_intervals()
						self.bt_intervals()
		def bt_interval(self,bot):
				config = self.bot_config(bot)
				intervals = self.ranges.bot.intervals.selected
				bt_results = []
				print(f'Initiating {bot.name} backtesting process...')
				rangelen = len(intervals)
				new_configs = s = pd.DataFrame([config.iloc[0].tolist()] * rangelen,columns=
				config.columns)
				new_configs.interval = intervals
				
				configs = self.remove_already_backtested(new_configs)
				if len(configs.index):
						for i in configs.index:
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
										interval=configs.loc[int(i),'interval'],
										includeIncompleteInterval=bot.includeIncompleteInterval,
										mappedBuySignal=bot.mappedBuySignal,
										mappedSellSignal=bot.mappedSellSignal,
										)
								print('interval testing',do.errorMessage,do.errorMessage)
								bt = self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
								bot_config = self.bot_config(bt.result)
								print(f'  BT result: {bt.result.roi}% with interval {configs.loc[int(i),"interval"]} minutes')
								bt_results.append(bot_config)
				else:
								bt_results.append(config)
				bt_results = pd.concat(bt_results)
				bt_results2 = pd.DataFrame(bt_results)
				bt_results2.sort_values(by="roi",ascending=False,inplace=True)
				bt_results2.drop_duplicates()
				bt_results2.reset_index(inplace=True,drop=True)
				self.store_results(bt_results2)
				
				return bt_results
		
		def bt_consensus(self,bot):
				
				bt_results = []
				print(f'Initiating {bot.name} backtesting process...')
				for i in self.parameter['signalconsensus']:
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
								useconsensus=i,
								disableAfterStopLoss=bot.disableAfterStopLoss,
								interval=bot.interval,
								includeIncompleteInterval=bot.includeIncompleteInterval,
								mappedBuySignal=bot.mappedBuySignal,
								mappedSellSignal=bot.mappedSellSignal,
								)
						# print('interval testing',do.errorMessage,do.errorMessage)
						bt = self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
						bot_config = self.bot_config(bt.result)
						print(f'{bt.result.roi}% with consensus {i}')
						bt_results.append(bot_config)
				bt_results = pd.concat(bt_results)
				bt_results2 = pd.DataFrame(bt_results)
				bt_results2.sort_values(by="roi",ascending=False,inplace=True)
				bt_results2.reset_index(inplace=True,drop=True)
				self.store_results(bt_results2)
				return bt_results
		
		def select_intervals(self):
				
				intervals = [inquirer.Checkbox(
						'intervals',message='Select required intervals using space, confirm with enter: ',
						choices=self.ranges.bot.intervals.list
						
						)]
				selected_intervals = inquirer.prompt(intervals)['intervals']
				self.config.set("MH_LIMITS",'selected_intervals',str(selected_intervals))
				self.write_file()
				
				return selected_intervals
		
		def bbl_menu(self):
				
				live_menu = [
                  # 'test',
                  'Select Bot',
                  'Change length range',
                  "Change BT date",
                  'Backtest range',
                  # 'Discover profit',
                  'Back'

                  ]
				dev_menu =  [
                  'test',
                  'Select Bot',
                  'Change length range',
                  "Change BT date",
                  'Backtest range',
                  'Discover profit',
                  'Back'

                  ]
				 
				
				bbl_menu = [inquirer.List('response',message=f'BB Length range: {self.ranges.indicators.bBands.length}',
				                          choices= live_menu if self.live else dev_menu
				                          )]
				while True:
						response = inquirer.prompt(bbl_menu)['response']
						if response == "Select Bot":
								bot = self.bot_selector(15)
						elif response == "Change length range":
								start = int(inquirer.text('Define bBands Length range start: '))
								stop = int(inquirer.text('Define bBands Length range stop: '))
								step = int(inquirer.text('Define bBands Length range step: '))
								self.ranges.indicators.bBands.length = start,stop,step
								# print(f'bBands Length range now set to {start}{stop} with step {step}')
								try:
										self.config.add_section('MH_INDICATOR_RANGES')
								except:
										pass
								self.config.set('MH_INDICATOR_RANGES','length_range',str(self.ranges.indicators.bBands.length))
								self.write_file()
						elif response == "Backtest range":
								self.backtest_bbands_length()
						elif response == 'test':
								self.get_first_bot()
								self.ranges.indicators.bBands.length = 2,5,1
								self.backtest_bbands_length()
								self.ranges.indicators.bBands.length = 3,7,1
								self.backtest_bbands_length()
						elif response == 'Back':
								break
		
		def backtest_bbands_length(self):
				bot = self.bot
				configs = self.bot_config(bot)
				start,stop,step = self.ranges.indicators.bBands.length
				bbl_range = range(start,stop + step,step)
				rangelen = len(bbl_range)
				new_configs = s = pd.DataFrame([configs.iloc[0].tolist()] * rangelen,columns=
				configs.columns)
				new_configs.bbl = bbl_range

				configs = self.remove_already_backtested(new_configs)
				
				for i in range(len(configs.index)):
						
						
						do = self.setup_bot_from_csv(bot=self.bot,config=configs.iloc[i])
						# do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
						# 		bot.guid,EnumMadHatterIndicators.BBANDS,0,int(configs.bbl.iloc[i])
						# 		)
						print(f'{bot.name} bBands Length set to {int(configs.bbl.iloc[i])}')
						
						# print('bBands L',do.errorCode,do.errorMessage)
						print('Now backtesting...')
						bt = self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
						# print(bt.errorCode,bt.errorMessage)
						print(f'{int(configs.bbl.iloc[i])} length ROI: {bt.result.roi} %')
						configs.loc[i,'roi'] = bt.result.roi
						configs.loc[i,'obj'] = bt.result
				self.store_results(configs)
		
		def store_results(self,bt_results):
				
				if self.bot.guid in self.config_storage:
						configs = self.config_storage[self.bot.guid]
						
						configs = configs.append(bt_results)
						configs.reset_index(inplace=True,drop=True)
						configs.sort_values(by="roi",ascending=False)
						configs.drop_duplicates(subset=self.columns,inplace=True)
						self.config_storage[self.bot.guid] = configs
						print(f'backtesting results have been added to current backtesting session storage pool.')
				
				else:
						self.config_storage[self.bot.guid] = bt_results
						print(self.config_storage[self.bot.guid].drop('obj',axis=1))
						print(f'Backtesting storage pool has been created and updated with current backtesting session results.')
		
		def remove_already_backtested(self,new_configs):
				columns = self.columns
				if self.bot.guid in self.config_storage:
						
						configs = self.config_storage[self.bot.guid].drop(['obj','roi'],axis=1)
						new_configs = new_configs.drop(['obj','roi'],axis=1)
						for i in configs.columns:
								if i not in columns:
										try:
												configs.drop(i,axis=1,inplace=True)
												new_configs.drop(i,axis=1,inplace=True)
										except:
												pass
						# print('configs',configs)
						# print('new configs',new_configs)
						
						unique_configs = new_configs.merge(configs,how='outer',indicator=True).loc[lambda x:x['_merge'] == 'left_only']
						for i in columns:
								if i not in columns:
										unique_configs.drop(i,axis=1,inplace=True)
						print('unique configs',unique_configs)
						print(f'Duplicate configs removed, {len(unique_configs.index)} will be backtested.')
						return unique_configs
				
				else:
						return new_configs
		
		def print_completed_configs(self):
				print(self.config_storage(self.bot.guid))
		def bruteforce_menu(self):
				live_menu = [
										'Interval',
										# 'Signal Consensus',
										'bBands length',
										# 'bBands Devup',
										# 'bBands Devdown',
										# 'MA Type',
										# 'Rsi Length',
										# 'Rsi Buy',
										# 'Rsi Sell',
										# 'MACD Slow',
										# 'MACD Fast',
										# 'MACD Signal',
										]
				dev_menu = [
										'test',
										'Interval',
										# 'Signal Consensus',
										# 'bBands length',
										# 'bBands Devup',
										# 'bBands Devdown',
										# 'MA Type',
										# 'Rsi Length',
										# 'Rsi Buy',
										# 'Rsi Sell',
										# 'MACD Slow',
										# 'MACD Fast',
										# 'MACD Signal',
										'New configs'
										]
				
				self.parameter = {}
				bf_menu = [
						inquirer.List(
								"response",
								message='Select a parameter to bruteforce:',
								choices= live_menu if self.live else dev_menu
								)]
					
				response = inquirer.prompt(bf_menu)['response']
				
				if response == 'Interval':
						self.response = response
						self.intervals_menu()
				elif response == 'Signal Consensus':
						self.response = response
						self.bt_consensus()
				elif response == 'bBands length':
						self.bbl_menu()
				elif response == 'bBands Devup':
						pass
				elif response == 'bBands Devdown':
						pass
				elif response == 'MA Type':
						pass
				elif response == 'Rsi Length':
						pass
				elif response == 'Rsi Buy':
						pass
				elif response == 'Rsi Sell':
						pass
				elif response == 'MACD Slow':
						pass
				elif response == 'MACD Fast':
						pass
				elif response == 'MACD Signal':
						pass
				elif response == 'New configs':
						ranges = self.create_configs_from_top_results()
						
						
