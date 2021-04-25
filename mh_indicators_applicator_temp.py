from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
import pandas as pd

def setup_bot_from_df(config):
				ordered_indicators_params = {'bbands':{'bbl':0,'devup':1,'devdn':2,'matype':3,'fcc':5,'resetmiddle':6,'allowmidsells':7,'enum':EnumMadHatterIndicators.BBANDS},'rsi':{'rsil':0,'rsib':1,'rsis':2,'rsi':EnumMadHatterIndicators.RSI},'macd':{'macdfast':0,'macdslow':1,'macdsign':2,'enum':EnumMadHatterIndicators.MACD}}
				for column in config.columns:
					# print(column)
					if column in [i for i in [[k for k,v in value.items()] for key,value in ordered_indicators_params.items()]]:
						print(True) 
				
				# print(ordered_indicators_params['bbands'].keys())
				# print([[key,[{k:v} for k,v in value.items()]] for key,value in ordered_indicators_params.items()])
				# print([[k for k,v in value.items()] for key,value in ordered_indicators_params.items()])
				print([i[0:1] for i in [[k for k,v in value.items()] for key,value in ordered_indicators_params.items()]])

df = pd.read_csv('bots.csv')
setup_bot = setup_bot_from_df(df)

# def 	
# 				do = self.c.customBotApi.set_mad_hatter_safety_parameter(
#             bot.guid, EnumMadHatterSafeties(0), 0)
				
# 				do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
#             # this way less api calls is being made
#             bot.guid,
#             ,
#             0,
#             int(config["bbl"]),
#         )
