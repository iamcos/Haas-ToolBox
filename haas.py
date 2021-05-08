import configparser as cp
import datetime
import os

from InquirerPy import inquirer
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient
from scripts.configmanager import ConfigManager



class Haas(ConfigManager):
		"""
		Haasonline trading software interaction class: get botlist, marketdata,
		create bots and configure their parameters,
		initiate backtests and so forth can be done through this class
		"""

		def __init__(self):
			self.config = cp.ConfigParser()
			self.bot = None
			self.bots = None
			self.ip = None
			self.secret = None
			self.check_config()

			self.c = self.client()
			self.ticks = self.read_ticks()





		def client(self):
			config_data = self.config

			haasomeclient = HaasomeClient(self.ip,self.secret)
			return haasomeclient


			return ticks

		def bot_selector(self,botType,multi=False):

			bots = [
				x
				for x in self.c.customBotApi.get_all_custom_bots().result
				if x.botType == botType
				]
				
			bots.sort(key=lambda x:x.name,reverse=False)
			b2 = [{'name':f"{i.name} {i.priceMarket.primaryCurrency}-"
				f"{i.priceMarket.secondaryCurrency}, {i.roi}",'value':i} for i in bots]

			if multi != True:
				bots = inquirer.select(
	
						message="Select SINGLE BOT using arrow and ENTER keys",
						choices=b2,
						).execute()
					
				self.bot = bots
				self.bots = [self.bot]
			


			else:
				bots = inquirer.select(
						
						message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
								"   Confirm selection using ENTER.",
						choices=b2,
						multiselect=True
						).execute()
				self.bots = bots
				
		def calculate_ticks_from_bot_trades(self,bot):
				
			trades_df = self.trades_to_df(bot)
			first_trade = trades_df.date.iloc[0]
			
			delta = datetime.datetime.now() - first_trade
			delta_minutes = delta.total_seconds() / 60
			ticks = delta_minutes
			
		def file_selector(self):
			"""[Displays multiple files and allows for t heir selection
			Selection then sets self.file path for reference and
			reads confis into a database self.configs]

			Args:
				path (str, optional): [description]. Defaults to ".".

			tsm
			"""
			files = self.get_csv_files()
			# print(files[0:5])
			file = inquirer.select(message="Please Select file from list: ", choices=[i for i in files]).execute()

			self.configs = pd.read_csv(file)

		def return_bot_objects(self):
			files = []
			for file in os.listdir("./bt_results/"):
				# if file.endswith(".obj") or file.endswith('.json'):
				if file.endswith(".obj"):
					files.append(file)
			file = inquirer.select(message="MH Bots: ",choices=files,
				).execute()  # where b bot object returned from dic[x] name list
			objects = pd.read_pickle(f"./bt_results/{file}")
			n = [[f"{x.name}| ROI: {x.roi}"][0] for x in objects]
			b = [x for x in objects]  # creates list of names
			dic = dict(zip(b,n))  # creates zipped obj/names list
			botobj = inquirer.select(message="MH Bots: ",choices=dic,
				).execute()  # where b bot object returned from dic[x] name list
			return botobj
		def trades_to_df(self,bot):
			completedOrders = [
				{
					"orderId":x.orderId,
					"orderStatus":x.orderStatus,
					"amountFilled":x.amountFilled,
					"orderType":x.orderType,
					"amount":x.amount,
					"price":x.price,
					"date":pd.to_datetime(x.unixAddedTime,unit="s"),
					}
				for x in bot.completedOrders
				]

			orders_df = pd.DataFrame(completedOrders)
			return orders_df



