import json
from typing import Any
from haasomeapi.dataobjects.custombots.BaseCustomBot import BaseCustomBot

import pandas as pd
from haasomeapi.dataobjects.util.HaasomeClientResponse import HaasomeClientResponse
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from pandas.core.frame import DataFrame
from ratelimit import limits, sleep_and_retry
from sqlalchemy.util.deprecations import deprecated

import madhatter_consts
from bots.mad_hatter.finetune import FineTune
from haas import Haas
from market_data import MarketData
from menus import Menus
from optimisation import Optimize


# TODO: GO to composition
class MadHatterBot(Optimize, FineTune, Menus):

	def __init__(self):
		self.haas: Haas = Haas()
		self.stoploss_range: list[float] = []
		self.num_configs: int
		self.limit: int
		self.bot_mode: int
		self.roi_threshold: float = 0.2
		self.config_storage: dict = {}
		self.configs: dict = {}
		self.current_config = None
		self.extended_range = None
		self.selected_intervals: Any = None
		self.intervals: list[int] = madhatter_consts.intervals
		self.columns: list[str] = madhatter_consts.columns
		self.possible_profit: int
		self.ticks: int

	@sleep_and_retry
	@limits(calls=5, period=1)
	# TODO: To know botType names
	def return_bots_by_15_type(self) -> list[BaseCustomBot]:
		custom_bots = self.haas.client.customBotApi.get_all_custom_bots()
		return [x for x in custom_bots.result if x.botType == 15]

	def get_bot_config_as_dataframe(self, bot: BaseCustomBot) -> DataFrame:
		bot_dict = madhatter_consts.get_bot_dict(bot)
		df = pd.DataFrame(bot_dict, index=[0])
		return df

	def setup_bot_from_df(self, bot: Any, config: DataFrame) -> HaasomeClientResponse[BaseCustomBot]:
		self._set_safeties(bot)
		self._set_indicators(bot, config)

		return self.haas.client.customBotApi.setup_mad_hatter_bot(
			botName=bot.name,
			botGuid=bot.guid,
			accountGuid=bot.accountId,
			primaryCoin=bot.priceMarket.primaryCurrency,
			secondaryCoin=bot.priceMarket.secondaryCurrency,
			contractName=bot.priceMarket.contractName,
			leverage=bot.leverage,
			templateGuid=bot.customTemplate,
			position=bot.coinPosition,
			fee=bot.currentFeePercentage,
			tradeAmountType=bot.amountType,
			tradeAmount=bot.currentTradeAmount,
			useconsensus=bot.useTwoSignals,
			disableAfterStopLoss=bot.disableAfterStopLoss,
			interval=config.interval,
			includeIncompleteInterval=bot.includeIncompleteInterval,
			mappedBuySignal=bot.mappedBuySignal,
			mappedSellSignal=bot.mappedSellSignal,
		)

	def _set_safeties(self, bot: Any) -> None:
		safeties_config: dict[EnumMadHatterSafeties, int] = self._generate_safeties_config()

		for current_type, value in safeties_config.items():
			self.haas.client.customBotApi.set_mad_hatter_safety_parameter(
				bot.guid, current_type, value
			)

	def _set_indicators(self, bot: Any, config: DataFrame) -> None:
		indicators_config: dict[
			EnumMadHatterIndicators, list[dict[int, str or int or bool]]] = self._generate_indicators_config(config)

		for current_type, values in indicators_config.items():
			for fieldNo, value in values:
				self.haas.client.customBotApi.set_mad_hatter_indicator_parameter(
					bot.guid, current_type, fieldNo, value
				)

	def _generate_safeties_config() -> dict[EnumMadHatterSafeties, int]:
		return {
			EnumMadHatterSafeties(0): 0,
			EnumMadHatterSafeties(1): 0,
			EnumMadHatterSafeties(2): 0
		}

	def _generate_indicators_config(config: DataFrame) -> \
			dict[EnumMadHatterIndicators, list[dict[int, str or int or bool]]]:
		return {
			EnumMadHatterIndicators.BBANDS: [
				{0: int(config['bbl'])},
				{1: config['devup']},
				{2: config['devdn']},
				{3: config['mattype']},
				{5: bool(config['fcc'])},
				{6: bool(config['resetmiddle'])},
				{7: bool(config['allowmidsells'])}
			],
			EnumMadHatterIndicators.RSI: [
				{0: config['rsil']},
				{1: config['rsib']},
				{2: config['rsis']}
			],
			EnumMadHatterIndicators.MACD: []
		}

	def create_top_bots(self):
		bot = self.bot
		configs = self.config_storage[bot.guid]

		print(f"{configs=}")

		if self.limit > len(configs.index):
			self.limit = len(configs.index)

		print(f"{self.limit=}")

		for c in range(self.limit):
			name = f"{self.bot.priceMarket.primaryCurrency}/"
			f"{self.bot.priceMarket.secondaryCurrency} {c} {configs.roi.iloc[c]}% "

			self.setup_bot_from_df(bot, configs.iloc[c])
			self.haas.client.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks())
			self.haas.client.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, name)

	def prepare_configs(configs):
		configs.loc[0:-1, "obj"] = None
		configs.loc[0:-1, "roi"] = 0

		for c in configs.columns:
			if c not in madhatter_consts.cols:
				configs.drop(c, axis=1, inplace=True)

		return configs

	def check_bot_trade_amount(self, bot):
		bt = self.haas.client.customBotApi.backtest_custom_bot(bot.guid, self.ticks).result
		bot = self.set_min_trade_amount(bt)
		return bot

	def set_min_trade_amount(bot):
		for x in bot.botLogBook:
			if "Minimum trade amount: " in x:
				a = x.partition("Minimum trade amount: ")
				b = a[2].partition(". Amount decimals")
				min_trade_amount = float(b[0])
				bot.currentTradeAmount = min_trade_amount
				return bot
			else:
				return bot

	def read_limits(self):
		prefix: str = '_cfg_'
		cfg_funcs_chain: list[str] = [entry[0] for entry in MadHatterBot.__dict__.items() if prefix in entry[0]]

		for func_name in cfg_funcs_chain:
			cfg_fun = getattr(self, func_name)
			prop_name = func_name.replace(prefix, '')
			self.__dict__[prop_name] = cfg_fun()

	def get_market_data(self):
		market_data = MarketData().get_market_data(
			self.bot.priceMarket, self.bot.interval, int(self.ticks) / self.bot.interval
		)
		return market_data

	def _cfg_num_configs(self) -> int:
		return int(self.haas.config_parser["MH_LIMITS"].get("number_of_configs_to_apply"))

	def _cfg_roi_threshold(self) -> float:
		return float(self.haas.config_parser["MH_LIMITS"].get("set_acceptable_roi_threshold"))

	def _cfg_bot_mode(self) -> int:
		return int(self.haas.config_parser["MH_LIMITS"].get("set_backtesting_mode"))

	def _cfg_limit(self) -> int:
		return int(self.haas.config_parser["MH_LIMITS"].get("limit_to_create"))

	def _cfg_stoploss_range(self) -> list[float]:
		return [
			float(self.haas.config_parser["MH_LIMITS"].get("stoploss_range_start")),
			float(self.haas.config_parser["MH_LIMITS"].get("stoploss_range_stop")),
			float(self.haas.config_parser["MH_LIMITS"].get("stoploss_range_step")),
		]

	def _cfg_selected_intervals(self) -> Any:
		return json.loads(self.haas.config_parser["MH_LIMITS"].get("selected_intervals"))

	# TODO: Using only in test, remove
	@deprecated
	def create_mad_hatter_bot(self, template_bot, bot_name) -> Any:
		"""[summary]

		Args: template_bot : [One bot that will be used as a template for newly created bot. New bot will have the
		same account id, bot type, primary/secondary currency, contract] bot_name : [newly created bot name]

		Returns:
			[type]: [description]
		"""
		return self.haas.client.customBotApi.new_custom_bot(
			template_bot.accountId,
			template_bot.botType,
			bot_name,
			template_bot.priceMarket.primaryCurrency,
			template_bot.priceMarket.secondaryCurrency,
			template_bot.priceMarket.contractName,
		).result

if __name__ == "__main__":
	mh = MadHatterBot().mh_menu()
