import pandas as pd
import inquirer
from haas import Haas
import datetime
from alive_progress import alive_bar
from tqdm import tqdm
import numpy as np
from haasomeapi.enums.EnumPriceSource import EnumPriceSource


class ScalperBot(Haas):
	def __init__(self):
		Haas.__init__(self)
		self.ticks = self.read_ticks()
		self.safetythreshold = ["","",""]
		self.targetpercentage = ["","",""]
	
	def return_scalper_bots(self):
		
		bl = self.c.customBotApi.get_all_custom_bots().result
		botlist = [x for x in bl if x.botType == 3]
		return botlist
	
	
	def markets_selector(self):
		
		markets = self.c.marketDataApi.get_all_price_markets().result
		m2 = [
			(
				f"{EnumPriceSource(i.priceSource).name},{i.primaryCurrency}-"
        f"{i.secondaryCurrency}",
				i,
				)
			for i in markets
			]
		
		question = [inquirer.Checkbox("markets",message="Select markets",choices=m2)]
		
		selection = inquirer.prompt(question)
		self.markets = selection["markets"]
		# print(selection)
		return selection
	
	def setup_scalper_bot(self,bot,targetpercentage,safetythreshold):
		
		do = self.c.customBotApi.setup_scalper_bot(
			accountguid=bot.accountId,
			botguid=bot.guid,
			botname=bot.name,
			primarycoin=bot.priceMarket.primaryCurrency,
			secondarycoin=bot.priceMarket.secondaryCurrency,
			templateguid=bot.customTemplate,
			contractname=bot.priceMarket.contractName,
			leverage=bot.leverage,
			amountType=bot.amountType,
			tradeamount=bot.tradeamount,
			position=bot.coinPosition,
			fee=bot.currentFeePercentage,
			targetpercentage=targetpercentage,
			safetythreshold=safetythreshold,
			)
		print('result: ',do.errorCode,do.errorMessage)
		return do.result
	
	def set_targetpercentage_range(self):
		start_input = [
			inquirer.Text(
				"start",
				message="Define start of the target percentage range",
				
				)
			]
		end_input = [
			inquirer.Text(
				"end",message="Define end of the target percentage range",
				)
			]
		step_input = [
			inquirer.Text(
				"step",
				message="Define number of steps between start and end",
				
				)
			]
		
		start = inquirer.prompt(start_input)["start"]
		end = inquirer.prompt(end_input)["end"]
		step = inquirer.prompt(step_input)["step"]
		self.targetpercentage = [start,end,step]
	
	def set_safetythreshold_range(self):
		start_input = [
			inquirer.Text(
				"start",message="Define start of the safety threshold range",)
			]
		end_input = [
			inquirer.Text(
				"end",message="Define end of the safety threshold range",)
			]
		step_input = [
			inquirer.Text(
				"step",
				message="Define number of steps between start and end",
				
				)
			]
		
		start = inquirer.prompt(start_input)["start"]
		end = inquirer.prompt(end_input)["end"]
		step = inquirer.prompt(step_input)["step"]
		self.safetythreshold = [start,end,step]
	
	def bt_date_to_unix(self):
		
		min = self.config["BT DATE"].get("min")
		hour = self.config["BT DATE"].get("hour")
		day = self.config["BT DATE"].get("day")
		month = self.config["BT DATE"].get("month")
		year = self.config["BT DATE"].get("year")
		btd = datetime.datetime(int(year),int(month),int(day),int(hour),int(min))
		return btd
	
	def backtest(self):
		safety_combinations = list(np.arange(
			float(self.safetythreshold[0]),
			float(self.safetythreshold[1]),
			float(self.safetythreshold[2]),
			))
		target_combinations = list(np.arange(
			float(self.targetpercentage[0]),
			float(self.targetpercentage[1]),
			float(self.targetpercentage[2]),
			))
		total_combs = len(safety_combinations) * len(target_combinations)
		btd = self.bt_date_to_unix()
		if self.bots is not None:
			for bot in self.bots:
				self.bot = bot
				with alive_bar(total_combs,title=f"{self.bot.name} backtesting. ") as bar:
					results = []
					columns = ["roi","safetythreshold","targetpercentage"]
					
					for s in tqdm(
							np.arange(
								float(self.safetythreshold[0]),
								float(self.safetythreshold[1]),
								float(self.safetythreshold[2]),
								)
							):
						
						for t in tqdm(
								np.arange(
									float(self.targetpercentage[0]),
									float(self.targetpercentage[1]),
									float(self.targetpercentage[2]),
									)
								):
							
							self.setup_scalper_bot(
								bot,
								targetpercentage=round(t,2),
								safetythreshold=round(s,2),
								)
							
							bt_result = self.c.customBotApi.backtest_custom_bot(
								bot.guid,self.read_ticks()
								).result
							
							try:
								print("ROI: ",bt_result.roi,round(t,2))
								total_results = {
									"roi":bt_result.roi,
									"targetpercentage":round(t,2),
									"safetythreshold":round(s,2),
									}
								
								results.append(
									[bt_result.roi,round(t,2),round(s,2)]
									)
							except Exception as e:
								print('backtesting error: ',e)
					
					df_res = pd.DataFrame(
						results,columns=columns,index=range(len(results))
						)
					df_res.sort_values(by="roi",ascending=False,inplace=True)
					df_res.reset_index(inplace=True,drop=True)
					# print(df_res)
					self.setup_scalper_bot(
						bot,
						df_res.safetythreshold.iloc[0],
						df_res.targetpercentage.iloc[0],
						)
					
					self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
		else:
			self.bot_selector(3,multi=True)
	
	def scalper_bot_menu(self):
		# choices =
		menu = [
			inquirer.List(
				"response",
				message="Please chose an action:",
				choices=[
					"Select bots",
					"Set range for safety threshold",
					"Set range for target percentage",
					"Backtest",
					"backtest every bot",
					"Change backtesting date",
					"Main menu",
					],
				)
			]
		
		while True:
			user_response = inquirer.prompt(menu)["response"]
			if user_response == "Select bots":
				self.bot_selector(3,multi=True)
			elif user_response == "Set range for safety threshold":
				self.set_safetythreshold_range()
			elif user_response == "Set range for target percentage":
				self.set_targetpercentage_range()
			elif user_response == "Change backtesting date":
				self.write_date()
			
			elif user_response == "Backtest":
				self.backtest()
			elif user_response == "backtest every bot":
				sb = ScalperBot()
				sb.bot = self.c.customBotApi.get_all_custom_bots().result
				
				sb.backtest()
			elif user_response == "Main menu":
				break



def main():
	sb = ScalperBot()
	sb.scalper_bot_menu()
	# sb.bot = sb.return_scalper_bots()[0:2]
	# print(sb.bot)


if __name__ == "__main__":
	main()