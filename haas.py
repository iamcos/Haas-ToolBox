import configparser as cp
import datetime
import os
import time

import inquirer
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient
from inquirer.themes import GreenPassion



class Haas:
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

			self.c = HaasomeClient(self.ip,self.secret)
			self.ticks = self.read_ticks()
			self.live = True


		def read_range(self,vars=vars):
			return [x for x in [self.config["MH_LIMITS"].get(p) for p in vars]]

		def check_config(self):

			if not os.path.exists("config.ini"):
				self.get_server_data()

			else:
				# Read File
				self.config.read("./config.ini")

				ip = self.config["SERVER DATA"].get("server_address")
				secret = self.config["SERVER DATA"].get("secret")
				self.ip = ip
				self.secret = secret
				client = self.client()
				# print(f'Connection status: {client.accountDataApi.get_all_wallets().errorCode.value}')

				if client.accountDataApi.get_all_wallets().errorCode.value == 100:
					print("Successfully connected!")

				elif client.accountDataApi.get_all_wallets().errorCode.value == 9002:
					for i in range(10):
						print(f"Server may be offline...")
						print(f"Retrying {i} out of 10")
						time.sleep(5)
						if client.accountDataApi.get_all_wallets().errorCode.value == 100:
							break
				else:

					self.get_server_data()
					self.check_config()
				return client

		def client(self):
			config_data = self.config

			haasomeclient = HaasomeClient(self.ip,self.secret)
			return haasomeclient

		def read_limits(self):
			try:
				vars = ['pricespread_start','pricespread_end','pricespread_step']
				self.pricespread = self.read_range(vars)

			except Exception as e:
				print(e)

			try:
				vars = ["percentageboost_start","percentageboost_end",
						"percentageboost_step"]
				self.percentageboost = self.read_range(vars)

			except Exception as e:
				print(e)
			try:
				vars = ["percentageboost_start","percentageboost_end",
						"percentageboost_step"]
				self.multiplyer = self.read_range(vars)
			except Exception as e:
				print(e)
			try:
				vars = ['multiplyer_min_end','multiplyer_min_start','multiplyer_min_step']
				self.multiplyer_min = self.read_range(vars)
			except Exception as e:
				print(e)
			try:
				vars = ['multiplyer_max_start','multiplyer_max_stop','multiplyer_max_step']
				self.multiplyer_max = self.read_range(vars)
			except Exception as e:
				print(e)
			try:
				vars = ['Total_buy','Total_sell']
				self.totalbuy,self.totalsell = self.read_range(vars)
			except Exception as e:
				print(e)

		def write_file(self):
			self.config.write(open("config.ini","w"))
			self.read_limits()

		def init_config(self):
			# self.config = cp.ConfigParser().read('config.ini')
			# return .read('config.ini')‹#3  £
			pass


		def get_server_data(self):

			server_api_data = [
				inquirer.Text(
					"ip","Type Haas Local api IP like so: 127.0.0.1",default="127.0.0.1"
					),
				inquirer.Text(
					"port","Type Haas Local api PORT like so: 8095",default="8095"
					),
				inquirer.Text(
					"secret",
					"Type Haas Local Key (Secret) like so: 123",
					),
				]
			connection_data = inquirer.prompt(server_api_data,theme=GreenPassion())

			self.config["SERVER DATA"] = {
				"server_address":"http://"
								+ connection_data["ip"]
								+ ":"
								+ connection_data["port"],
				"secret":connection_data["secret"],
				}
			self.ip = self.config["SERVER DATA"].get("server_address")
			self.secret = self.config["SERVER DATA"].get("secret")
			self.write_file()

		def write_date(self):

			choices = [
				f"Write Year",
				f"Write month (current is {str(datetime.datetime.today().month)}): ",
				f"Write day (today is {str(datetime.datetime.today().day)}: ",
				f"Write  hour (now is {str(datetime.datetime.today().hour)}):",
				f"Write min (now {str(datetime.datetime.today().minute)}): ",
			]

			date_q = [
				inquirer.Text("y", message=choices[0]),
				inquirer.Text("m", message=choices[1]),
				inquirer.Text("d", message=choices[2]),
				inquirer.Text("h", message=choices[3]),
				inquirer.Text("min", message=choices[4]),
			]


			answers = inquirer.prompt(date_q,theme=GreenPassion())

			self.config["BT DATE"] = {
				"year": answers["y"],
				"month": answers["m"],
				"day": answers["d"],
				"hour": answers["h"],
				"min": answers["min"],
			}

			self.write_file()

		def read_ticks(self):
			date_dict = {}

			try:
				for i in ["min", "hour", "day", "month", "year"]:
					date_dict[i] = self.config["BT DATE"].get(i)
			except Exception as e:
				print("read ticks",e)
				self.write_date()

			dt_from = datetime.datetime(
				int(date_dict["year"]),
				int(date_dict["month"]),
				int(date_dict["day"]),
				int(date_dict["hour"]),
				int(date_dict["min"]),
			)

			delta = datetime.datetime.now() - dt_from
			delta_minutes = delta.total_seconds() / 60

			return int(delta_minutes)

		def calculate_ticks_from_bot_trades(self,bot):
  			
			trades_df = self.trades_to_df(bot)
			first_trade = trades_df.date.iloc[0]
			
			delta = datetime.datetime.now() - first_trade
			delta_minutes = delta.total_seconds() / 60
			ticks = delta_minutes
			return ticks
		def bot_selector(self,botType,multi=False):

			bots = [
				x
				for x in self.c.customBotApi.get_all_custom_bots().result
				if x.botType == botType
				]
		
  
			bots.sort(key=lambda x:x.name,reverse=False)
			b2 = [(f"{i.name} {i.priceMarket.primaryCurrency}-"
				f"{i.priceMarket.secondaryCurrency}, {i.roi}",i) for i in bots]

			if multi != True:
				question = [
					inquirer.List(
						"bot",
						message="Select SINGLE BOT using arrow and ENTER keys",
						choices=b2,
						)
					]
				try:
					self.bot = inquirer.prompt(question,theme=GreenPassion())['bot']
					self.bots = [self.bot]
				except Exception as e:
					print("Bot Selection error",e)


			else:
				question = [
					inquirer.Checkbox(
						"bots",
						message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
								"   Confirm selection using ENTER.",
						choices=b2,
						)
					]

				try:
					self.bots = inquirer.prompt(question,theme=GreenPassion())['bots']

				except Exception as e:
					print("Bot Selection error",e)


		def get_csv_files(self,path="./"):
			files = []
			for file in os.listdir(path):
				# if file.endswith(".csv") or file.endswith('.json'):
				if file.endswith(".csv"):
					files.append(os.path.join(path,file))
			return files

		def file_selector(self,path="."):
			"""[Displays multiple files and allows for t heir selection
			Selection then sets self.file path for reference and
			reads confis into a database self.configs]

			Args:
				path (str, optional): [description]. Defaults to ".".

			tsm
			"""
			files = self.get_csv_files(path)
			# print(files[0:5])
			question = [
				inquirer.List("file", "Please Select file from list: ", [i for i in files])
			]

			selection = inquirer.prompt(question,theme=GreenPassion())
			self.file = selection["file"]
			self.configs = pd.read_csv(self.file)

		def return_bot_objects(self):
			files = []
			for file in os.listdir("./bt_results/"):
				# if file.endswith(".obj") or file.endswith('.json'):
				if file.endswith(".obj"):
					files.append(file)
			file = inquirer.list_input(message="MH Bots: ",choices=files,
				)  # where b bot object returned from dic[x] name list
			objects = pd.read_pickle(f"./bt_results/{file}")
			n = [[f"{x.name}| ROI: {x.roi}"][0] for x in objects]
			b = [x for x in objects]  # creates list of names
			dic = dict(zip(b,n))  # creates zipped obj/names list
			botobj = inquirer.list_input(message="MH Bots: ",choices=dic,
				)  # where b bot object returned from dic[x] name list
			return botobj

		def last_trades_to_df(self,trades):
			df = [
				{
					"orderId":x.orderId,
					"orderStatus":x.orderStatus,
					"amountFilled":x.amountFilled,
					"orderType":x.orderType,
					"amount":x.amount,
					"price":x.price,
					"date":pd.to_datetime(x.unixAddedTime,unit="s"),
					}
				for x in trades
				]
			return df

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



