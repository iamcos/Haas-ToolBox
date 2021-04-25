# from janitor import expand_grid
import pandas as pd
from numpy import NaN
from numpy.ma import arange



class FineTune:
	
	def clean_df(self,df):
		cols = [
			"interval",
			"signalconsensus"
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
			if c not in cols:
				df.drop(c,axis=1,inplace=True)
		return df
	
	
	def create_configs_from_top_results(self):

		columns = [
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
		int_cols = [
			'rsil',
			"rsib",
			"rsis",
			"bbl",
			"macdfast",
			"macdslow",
			"macdsign",
			]
		float_cols = [
			"devup",
			"devdn",
			]
		bool_cols = [
			"signalconsensus",
			"fcc",
			"resetmiddle",
			"allowmidsells",
			]
		top_configs = pd.read_csv('bots.csv')[:3]
		top_configs = self.clean_df(top_configs)
		ranges = {}
		
		for column in float_cols:
				ranges[column] = arange(top_configs[column].min(), top_configs[column].max(), 0.2)
		for column in int_cols:
				ranges[column] = range(int(top_configs[column].min()), int(top_configs[column].max()), 2)
		for column in bool_cols:
				ranges[column] = [True,False]
		ranges['matype'] = range(0,8)
	
		df = pd.concat([pd.DataFrame(ranges[x],columns=[x]).reset_index() for x in list(ranges.keys())],ignore_index=False,axis=1)

		dfs = []
		for i in range(len(df.index)):
			config = self.augment_config_with_missing_columns(df.iloc[i],top_configs.iloc[0])
			dfs.append(config)
		df = pd.concat(dfs)
		return df
		
	def augment_config_with_missing_columns(self,config,bot):
			bot_configuration = bot
			
			for col in config.index:
					
					bot_configuration[col] = config[col]
			return bot_configuration