from configparser import ConfigParser
from typing import Any
import pandas as pd
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from InquirerPy import inquirer
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.HaasomeClient import HaasomeClient
from pandas.core.frame import DataFrame
from scripts.configmanager import ConfigManager
from configsstorage import ConfigsManagment

"""
Haasonline trading software interaction class: get botlist, marketdata,
create bots and configure their parameters,
initiate backtests and so forth can be done through this class
"""
# TODO: Make SRP
# TODO: Rename pass more info
class Haas():

		def __init__(self) -> None:
			self.config_parser: ConfigParser = ConfigParser()
			self.configs_management: ConfigsManagment = ConfigsManagment()
			self.config_manager: ConfigManager = ConfigManager()

			self.bot = None
			self.bots = None

			self.client: HaasomeClient = self.generate_client()
			self.ticks: int = self.config_manager.read_ticks()

			self.config_manager.check_config()


		def get_accounts_with_details(self) -> list:
			accounts = self.client.accountDataApi.get_all_account_details().result
			accounts_with_details = list(accounts.values())

			return accounts_with_details


		def select_exchange(self) -> list[Any]:
			accounts : list = self.get_accounts_with_details()

			name_format : str = """{EnumPriceSource(.connectedPriceSource).name} {bot.name} {EnumPlatform(bot.platformType).name} """
			accounts_inquirer_format : list[dict[str, list]] = [
				{
					"name": name_format.format(bot=_),
					"value": _,
				} for _ in accounts
			]

			# TODO: To know what is ALL
			accounts_inquirer_format.append({'ALL' : []})

			exchange : list[Any] = [
				inquirer.select(
					message="Select exchange account by pressing Return or Enter ",
					choices=accounts_inquirer_format,
				).execute()
			]

			return exchange


		def get_market_selector(self, exchange) -> Any:
			markets : list = self.client.marketDataApi.get_price_markets(EnumPriceSource(exchange[0].connectedPriceSource).value).result
			name_format : str = """{market.primaryCurrency}/ {market.secondaryCurrency}"""

			m2 : list[dict[str, str | list]] = [
				{ 'name':name_format.format(market=_), "value" : _} for _ in markets
			]

			markets = inquirer.fuzzy(message="Type tickers to search:",choices=m2).execute()
			return markets


		def generate_client(self) -> HaasomeClient:
			haasomeclient = HaasomeClient(self.config_manager.ip, self.config_manager.secret)
			return haasomeclient


		def select_single_bot_by_type(self, botType: int) -> Any:
			bots_as_choices = self._get_bots_as_choices(botType)

			# TODO: Separate condition for two funcs
			bots: Any = inquirer.select(
				message="Select SINGLE BOT using arrow and ENTER keys",
				choices=bots_as_choices,
			).execute()

			self.bot = bots
			self.bots = [self.bot]

			return bots


		def select_multiple_bots_by_type(self, botType: int) -> Any:
			bots_as_choices = self._get_bots_as_choices(botType)

			bots: Any = inquirer.select(
				message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
						"   Confirm selection using ENTER.",
				choices=bots_as_choices,
				multiselect=True
			).execute()

			self.bots = bots
			return bots


		def _get_bots_as_choices(self, botType : int) -> list:
			all_custom_bots : list = self.client.customBotApi.get_all_custom_bots().result
			bots : list = [bot for bot in all_custom_bots if bot.botType == botType]

			bots.sort(key=lambda x : x.name, reverse=False)

			name_format : str = """{bot.name} {bot.priceMarket.primaryCurrency}-{bot.priceMarket.secondaryCurrency}"""
			bots_as_choices = [{'name':name_format.format(bot=_), 'value':_} for _ in bots]

			return bots_as_choices


		def convert_trades_to_dataframe(self, bot) -> DataFrame:
			completedOrders : list = [
				{
					"orderId" : _.orderId,
					"orderStatus" : _.orderStatus,
					"amountFilled" : _.amountFilled,
					"orderType" : _.orderType,
					"amount" : _.amount,
					"price" : _.price,
					"date" : pd.to_datetime(_.unixAddedTime,unit="s"),
				} for _ in bot.completedOrders
			]

			return pd.DataFrame(completedOrders)


		def select_bottype_to_create(self):
			bot_types = [{'name':_.name,"value":_.value} for _ in EnumCustomBotType]

			selected_type = inquirer.select(
				message=" Select bot type to create", choices=bot_types
			).execute()

			self.bottype = selected_type


if __name__ == "__main__":
	Haas()
