import configparser as cp
import datetime

from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumPlatform import EnumPlatform
from InquirerPy import inquirer
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient
<<<<<<< Updated upstream
from scripts.configmanager import ConfigManager
from configsstorage import ConfigsManagment
from haasomeapi.enums.EnumTradeType import EnumTradeType


class Haas(ConfigManager,ConfigsManagment):
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
=======
from pandas.core.frame import DataFrame
from scripts.config_manager import ConfigManager
from bots_creator import BotsCreator

"""
Haasonline trading software interaction class: get bots list, market data,
create bots and configure their parameters,
initiate back tests and so forth can be done through this class
"""


# TODO: Make SRP
# TODO: Rename pass more info
class Haas:

    def __init__(self) -> None:

        self.configs_management: BotsCreator = BotsCreator()
        self.config_manager: ConfigManager = ConfigManager()
        self.config_parser: ConfigParser = self.config_manager.get_config_data()



        self.bot = None
        self.bots = None
        self.bot_type = None


        self.client: HaasomeClient = self.config_manager.check_config()
        self.ticks: int = self.config_manager.read_ticks()


>>>>>>> Stashed changes

			self.c = self.client()
			self.ticks = self.read_ticks()


		def get_accounts_with_details(self):
			accounts = self.c.accountDataApi.get_all_account_details().result
			accounts_with_details = list(accounts.values())
			return accounts_with_details

		def select_exchange(self):
			accounts = self.get_accounts_with_details()
			accounts_inquirer_format = [
							{
											"name": f"{EnumPriceSource(i.connectedPriceSource).name} {i.name} {EnumPlatform(i.platformType).name} "
											f"",
											"value": i,
							}
							for i in accounts
			]
			exchange = [
							inquirer.select(
											message="Select exchange account by pressing Return or Enter ",
											choices=accounts_inquirer_format+['ALL'],
							).execute()
			]
			return exchange

		def market_selector(self,exchange):

				market= self.c.marketDataApi.get_price_markets(EnumPriceSource(exchange[0].connectedPriceSource).value).result
				m2 = [
						{ 'name':f"{i.primaryCurrency}/" #{EnumPriceSource(i.priceSource).name},
								f"{i.secondaryCurrency}", "value" : i} for i in market
						]

				market = inquirer.fuzzy(message="Type tickers to search:",choices=m2).execute()
				return market

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

<<<<<<< Updated upstream
			bots.sort(key=lambda x:x.name,reverse=False)
			b2 = [{'name':f"{i.name} {i.priceMarket.primaryCurrency}-"
				f"{i.priceMarket.secondaryCurrency}, {i.roi}",'value':i} for i in bots]
=======
    def generate_client(self) -> HaasomeClient:
        # print('CM',self.config_manager.__dict__)
        return HaasomeClient(self.config_manager.ip, self.config_manager.secret)
>>>>>>> Stashed changes

			if multi != True:
				bots = inquirer.select(

						message="Select SINGLE BOT using arrow and ENTER keys",
						choices=b2,
						).execute()

				self.bot = bots
				self.bots = [self.bot]
				return bots


			else:
				bots = inquirer.select(

						message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
								"   Confirm selection using ENTER.",
						choices=b2,
						multiselect=True
						).execute()
				self.bots = bots
				return bots

		def calculate_ticks_from_bot_trades(self,bot):

			trades_df = self.trades_to_df(bot)
			first_trade = trades_df.date.iloc[0]

			delta = datetime.datetime.now() - first_trade
			delta_minutes = delta.total_seconds() / 60
			ticks = delta_minutes




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


		def select_bottype_to_create(self):
				bot_types = [{'name':e.name,"value":e.value} for e in EnumCustomBotType]
				selected_type = inquirer.select(
						message=" Select bot type to create", choices=bot_types
				).execute()
				self.bottype = selected_type


if __name__ == "__main__":
	h = Haas()
	# file = h.obj_file_selector()
	# object = h.		()
	# exchange = h.match_exchange_with_bot(object)
