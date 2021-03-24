import datetime
import json
import time
import enlighten
import inquirer
import pandas as pd
from alive_progress import alive_bar
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
from inquirer.themes import GreenPassion
from ratelimit import limits,sleep_and_retry
import os
from finetune import FineTune
from haas import Haas
from marketdata import MarketData
from optimisation import Optimize
from technical_analysis_for_haas import TA
from numpy import NaN
from menus import Menus
from configsstorage import ConfigsManagment
class MadHatterBot(Haas,Optimize,FineTune,TA, Menus,ConfigsManagment):
    
    def __init__(self):
        Haas.__init__(self)
        self.stoploss_range = None
        self.num_configs = None
        self.limit = None
        self.config_storage = dict()
        self.configs = None
        self.current_config = None
        self.extended_range = None
        self.ranges = self.set_ranges()
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
    
    def create_mh(self,example_bot,name):
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
    @limits(calls=5,period=1)
    def return_botlist(self):
        bl = self.c.customBotApi.get_all_custom_bots()
        # print(bl.errorMessage)
        botlist = [x for x in bl.result if x.botType == 15]
        # print(botlist)
        return botlist
    
    def bot_config(self,bot):
        """[Generates dataframe witb bot configuration of every configurable parameter
        together with a bot object]

        Args:
            bot ([type]): [Bot to generate config from]

        Returns:
            [Dataframe]
        """        
        botdict = {
            "roi":float(bot.roi),
            "interval":int(bot.interval),
            "signalconsensus":bool(bot.useTwoSignals),
            "fcc":bool(bot.bBands["RequireFcc"]),
            "resetmiddle":bool(bot.bBands["ResetMid"]),
            "allowmidsells":bool(bot.bBands["AllowMidSell"]),
            "matype":int(bot.bBands["MaType"]),
            "rsil":int(bot.rsi["RsiLength"]),
            "rsib":float(bot.rsi["RsiOversold"]),
            "rsis":float(bot.rsi["RsiOverbought"]),
            "bbl":int(bot.bBands["Length"]),
            "devup":float(bot.bBands["Devup"]),
            "devdn":float(bot.bBands["Devdn"]),
            "macdfast":int(bot.macd["MacdFast"]),
            "macdslow":int(bot.macd["MacdSlow"]),
            "macdsign":int(bot.macd["MacdSign"]),
            "trades":int(len(bot.completedOrders)),
            "obj":bot
            }
        df = pd.DataFrame(botdict,index=[0])

        return df
    
    def set_ranges(self):
        class UtilClass:
            pass
        
        ranges = UtilClass()
        ranges.bot = UtilClass()
        ranges.indicators = UtilClass()
        ranges.safeties = UtilClass()
        
        interval = [
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
        
        signalconsensus = allowmidsells = resetmiddle = requirefcc = True,False
        
        stoploss = 0.5,5.0,0.1
        intervals = UtilClass()
        intervals.list = interval
        
        ranges.bot.intervals = intervals
        ranges.bot.signalconsensus = signalconsensus
        
        bBands = UtilClass()
        bBands.matype = 0,9,1
        bBands.length = 7,9,1
        bBands.devup = 1.0,1.2,0.1
        bBands.devdown = 1.0,1.2,0.1
        
        rsi = UtilClass()
        rsi.length = 2,21,1
        rsi.buy = 51,99,1
        rsi.sell = 2,49,1
        
        macd = UtilClass()
        macd.fast = 2,59,1
        macd.slow = 40,80,1
        macd.signal = 3,21,1
        
        ranges.indicators.bBands = bBands
        ranges.indicators.rsi = rsi
        ranges.indicators.macd = macd
        ranges.safeties.stoploss = stoploss
        
        self.ranges = ranges
        
        return ranges
    
    def setup_bot_from_df(self,bot,config,print_errors=False):
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            # this way less api calls is being made
            bot.guid,EnumMadHatterIndicators.BBANDS,0,int(config["bbl"])
            )
        if print_errors == True:
            print("bBands",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            1,
            config["devup"],
            )
        if print_errors == True:
            print("bBands",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.BBANDS,
            2,
            config["devdn"],
            )
        if print_errors == True:
            print("bBands",do.errorCode,do.errorMessage)
        
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
            print("bBands FCC",do.errorCode,do.errorMessage)
        
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
            print("bBands",do.errorCode,do.errorMessage)
        
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
            print("bBands",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.RSI,
            0,
            config["rsil"],
            )
        if print_errors == True:
            print('bool(config["fcc"]: ',bool(config["fcc"]))
            print("bBands",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.RSI,
            1,
            config["rsib"],
            )
        if print_errors == True:
            print("rsi",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,EnumMadHatterIndicators.RSI,2,config["rsis"]
            )
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            0,
            config["macdfast"],
            )
        if print_errors == True:
            print("rsi",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            1,
            config["macdslow"],
            )
        if print_errors == True:
            print("rsi",do.errorCode,do.errorMessage)
        
        do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            bot.guid,
            EnumMadHatterIndicators.MACD,
            2,
            config["macdsign"],
            )
        if print_errors == True:
            print("macd",do.errorCode,do.errorMessage)
        
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
            print("macd",do.errorCode,do.errorMessage)
        
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
            print("macd",do.errorCode,do.errorMessage)
        # print("MH FROM CSV",do.errorCode,do.errorMessage)
        updated_bot = do
        try:
            # print("updated_bot",updated_bot.errorCode,updated_bot.errorMessage)
            pass
        except Exception as e:
            print(e)
        
        return do
    
    
    def setup_bot_from_obj(self,bot,config,print_errors=False):
        
        if bot.bBands["Length"] != config.bBands["Length"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,EnumMadHatterIndicators.BBANDS,0,config.bBands["Length"]
                )
        if print_errors == True:
            print("interval",do.errorCode,do.errorMessage)
        if bot.bBands["Devup"] != config.bBands["Devup"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                1,
                config.bBands["Devup"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.bBands["Devdn"] != config.bBands["Devdn"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                2,
                config.bBands["Devdn"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.bBands["MaType"] != config.bBands["MaType"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                3,
                config.bBands["MaType"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.bBands["AllowMidSell"] != config.bBands["AllowMidSell"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                5,
                config.bBands["AllowMidSell"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.bBands["RequireFcc"] != config.bBands["RequireFcc"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                6,
                config.bBands["fcc"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.rsi["RsiLength"] != config.rsi["RsiLength"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                0,
                config.rsi["RsiLength"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.rsi["RsiOverbought"] != config.rsi["RsiOverbought"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                1,
                config.rsi["RsiOverbought"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.rsi["RsiOversold"] != config.rsi["RsiOversold"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,EnumMadHatterIndicators.RSI,2,config.rsi["RsiOversold"]
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.macd["MacdFast"] != config.macd["MacdFast"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                0,
                config.macd["MacdFast"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.macd["MacdSlow"] != config.macd["MacdSlow"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                1,
                config.macd["MacdSlow"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
        if bot.macd["MacdSign"] != config.macd["MacdSign"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                2,
                config.macd["MacdSign"],
                )
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
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
                ).result
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
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
                ).result
        if print_errors == True:
            print(do.errorCode,do.errorMessage)
    
    def bt(self):
    
        if self.num_configs > len(self.configs.index):
            self.num_configs == len(self.configs.index)
            print(
                f"config limit bigger than configs in config file, setting it to "
                f"{self.num_configs}"
                )
        print("index",self.configs.index)
        print("the configs",self.configs)
    
        unsorted_results = self.iterate_csv(self.configs[0: self.num_configs],self.bot)
        bt_results = self.save_and_sort_results(unsorted_results)
        self.store_results(bt_results)
        return bt_results
    
    def save_and_sort_results(self,bt_results,obj=True,csv=True):
        if obj:
            os.makedirs('./bt_results/',exist_ok=True)
            obj_file_name = (
                f'./bt_results/{self.bot.name.replace("/","_")}_'
                f'{datetime.date.today().month}'
                f"_{datetime.date.today().day}.obj"
            )
            objects = bt_results.obj
            objects.to_pickle(obj_file_name)
            
        if csv:
            filename = (
                str(self.bot.name.replace("/","_"))
                + str("_")
                + str(datetime.date.today().month)
                + str("-")
                + str(datetime.date.today().day)
                + str("_")
                + str(len(bt_results))
                + str(".csv")
            )
            to_csv = bt_results.drop("obj",axis=1)
            to_csv.sort_values(by="roi",ascending=False,inplace=True)
            to_csv.drop_duplicates()
            to_csv.reset_index(inplace=True,drop=True)
            to_csv.to_csv(filename)
        
        bt_results2 = bt_results.sort_values(by="roi",ascending=False)
        bt_results2.drop_duplicates()
        bt_results2.reset_index(inplace=True,drop=True)
        return bt_results2
    
    def create_top_bots(self):
        bot = self.bot
        configs = self.config_storage[bot.guid]
        print('configs',configs)
        if self.limit > len(configs.index):
            self.limit = len(configs.index)
        print('LIMIT',self.limit)
        for c in range(self.limit):
            name = f"{bot.name} {c} {configs.roi.iloc[c]}%"
            self.setup_bot_from_df(bot,configs.iloc[c],print_errors=False)
            self.c.customBotApi.backtest_custom_bot(bot.guid,self.read_ticks())
            self.c.customBotApi.clone_custom_bot_simple(bot.accountId,bot.guid,name)
    
    def iterate_csv(self,configs,bot):
        best_roi = 0
      
        
        configs.loc[0:-1,'obj'] = None
        configs.loc[0:-1,'roi'] = 0
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
                configs.drop(c,axis=1,inplace=True)
        
        bot.currentTradeAmount = 10000
        
        pbar = enlighten.Counter(total=self.num_configs, desc='Basic', unit='configs') 
        

        print("\nTop 10 configs so far:\n")
        for i in range(self.num_configs):
            try:
                
                print(
                    f"Current Backtest ROI:  {bt.roi} % 	best ROI: "
                    f"{best_roi}%."
                    )
                
            except Exception as e:
                    print(e)
            pcfg = configs.sort_values(by="roi",ascending=False).drop(
                "obj",axis=1
                )[0:10]
            print(pcfg)
            config = configs.loc[i]
            self.setup_bot_from_df(bot,config)
            bt = self.c.customBotApi.backtest_custom_bot(
                bot.guid,self.ticks
                )
            bt = bt.result
            
            if bt.roi > best_roi:
                best_roi = bt.roi
            configs.loc[i,'roi'] = bt.roi
            configs.loc[i,'obj'] = bt
            self.bot = bt
     
            pbar.update()
        print(config)
        return configs
        
    def set_configs_limit(self):
        try:
            num_configs = [
                inquirer.Text(
                    "num_configs",
                    message="Type the number of configs you wish to apply from a "
                            "given file: ",
                    )
                ]
            self.num_configs = int(
                inquirer.prompt(num_configs,theme=GreenPassion())["num_configs"]
                )
        except ValueError:
            print(
                "Invalid input value for the number of configs to apply from a given "
                "file. Please type a "
                "digit:"
                )
            num_configs = [
                inquirer.Text(
                    "num_configs",
                    message="Type the number of configs you wish to apply from a "
                            "given file: ",
                    )
                ]
        
        try:
            self.config.add_section("MH_LIMITS")
        except:
            pass
        self.config.set(
            "MH_LIMITS","number_of_configs_to_apply",str(self.num_configs)
            )
        self.write_file()
        self.read_limits()
    
    def set_create_limit(self):
        create_limit = [
            inquirer.Text("limit",message="Type a number how many top bots to create ")
            ]
        create_limit_response = inquirer.prompt(create_limit,theme=GreenPassion())[
            "limit"
        ]
        self.limit = int(create_limit_response)
        self.config.set("MH_LIMITS","limit_to_create",str(self.limit))
        self.write_file()
        self.read_limits()
    
    def read_limits(self):
        try:
            self.num_configs = int(
                self.config["MH_LIMITS"].get("number_of_configs_to_apply")
                )
        except Exception as e:
            print(e)
        
        try:
            self.limit = int(self.config["MH_LIMITS"].get("limit_to_create"))
        except Exception as e:
            print(e)
        try:
            self.stoploss_range = [
                float(self.config["MH_LIMITS"].get("stoploss_range_start")),
                float(self.config["MH_LIMITS"].get("stoploss_range_stop")),
                float(self.config["MH_LIMITS"].get("stoploss_range_step")),
                ]
        except Exception as e:
            print(e)
        try:
            self.selected_intervals = json.loads(
                self.config["MH_LIMITS"].get("selected_intervals")
                )
        except Exception as e:
            print(e)
    

    def get_first_bot(self):
        bl = self.c.customBotApi.get_all_custom_bots()
        botlist = [x for x in bl.result if x.botType == 15]
        self.bots = botlist[0:1]
        for b in self.bots:
            self.bot = b
    
    def set_configs_file(self):
        if self.configs is None:
            self.configs = pd.read_csv("./bots.csv")
     
    
    def test_bt_couple_of_bot_ranges(self):
        self.get_first_bot()
        self.set_configs_file()
        self.configs = self.configs[0:5]
        self.configs.reset_index(inplace=True,drop=True)
        self.bt()
        self.create_top_bots()
    
    def calculate_average_trade(self):

        last_trades_storage = []
        last_trades = self.c.marketDataApi.get_last_trades_from_market(
            self.bot.priceMarket
            ).result
        df = self.last_trades_to_df(self.bot,last_trades)
        print(f"Average Trade for {self.bot.priceMarket.name} is aprox {df.mean()}")
        last_trades_storage.expand(last_trades)
    
    def calculate_possible_roi(self):
        print("calculating possible profit for current bot...")
        interval = self.bot.interval
        marketdata = MarketData().get_market_data(
            self.bot.priceMarket,interval,int(self.read_ticks() / interval)
            )
        lowest = marketdata.Close.min()
        highest = marketdata.Open.max()
        idxmi = marketdata.Close.idxmin()
        
        idxma = marketdata.Open.idxmax()
        if idxmi < idxma:
            first = lowest
            second = highest
        else:
            first = idxmi
            second = idxma
        
        print(f"low: {lowest} {idxmi} - index and high: {highest} {idxma} - index")
        percentage = (float(first) / float(second)) * float(100)
        print(f"{percentage} is possible profit")
        self.possible_profit = round(percentage,2)


if __name__ == "__main__":
    mh = MadHatterBot()
    mh.create_configs_from_top_results()
    mh.mh_menu()
    
   