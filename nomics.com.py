
import pandas as pd
import requests
import json
from pprint import pprint
# from iteration_utilities import deepflatten
from InquirerPy import inquirer
from marketdata import MarketData

class Nomics(MarketData):

	def __init__(self):
		MarketData.__init__(self)
		self.payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
		self.payload = None
		self.asset = None
		self.supported_markets = None
		
	def get_all_supported_markets(self):
		df = self.get_all_markets()
		usd_tickers = df[df.Ticker.str.contains('USD|usd')].primarycurrency.unique()
		print('len',len(usd_tickers))		
		return usd_tickers
	
	def return_predictions(self):
		
		all_markets = self.get_all_supported_markets()
		# print(all_markets)
		string = str([i for i in all_markets]).replace("'", "").replace(" ", "").replace("[", "").replace("]", "")
		# print(string)
		print('len',len(string))
		response = requests.get(f"https://nomics.com/data/currencies-predictions-ticker?ids={string}")
		# pprint(response.json())
		
		return response.json()
		
		
	
	def return_prediction(self):
		result = requests.get(f"https://nomics.com/data/currencies-predictions-ticker?ids={self.asset}")
		
		
		try:
			j = result.json()
			raw_data = [{key:value} for key, value in j[0:1][0].items()]
			base_currency = 'USD'
			predictions = [{key:value} for key, value in raw_data[1]['predictions'][0].items()] 
			predictions_dict = {}
			predictions_dict['Ticker'] = self.asset
			predictions_dict['base_currency'] = base_currency
			print(type(predictions[0]))
			for i in predictions:
				for key, value in  i.items():
					predictions_dict[key] = value	
			print(predictions_dict)
			return predictions_dict
		except IndexError:
			pass
			
if __name__ == "__main__":
	
	ncs = Nomics()
	predictions = ncs.return_predictions()
	
	# print(predictions)
	print([[x['predictions']] for x in predictions])
	print(len(predictions))
