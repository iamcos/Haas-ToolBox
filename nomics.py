
import pandas as pd
import requests
import json
from pprint import pprint
from datetime import datetime
# from iteration_utilities import deepflatten
from InquirerPy import inquirer
from marketdata import MarketData
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from InquirerPy.separator import Separator
class Nomics(MarketData):

	def __init__(self):
		MarketData.__init__(self)
		self.exchange = self.select_exchange()
		self.selected_markets = None
		
	def get_all_supported_markets(self):
		df = self.get_all_markets()
		
		usd_tickers = df[df.Ticker.str.contains('USD|usd')]
		print(usd_tickers)
		return usd_tickers
	

	def return_df_with_predictions(self):
		all_markets = self.get_all_supported_markets()
		all_markets.pricesource = [EnumPriceSource(i).name for i in all_markets.pricesource]
		if type(self.exchange[0]) != str:
				all_markets = all_markets[all_markets.pricesource==EnumPriceSource(self.exchange[0].connectedPriceSource).name]
		market_list = all_markets.primarycurrency.to_list()
		market_list = str(market_list).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")
		response = requests.get(f"https://nomics.com/data/currencies-predictions-ticker?ids={market_list}")
		tickers = [i['id'] for i in response.json()]
		markets = all_markets[all_markets.primarycurrency.isin(tickers)][all_markets.Ticker.isin(all_markets.Ticker.unique())].reset_index(drop=True)
		predictions = [i['predictions'] for i in response.json()]
		clean_predictions = []
		for d in predictions:
			for dd in d:
				clean_predictions.append(dd)
		coins_df = pd.DataFrame(tickers,columns=['primarycurrency'])
		predictions_df = pd.DataFrame(clean_predictions)
		predictions_with_tickers = pd.concat([coins_df, predictions_df], axis=1,join='outer')
		predictions_with_tickers_and_markets = predictions_with_tickers.merge(markets,how='outer',left_on='primarycurrency',right_on='primarycurrency')
		
		return predictions_with_tickers_and_markets
		

	def clean_predictions_df(self,predictions):
		predictions.sort_values(by='price_change_pct',ascending=False,inplace=True)
		predictions['avg_error_pct'] = pd.to_numeric(predictions['avg_error_pct'], ).map("{:.0%}".format)
		predictions['avg_error_pct_30d'] = pd.to_numeric(predictions['avg_error_pct_30d'], ).map("{:.0%}".format)
		
		predictions['avg_error_pct_7d'] = pd.to_numeric(predictions['avg_error_pct_7d'], ).map("{:.0%}".format)
		predictions['price_change_pct'] = pd.to_numeric(predictions['price_change_pct'], ).map("{:.0%}".format)
		predictions['timestamp_end'] = (pd.to_datetime(predictions['timestamp_end'], dayfirst=True, utc=True).dt.tz_localize(None)-datetime.utcnow()).dt.days
		predictions['timestamp_start'] = pd.to_datetime(predictions['timestamp_start'], dayfirst=True, utc=True).dt.tz_localize(None)
		predictions.to_csv('nomics_with_haas.csv')
		return predictions

	def select_markets(self, predictions):
		rows = [{'name':f"{x[0]} ^ {x[5]}={x[6]}≠{x[8]}D|7d: {x[3]} 30d: {x[2]} A: {x[1]}|{x[12]}/{x[14]}", 'value':[x[13], x[6], x[14], x[12]]} for x in predictions.values.tolist()]
					
		resp = inquirer.fuzzy('Choose! ', choices=rows, multiselect=True).execute()
		self.markets = resp
		return resp
if __name__ == "__main__":
	
	ncs = Nomics()
	pred = {}
	predictions = ncs.return_df_with_predictions()
	predictions = ncs.clean_predictions_df(predictions)
	choices = ncs.select_markets(predictions)
	for i in choices:
  		print(i)
	

