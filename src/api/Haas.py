from configparser import ConfigParser
from typing import Any
import pandas as pd
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from InquirerPy import inquirer
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haasomeapi.HaasomeClient import HaasomeClient
from pandas.core.frame import DataFrame
from api.config_manager import ConfigManager


# TODO: Rename pass more info
class Haas:
    """
    Haasonline trading software interaction class: get bots list, market data,
    create bots and configure their parameters,
    initiate back tests and so forth can be done through this class
    """

    def __init__(self) -> None:
        self.config_parser: ConfigParser = ConfigParser()
        self.config_manager: ConfigManager = ConfigManager()

        self.bot = None
        self.bots = None
        self.bot_type = None

        self.client: HaasomeClient = self.generate_client()
        self.ticks: int = self.config_manager.read_ticks()

    def get_accounts_with_details(self) -> list:
        accounts = self.client.accountDataApi.get_all_account_details().result
        accounts_with_details = list(accounts.values())

        return accounts_with_details

    def select_exchange(self) -> list[Any]:
        accounts: list = self.get_accounts_with_details()

        name_format: str = """{EnumPriceSource(account.connectedPriceSource).name} {account.name} {EnumPlatform(
        account.platformType).name} """

        accounts_inquirer_format: list[dict[str, Any]] = [
            {
                "name": name_format.format(bot=account),
                "value": account,
            } for account in accounts
        ]

        # TODO: To know what is ALL
        accounts_inquirer_format.append({'ALL': []})

        exchange: list[Any] = [
            inquirer.select(
                message="Select exchange account by pressing Return or Enter ",
                choices=accounts_inquirer_format,
            ).execute()
        ]

        return exchange

    def get_market_selector(self, exchange) -> Any:
        markets: list = self.client.marketDataApi.get_price_markets(
            EnumPriceSource(exchange[0].connectedPriceSource).value).result
        name_format: str = """{market.primaryCurrency}/ {market.secondaryCurrency}"""

        m2: list[dict[str, str or list]] = [
            {'name': name_format.format(market=_), "value": _} for _ in markets
        ]

        markets = inquirer.fuzzy(message="Type tickers to search:", choices=m2).execute()
        return markets

    def generate_client(self) -> HaasomeClient:
        return HaasomeClient(self.config_manager.url, self.config_manager.secret)

    def select_single_bot_by_type(self, bot_type: int) -> Any:
        bots_as_choices = self._get_bots_as_choices(bot_type)

        # TODO: Separate condition for two funcs
        bots: Any = inquirer.select(
            message="Select SINGLE BOT using arrow and ENTER keys",
            choices=bots_as_choices,
        ).execute()

        self.bot = bots
        self.bots = [self.bot]

        return bots

    def select_multiple_bots_by_type(self, bot_type: int) -> Any:
        bots_as_choices = self._get_bots_as_choices(bot_type)

        bots: Any = inquirer.select(
            message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
                    "   Confirm selection using ENTER.",
            choices=bots_as_choices,
            multiselect=True
        ).execute()

        self.bots = bots
        return bots

    def _get_bots_as_choices(self, bot_type: int) -> list:
        all_custom_bots: list = self.client.customBotApi.get_all_custom_bots().result
        bots: list = [bot for bot in all_custom_bots if bot.botType == bot_type]

        bots.sort(key=lambda x: x.name, reverse=False)

        name_format: str = """{bot.name} {bot.priceMarket.primaryCurrency}-{bot.priceMarket.secondaryCurrency}"""
        bots_as_choices = [{'name': name_format.format(bot=_), 'value': _} for _ in bots]

        return bots_as_choices

    def convert_trades_to_dataframe(self, bot) -> DataFrame:
        completed_orders: list = [
            {
                "orderId": _.orderId,
                "orderStatus": _.orderStatus,
                "amountFilled": _.amountFilled,
                "orderType": _.orderType,
                "amount": _.amount,
                "price": _.price,
                "date": pd.to_datetime(_.unixAddedTime, unit="s"),
            } for _ in bot.completedOrders
        ]

        return pd.DataFrame(completed_orders)

    def select_bot_type_to_create(self):
        bot_types = [{'name': _.name, "value": _.value} for _ in EnumCustomBotType]

        selected_type = inquirer.select(
            message=" Select bot type to create", choices=bot_types
        ).execute()

        self.bot_type = selected_type

