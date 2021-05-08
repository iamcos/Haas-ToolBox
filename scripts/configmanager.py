import datetime
import os
import time

from InquirerPy import inquirer



class ConfigManager:
	
		def get_csv_files(self):
			files = []
			for file in os.listdir('.'):
				# if file.endswith(".csv") or file.endswith('.json'):
				if file.endswith(".csv"):
					files.append(file)
			return files
		def read_range(self,vars=vars):
			return [x for x in [self.config["MH_LIMITS"].get(p) for p in vars]]

		def check_config(self):

			if not os.path.exists("config.ini"):
				self.request_server_data()

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

					self.request_server_data()
					self.check_config()
				return client
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


		def request_server_data(self):


			ip = inquirer.text(message="Type Haas Local api IP like so: 127.0.0.1",default="127.0.0.1").execute()
			port = inquirer.text(message="Type Haas Local api PORT like so: 8095",default="8095").execute()
			secret = inquirer.text(message="Type Haas Local Key (Secret) like so: 123",).execute()

		

			self.config["SERVER DATA"] = {
				"server_address":f"http://{ip}:{port}",
				"secret":secret
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

			
			y= inquirer.text(message=choices[0]).execute()
			m= inquirer.text(message=choices[1]).execute()
			d= inquirer.text(message=choices[2]).execute()
			h= inquirer.text(message=choices[3]).execute()
			min= inquirer.text(message=choices[4]).execute()
			


			

			self.config["BT DATE"] = {
				"year": y,
				"month": m,
				"day": d,
				"hour": h,
				"min": min,
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
			# print('read ticks delta minutes',int(delta_minutes))
			return int(delta_minutes)



