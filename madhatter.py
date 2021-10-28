import datetime
import json
import enlighten
from InquirerPy import inquirer
import pandas as pd
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from ratelimit import limits, sleep_and_retry
import os
from finetune import FineTune
from haas import Haas
from marketdata import MarketData
from optimisation import Optimize
from menus import Menus
from configsstorage import ConfigsManagment


class MadHatterBot(Haas, Optimize, FineTune, Menus, ConfigsManagment):

    def __init__(self):
        Haas.__init__(self)
        self.stoploss_range = None
        self.num_configs = None

        self.roi_threshold = 0.2

        self.config_storage = dict()
        self.configs = None
        self.current_config = None
        self.extended_range = None

        self.intervals_list = [
            1,
            2,
            3,
            4,
            5,
            6,
            10,
            12,
            15,
            20,
            30,
            45,
            60,
            90,
            120,
            150,
            180,
            240,
            300,
            600,
            1200,
            2400,
        ]
        self.columns = [
            "roi",
            "trades",
            "interval",
            "signalconsensus",
            "fcc",
            "resetmiddle",
            "allowmidsells",
            "matype",
            "rsil",
            "rsib",
            "rsis",
            "bbl",
            "devup",
            "devdn",
            "macdfast",
            "macdslow",
            "macdsign",
        ]
        self.possible_profit = None

    def create_mh(self, example_bot, name):
        """[summary]

        Args:
            example_bot : [One bot that will be used as a template for newly created bot. New bot will have the same account id,
            bot type, primary/secondary currency, contract]
            name : [newly created bot's name]

        Returns:
            [type]: [description]
        """
        new_mad_hatter_bot = self.c.customBotApi.new_custom_bot(
            example_bot.accountId,
            example_bot.botType,
            name,
            example_bot.priceMarket.primaryCurrency,
            example_bot.priceMarket.secondaryCurrency,
            example_bot.priceMarket.contractName,
        )
        return new_mad_hatter_bot.result

    @sleep_and_retry
    @limits(calls=5, period=1)
    def return_botlist(self):
        bl = self.c.customBotApi.get_all_custom_bots()
        # print(bl.errorMessage)
        botlist = [x for x in bl.result if x.botType == 15]
        # print(botlist)
        return botlist

    def bot_config(self, bot):
        """[Generates dataframe witb bot configuration of every configurable parameter
        together with a bot object]

        Args:
            bot ([type]): [Bot to generate config from]

        Returns:
            [Dataframe]
        """
        botdict = {
            "roi": float(bot.roi),
            "interval": int(bot.interval),
            "signalconsensus": bool(bot.useTwoSignals),
            "fcc": bool(bot.bBands["RequireFcc"]),
            "resetmiddle": bool(bot.bBands["ResetMid"]),
            "allowmidsells": bool(bot.bBands["AllowMidSell"]),
            "matype": int(bot.bBands["MaType"]),
            "rsil": int(bot.rsi["RsiLength"]),
            "rsib": float(bot.rsi["RsiOversold"]),
            "rsis": float(bot.rsi["RsiOverbought"]),
            "bbl": int(bot.bBands["Length"]),
            "devup": float(bot.bBands["Devup"]),
            "devdn": float(bot.bBands["Devdn"]),
            "macdfast": int(bot.macd["MacdFast"]),
            "macdslow": int(bot.macd["MacdSlow"]),
            "macdsign": int(bot.macd["MacdSign"]),
            "trades": int(len(bot.completedOrders)),
            "obj": bot,
        }
        df = pd.DataFrame(botdict, index=[0])

        return df


    def setup_bot_from_df(self, bot, config, print_errors=False):
        do = self.c.customBotApi.set_mad_hatter_safety_parameter(
            bot.guid, EnumMadHatterSafeties(0), 0
        )
        if print_errors == True:
            print("Safety", do.errorCode, do.errorMessage)
        do = self.c.customBotApi.set_mad_hatter_safety_parameter(
            bot.guid, EnumMadHatterSafeties(1), 0
        )
        if print_errors == True:
            print("Safety", do.errorCode, do.errorMessage)
        do = self.c.customBotApi.set_mad_hatter_safety_parameter(
            bot.guid, EnumMadHatterSafeties(2), 0
        )
        if print_errors == True:
            print("Safety", do.errorCode, do.errorMessage)
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            # this way less api calls is being made
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            0,
            int(config["bbl"]),
        )
        if print_errors == True:
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            1,
            config["devup"],
        )
        if print_errors == True:
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            2,
            config["devdn"],
        )
        if print_errors == True:
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            3,
            config["matype"],
        )

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            5,
            bool(config["fcc"]),
        )
        if print_errors == True:
            print("bBands FCC", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            6,
            bool(config["resetmiddle"]),
        )
        if print_errors == True:
            # print('bot.bBands["ResetMid"]','type: ',type(bot.bBands["ResetMid"]),
            # bot.bBands["ResetMid"], \
            #       'bool(config["fcc"]: ',bool(config["resetmiddle"]))
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            7,
            bool(config["allowmidsells"]),
        )
        if print_errors == True:
            # print('bot.bBands["AllowMidSell"]','type: ',type(bot.bBands[
            # "AllowMidSell"]),bot.bBands[
            # 		"AllowMidSell"],'bool(config['
            #                     '"resetmiddle"]: ',bool(config[
            # 		                                            "resetmiddle"]))
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.RSI,
            0,
            config["rsil"],
        )
        if print_errors == True:
            print('bool(config["fcc"]: ', bool(config["fcc"]))
            print("bBands", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.RSI,
            1,
            config["rsib"],
        )
        if print_errors == True:
            print("rsi", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid, EnumMadHatterIndicators.RSI, 2, config["rsis"]
        )

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            0,
            config["macdfast"],
        )
        if print_errors == True:
            print("rsi", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            1,
            config["macdslow"],
        )
        if print_errors == True:
            print("rsi", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            2,
            config["macdsign"],
        )
        if print_errors == True:
            print("macd", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.setup_mad_hatter_bot(
            # This code sets time interval
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
        if print_errors == True:
            print("macd", do.errorCode, do.errorMessage)

        do = self.c.customBotApi.setup_mad_hatter_bot(
            # This code sets time interval
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
        if print_errors == True:
            print("macd", do.errorCode, do.errorMessage)
        # print("MH FROM CSV",do.errorCode,do.errorMessage)
        updated_bot = do
        try:
            # print("updated_bot",updated_bot.errorCode,updated_bot.errorMessage)
            pass
        except Exception as e:
            print(e,'331')


        return do

    def setup_bot_from_obj(self, bot, config, print_errors=False):
        print(bot,'bot')
        if bot.bBands["Length"] != config.bBands["Length"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid, EnumMadHatterIndicators.BBANDS, 0, config.bBands["Length"]
            )
        if print_errors == True:
            print("interval", do.errorCode, do.errorMessage)
        if bot.bBands["Devup"] != config.bBands["Devup"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                1,
                config.bBands["Devup"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.bBands["Devdn"] != config.bBands["Devdn"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                2,
                config.bBands["Devdn"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.bBands["MaType"] != config.bBands["MaType"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                3,
                config.bBands["MaType"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.bBands["AllowMidSell"] != config.bBands["AllowMidSell"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                5,
                config.bBands["AllowMidSell"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.bBands["RequireFcc"] != config.bBands["RequireFcc"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                6,
                config.bBands["RequireFcc"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        print(bot.rsi)
        if bot.rsi.__dict__["rsiLength"] != config.rsi["RsiLength"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                0,
                config.rsi["RsiLength"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.rsi.__dict__["rsiOverbought"] != config.rsi["RsiOverbought"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                1,
                config.rsi["RsiOverbought"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.rsi.__dict__["rsiOversold"] != config.rsi["RsiOversold"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid, EnumMadHatterIndicators.RSI, 2, config.rsi["RsiOversold"]
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.macd.__dict__["macdFast"] != config.macd["MacdFast"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                0,
                config.macd["MacdFast"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.macd.__dict__["macdSlow"] != config.macd["MacdSlow"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                1,
                config.macd["MacdSlow"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.macd.__dict__["macdSign"] != config.macd["MacdSign"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                2,
                config.macd["MacdSign"],
            )
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.interval != config.interval:
            do = self.c.customBotApi.setup_mad_hatter_bot(
                # This code sets time interval as main goalj
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
        if print_errors == True:
            print(do.errorCode, do.errorMessage)
        if bot.useTwoSignals != config.useTwoSignals:
            do = self.c.customBotApi.setup_mad_hatter_bot(
                # This code sets time interval as main goalj
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
        if print_errors == True:
            print(do.errorCode, do.errorMessage)

    def bt(self):

        if self.num_configs > len(self.configs.index):
            self.num_configs == len(self.configs.index)
            print(
                f"config limit bigger than configs in config file, setting it to "
                f"{self.num_configs}"
            )


        unsorted_results = self.iterate_csv(
            self.configs, self.bot
        )
        bt_results = self.save_and_sort_results(unsorted_results)
        self.store_results(bt_results)
        return bt_results



    def create_top_bots(self):
        bot = self.bot
        configs = self.config_storage[bot.guid]
        print("configs", configs)
        if self.limit > len(configs.index):
            self.limit = len(configs.index)
        print("LIMIT", self.limit)
        for c in range(self.limit):
            name = f"{self.bot.priceMarket.primaryCurrency}/{self.bot.priceMarket.secondaryCurrency} {c} {configs.roi.iloc[c]}%"
            self.setup_bot_from_df(bot, configs.iloc[c], print_errors=False)
            self.c.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks())
            self.c.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, name)

    def prepare_configs(self, configs):
        configs.loc[0:-1, "obj"] = None
        configs.loc[0:-1, "roi"] = 0
        cols = [
            "interval",
            "signalconsensus",
            "fcc",
            "resetmiddle",
            "allowmidsells",
            "matype",
            "rsil",
            "rsib",
            "rsis",
            "bbl",
            "devup",
            "devdn",
            "macdfast",
            "macdslow",
            "macdsign",
            "trades",
            "roi",
            "obj",
        ]
        for c in configs.columns:
            if c not in cols:
                configs.drop(c, axis=1, inplace=True)

        return configs


    def check_bot_trade_ammount(self,bot):

        bt = self.c.customBotApi.backtest_custom_bot(bot.guid, self.ticks).result
        bot = self.set_min_trade_ammount(bt)
        return bot

    def set_min_trade_ammount(self, bot):
        for x in bot.botLogBook:
            if "Minimum trade amount: " in x:
                a = x.partition("Minimum trade amount: ")
                b = a[2].partition(". Amount decimals")
                min_trade_ammount = float(b[0])
                bot.currentTradeAmount = min_trade_ammount
                return bot
            else:
                return bot

    def iterate_csv(self, configs, bot):
        configs = self.prepare_configs(configs)
        bot = self.check_bot_trade_ammount(bot)

        configs = self.iterate_configs(configs, bot)
        return configs

    def iterate_configs(self, configs, bot):
        best_roi = 0
        if self.num_configs > len(self.configs.index):
            self.num_configs == len(self.configs.index)
        pbar = enlighten.Counter(total=self.num_configs, desc="Basic", unit="configs")
        marketdata = self.get_market_data()
        print("\nTop 10 configs so far:\n")
        for i in range(self.num_configs):
            try:
                print(f"Current Backtest ROI:  {bt.roi} % 	best ROI: " f"{best_roi}%.")

            except Exception as e:
                print(e,'exception')

            pcfg = configs.sort_values(by="roi", ascending=False).drop("obj", axis=1)[
                0:10
            ]
            print(pcfg)
            print(self.calculate_market_move_percentage(marketdata))

            config_df = configs.sample()
            i = config_df.index[0]
            config = config_df.loc[i,:]
            self.setup_bot_from_df(bot, config)

            bt = self.c.customBotApi.backtest_custom_bot(bot.guid, self.ticks)
            bt = bt.result

            if bt.roi > best_roi:
                best_roi = bt.roi
            print('config index', i)
            configs.loc[i, "roi"] = bt.roi
            configs.loc[i, "obj"] = bt
            self.bot = bt

            pbar.update()

            # if self.bt_mode == 1:
            #     if  self.possible_profit*self.roi_threshold<=best_roi:
            #         break
            # else:
            #     pass
        return configs

    def set_configs_limit(self):

        self.num_configs = inquirer.text(
            message="Type the number of configs you wish to apply from a "
            "given file: ",
        ).execute()
        try:
            self.config.add_section("MH_LIMITS")
        except Exception as e:
            print(e,'exception')
        self.config.set(
            "MH_LIMITS", "number_of_configs_to_apply", str(self.num_configs)
        )
        self.write_file()
        self.read_limits()

    def set_acceptable_roi_threshold(self):
        print('\n  What is ROI threshold?: ')
        print('\n    You can now define acceptible BT result')
        print('    by setting backtesting goal as % of market growth over')
        print('    the backtesting period.')
        print('    Write 0.9 to set it to 90% \n    backtesting will stop after ROI hits 90% of market growth over BT period\n')
        print("    0.1 is 10%, 1 is 100%\n")
        self.roi_threshold = inquirer.text(
            message="Write: ",
        ).execute()
        try:
            self.config.add_section("MH_LIMITS")
        except Exception as e:
            print(e,'exception')
        self.config.set(
            "MH_LIMITS", "set_acceptable_roi_threshold", str(self.roi_threshold)
        )
        self.write_file()
        self.read_limits()

    def set_backtesting_mode(self):
        print('\n     Two BT methods:')
        print('\n  Backtesting mode 0 does not care about threshold')
        print('  or negative price change over BT period')
        print('  Configs are fed in the same order as in file\n')
        print('  Mode 1 will stop backtesting if coin price ')
        print('  fell over the course of backtestng period')
        print('  or if backtesting results are within threshold\n')
        print('  configs are now selected at random and applied')
        self.bt_mode = int(inquirer.text(
            message="Type 0 for ordered or 1 for random config selection: ",
        ).execute())
        try:
            self.config.add_section("MH_LIMITS")
        except Exception as e:
            print(e,'exception')
        self.config.set(
            "MH_LIMITS", "set_backtesting_mode", str(self.bt_mode)
        )
        self.write_file()
        self.read_limits()

    def set_create_limit(self):
        self.limit = inquirer.text(
            message="Type a number how many top bots to create "
        ).execute()
        self.config.set("MH_LIMITS", "limit_to_create", str(self.limit))
        self.write_file()
        self.read_limits()

    def read_limits(self):
        try:
            self.num_configs = int(
                self.config["MH_LIMITS"].get("number_of_configs_to_apply")
            )
        except Exception as e:
            print(e,'exception')
        try:
            self.roi_threshold = float(
                self.config["MH_LIMITS"].get("set_acceptable_roi_threshold")
            )
        except Exception as e:
            print(e,'exception')
        try:
            self.bt_mode = int(
                self.config["MH_LIMITS"].get("set_backtesting_mode")
            )
        except Exception as e:
            print(e,'exception')

        try:
            self.limit = int(self.config["MH_LIMITS"].get("limit_to_create"))
        except Exception as e:
            print(e,'exception')
        try:
            self.stoploss_range = [
                float(self.config["MH_LIMITS"].get("stoploss_range_start")),
                float(self.config["MH_LIMITS"].get("stoploss_range_stop")),
                float(self.config["MH_LIMITS"].get("stoploss_range_step")),
            ]
        except Exception as e:
            print(e,'exception')
        try:
            self.selected_intervals = json.loads(
                self.config["MH_LIMITS"].get("selected_intervals")
            )
        except Exception as e:
            print(e,'exception')


    def get_market_data(self):
        marketdata = MarketData().get_market_data(
            self.bot.priceMarket, self.bot.interval, int(self.ticks)/self.bot.interval
        )
        return marketdata

    def calculate_market_move_percentage(self, marketdata):

        lowest = marketdata.Close.min()
        highest = marketdata.Open.max()
        idxmi = marketdata.Close.idxmin()
        idxma = marketdata.Open.idxmax()

        if idxmi < idxma:
            first = highest
            second = lowest
            percentage = (first - second) / first * 100
            print(f"low: {idxmi.strftime('%x %X')}—{lowest} high: {idxma.strftime('%x %X')}—{highest} Growth: {round(percentage, 2)}%")
        else:
            first = lowest
            second = highest
            percentage = (first - second) / first * 100
            print(f"high: {idxma.strftime('%x %X')}—{highest} low: {idxmi.strftime('%x %X')}:{lowest} Fall: {round(percentage, 2)}%")


        print(f"{round(percentage, 2)}% is max price change over bt period")
        self.possible_profit = round(percentage, 2)



if __name__ == "__main__":
    mh = MadHatterBot().mh_menu()
