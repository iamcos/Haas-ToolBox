# from janitor import expand_grid
import pandas as pd
from numpy import NaN
from numpy.ma import arange



class FineTune:
	
	def clean_df(self,df):
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
			"obj",
			]
		
		for c in df.columns:
			if c not in self.columns:
				df.drop(c,axis=1,inplace=True)
		return df
	
	
	def create_configs_from_top_results(self):

		self.columns = [
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
			"obj",
			]
		self.int_cols = [
			'rsil',
			"rsib",
			"rsis",
			"bbl",
			"macdfast",
			"macdslow",
			"macdsign",
			]
		self.float_cols = [
			"devup",
			"devdn",
			]
		self.bool_cols = [
			"signalconsensus",
			"fcc",
			"resetmiddle",
			"allowmidsells",
			]
		self.range_cols = [
			"matype",
			"interval",
			]
		top_configs = pd.read_csv('BTC_USDT 9 0.0%_12-12_40.csv')[:3]
		# top_configs = self.config_storage(self.bot.guid)[0:5]
		top_configs = self.clean_df(top_configs)
		# print(top_configs)
		# top_configs= top_configs.drop(['roi','obj','trades'],axis=0)
		columns = top_configs.columns
		ranges = {}
		
		for column in self.float_cols:
				ranges[column] = arange(top_configs[column].min(), top_configs[column].max(), 0.2)
		for column in self.int_cols:
				ranges[column] = range(int(top_configs[column].min()), int(top_configs[column].max()), 2)
		for column in self.bool_cols:
				ranges[column] = [True,False]
		# ranges['interval'] = self.intervals_list
		ranges['matype'] = range(0,7)
		# print(ranges)
		
		df = pd.concat([pd.DataFrame(ranges[x],columns=[x]).reset_index() for x in list(ranges.keys())],ignore_index=False,axis=1)

		# print(df)
	
		dfs = []
		for i in range(len(df.index)):
			# print(i)
			config = self.augment_config_with_missing_columns(df.iloc[i],top_configs.iloc[0])
			dfs.append(config)
		df = pd.concat(dfs)
		# print(df)
		return df
		
	def augment_config_with_missing_columns(self,config,bot):
			bot_configuration = bot
			# bot_configuration = self.bot_config(bot.guid)
			
			for col in config.index:
					
					bot_configuration[col] = config[col]
			# print(bot_configuration)
			return bot_configuration