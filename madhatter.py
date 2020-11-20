from numpy import arange
from haas import Haas
from ratelimit import limits, sleep_and_retry
import inquirer
import pandas as pd
from haasomeapi.HaasomeClient import HaasomeClient
from botdb import BotDB
import datetime
from haasomeapi.enums.EnumMadHatterIndicators import EnumMadHatterIndicators
class MadHatterBot(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.config = Haas().config
        self.c = HaasomeClient(self.ip, self.secret)
        self.ticks = Haas().read_ticks()
        self.stoploss_range = [0.5, 2.0, 0.2]
        self.num_configs = 5
        self.limit = 5

    def create_mh(self, input_bot, name):
        new_mad_hatter_bot = self.c.customBotApi.new_mad_hatter_bot_custom_bot(
            input_bot.accountId,
            input_bot.botType,
            name,
            input_bot.priceMarket.primaryCurrency,
            input_bot.priceMarket.secondaryCurrency,
            input_bot.priceMarket.contractName,
        )
        # print(new_mad_hatter_bot.errorCode, new_mad_hatter_bot.errorMessage)
        # print(new_mad_hatter_bot.result)
        return new_mad_hatter_bot.result

    @sleep_and_retry
    @limits(calls=3, period=2)
    def return_botlist(self):
        bl = self.c.customBotApi.get_all_custom_bots()
        # print(bl.errorMessage)
        botlist = [x for x in bl.result if x.botType == 15]
        # print(botlist)
        return botlist
    #
    # def make_bot_from_bot_config(self, config, name):
    #     botname = (
    #             str(config.priceMarket.primaryCurrency)
    #             + str(" / ")
    #             + str(config.priceMarket.secondaryCurrency)
    #             + str(" Roi ")
    #             + str(config.roi)
    #     )
    #     new_bot = self.create_mh(example_bot, botname)
    #     self.configure_mh_from_another_bot(config, new_bot)
    #     return new_bot.result

    def bruteforce_indicators(self, bot):

        d = self.bruteforce_rsi_corridor(bot)

    def bot_config(self, bot):
        botdict = {
            "roi": int(bot.roi),
            "interval": int(bot.interval),
            "signalconsensus": bool(bot.useTwoSignals),
            "resetmiddle": bool(bot.bBands["ResetMid"]),
            "allowmidsells": bool(bot.bBands["AllowMidSell"]),
            "matype": bot.bBands["MaType"],
            "fcc": bool(bot.bBands["RequireFcc"]),
            "rsil": str(bot.rsi["RsiLength"]),
            "rsib": str(bot.rsi["RsiOversold"]),
            "rsis": str(bot.rsi["RsiOverbought"]),
            "bbl": str(bot.bBands["Length"]),
            "devup": str(bot.bBands["Devup"]),
            "devdn": str(bot.bBands["Devdn"]),
            "macdfast": str(bot.macd["MacdFast"]),
            "macdslow": str(bot.macd["MacdSlow"]),
            "macdsign": str(bot.macd["MacdSign"]),
            "trades": int(len(bot.completedOrders)),
        }
        # "pricesource": EnumPriceSource(bot.priceMarket.priceSource).name,
        # "primarycoin": bot.priceMarket.primaryCurrency,
        # "secondarycoin": bot.priceMarket.secondaryCurrency,
        df = pd.DataFrame.from_dict([botdict])

        return df

    def mad_hatter_base_parameters(self):
        ranges = {}
        ranges["interval"] = [
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
        ranges["signalconsensus"] = [bool(True), bool(False)]
        ranges["resetmiddle"] = ranges["signalconsensus"]
        ranges["allowmidsells"] = ranges["signalconsensus"]
        ranges["matype"] = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        ranges["fcc"] = ranges["signalconsensus"]

        ranges["rsil"] = list(range(2, 21))
        ranges["rsib"] = list(range(2, 49))
        ranges["rsis"] = list(range(51, 99))
        ranges["bb"] = list(range(7, 60))
        ranges["devup"] = list(arange(0.1, 4.0))
        ranges["devdown"] = list(arange(0.1, 4.0))
        ranges["macdfast"] = list(range(2, 59, 2))
        ranges["macdslow"] = list(range(40, 80, 2))
        ranges["macdsign"] = list(range(3, 21, 2))
        df = pd.DataFrame(botdict, index=range(len(botdict)))
        return df

        configure = self.setup(bot, df)

    def trades_to_df(self, bot):
        if len(bot.completedOrders) > 0:
            completedOrders = [
                {
                    "orderId": x.orderId,
                    "orderStatus": x.orderStatus,
                    "orderType": x.orderType,
                    "price": x.price,
                    "amount": x.amount,
                    "amountFilled": x.amountFilled,
                    "date": pd.to_datetime(x.unixAddedTime, unit="s"),
                }
                for x in bot.completedOrders
            ]
            orders_df = pd.DataFrame(completedOrders)
            return orders_df

        else:

            completedOrders = [
                {
                    "orderId": None,
                    "orderStatus": None,
                    "orderType": None,
                    "price": None,
                    "amount": None,
                    "amountFilled": None,
                    "unixTimeStamp": datetime.datetime.today().year(),
                }
                for x in range(1)
            ]
            orders_df = pd.DataFrame(completedOrders)
        return orders_df

    # @sleep_and_retry
    # @limits(calls=3, period=2)

    def compare_indicators(self, bot, bot1):
        # print(bot.rsi, '\n',bot1.rsi)
        rsi = bot.rsi.items() == bot1.rsi.items()
        bbands = bot.bBands.items() == bot1.bBands.items()
        macd = bot.macd.items() == bot1.macd.items()
        interval = bot.interval == bot1.interval
        if rsi == True and bbands == True and macd == True and interval == True:
            return True
        else:
            # print('bot not alike')
            return False

    @sleep_and_retry
    @limits(calls=4, period=3)
    def identify_which_bot(self, ticks):
        results = []
        botlist = self.return_botlist()
        try:
            while True:

                botlist2 = self.return_botlist()
                lists = zip(botlist, botlist2)
                for x in lists:
                    if x[0].guid == x[1].guid:
                        # c = self.compare_indicators(lists[x][0], lists[x][1])
                        c = self.compare_indicators(x[0], x[1])
                        if c == False:
                            botlist = botlist2
                            # print(ticks)
                            bot = self.bt_mh_on_update(x[1], ticks)
                            results.append(bot)
                        elif c == True:
                            pass
                        else:
                            return results
        except KeyboardInterrupt:
            return results

    @sleep_and_retry
    @limits(calls=3, period=2)
    def bt_mh_on_update(self, bot, ticks):

        bt = self.c.customBotApi.backtest_custom_bot(bot.guid, int(ticks))
        if bt.errorCode != EnumErrorCode.SUCCESS:
            print("bt", bt.errorCode, bt.errorMessage)
        else:
            # print(bt.result.roi)
            # print(bt.errorCode, bt.errorMessage)
            return bt.result

            # yeid

    def return_bot(self, guid):
        bot = self.c.customBotApi.get_custom_bot(
            guid, EnumCustomBotType.BASE_CUSTOM_BOT
        ).result
        return bot

    def find_stoploss(self, bot):
        start, stop, step = self.stoploss_range
        for i in arange(start, stop, step):
            do = self.c.customBotApi.set_mad_hatter_safety_parameter(bot.guid, 0, i)
            print('sl', do.errorCode, do.errorMessage)

    def setup_bot_from_csv(self, bot, config):

        # if params differ - applies new one.
        if bot.bBands["Length"] != config["bbl"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(  # this way less api calls is being made
                bot.guid, EnumMadHatterIndicators.BBANDS, 0, config["bbl"]
            )

        if bot.bBands["Devup"] != config["devup"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                1,
                config["devup"],
            )

        if bot.bBands["Devdn"] != config["devdn"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                2,
                config["devdn"],
            )

        if bot.bBands["MaType"] != config["matype"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                3,
                config["matype"],
            )

        if bot.bBands["AllowMidSell"] != config["allowmidsells"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                5,
                config["allowmidsells"],
            )

        if bot.bBands["RequireFcc"] != config["fcc"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.BBANDS,
                6,
                config["fcc"],
            )

        if bot.rsi["RsiLength"] != config["rsil"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                0,
                config["rsil"],
            )

        if bot.rsi["RsiOverbought"] != config["rsib"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.RSI,
                1,
                config["rsib"],
            )

        if bot.rsi["RsiOversold"] != config["rsis"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid, EnumMadHatterIndicators.RSI, 2, config["rsis"]
            )

        if bot.macd["MacdFast"] != config["macdfast"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                0,
                config["macdfast"],
            )

        if bot.macd["MacdSlow"] != config["macdslow"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                1,
                config["macdslow"],
            )

        if bot.macd["MacdSign"] != config["macdsign"]:
            do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
                bot.guid,
                EnumMadHatterIndicators.MACD,
                2,
                config["macdsign"],
            )
        if bot.interval != config.interval:
            do = self.c.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
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
            print('MH FROM CSV', do.errorCode, do.errorMessage)
            return do
        # print(bot.name, ' Has been configured')
        # Indicator parameters have been set
        # calling it setup_bot_from_obj. It checks each parameter against new config.

        return do

    def bt(self, b):
        if self.num_configs > len(self.configs.index):
            self.num_configs == len(self.configs.index)
            print(f'config limit bigger than configs in config file, setting it to {self.num_configs}')
        print('index', self.configs.index)
        print('the configs', self.configs)
        bt_results = BotDB().iterate_csv(self.configs[0:self.num_configs], b, depth=Haas().read_ticks())
        filename = (
                str(b.name.replace("/", "_"))
                + str("_")
                + str(datetime.date.today().month)
                + str("-")
                + str(datetime.date.today().day)
                + str("_")
                + str(len(bt_results))
                + str("multi.csv")
        )
        bt_results.sort_values(by="roi", ascending=False, inplace=True)
        bt_results.drop_duplicates()
        bt_results.reset_index(inplace=True, drop=True)
        bt_results.to_csv(filename)
        self.configs = bt_results

    def create_mh_bots(self, b):
        botdb = BotDB()
        if self.limit > len(self.configs.index):
            self.limit == len(self.configs.index)
            print(f'create limit bigger than bots, setting it to {self.limit}')
        for c in range(self.limit):

            # print(self.c)
            bl = [x.guid for x in self.c.customBotApi.get_all_custom_bots().result if x.botType == 15]

            # print(bl)
            name = f"{b.name} {c} {b.roi}%"
            # new_bot = self.c.customBotApi.clone_custom_bot_simple(b.accountId, b.guid, name)
            new_bot = self.c.customBotApi.new_custom_bot(b.accountId, b.botType, name,
                                                              b.priceMarket.primaryCurrency,
                                                              b.priceMarket.secondaryCurrency,
                                                              b.priceMarket.contractName)
            print('New BOT CEATED', new_bot.__dict__)
            print('BOT CLONED', new_bot.errorCode, new_bot.errorMessage)
            bl2 = [x.guid for x in self.c.customBotApi.get_all_custom_bots().result if x.botType == 15]
            # print(bl2)

            for i in bl2:
                if i not in bl:
                        print('i.guid', i)
                        new_bot =self.c.customBotApi.backtest_custom_bot(i, self.ticks).result

                        # new_bot = self.c.customBotApi.backtest_custom_bot_on_market(self.bot.accountId,i,
                        #                                                                  self.ticks,
                        #            self.bot.priceMarket.primaryCurrency,
                        #            self.bot.priceMarket.secondaryCurrency,
                        #            self.bot.priceMarket.contractName).result
                        print(new_bot.guid)

                        print(self.configs)
                        b1 = self.setup_bot_from_csv(new_bot, self.configs.iloc[c])
                        print(b1.__dict__)
                        # self().setup_bot_from_obj(new_bot,self.configs.iloc[c])
                        bt = self.c.customBotApi.backtest_custom_bot(new_bot.guid, self.ticks)

                    # print(i2.__dict__)
                    # print([{x:i2.__dict__[x]} for x in i2.__dict__])




    def menu(self):

            menu = [
                inquirer.List(
                    "response",
                    message="Please chose an action:",
                    choices=[
                        'Test create',
                        "Select Bots",
                        "Select config file",
                        "Set configs limit",
                        "Set create limit",
                        "Start Backtesting",
                        "Change backtesting date",
                        "Main Menu",
                    ],
                )
            ]

            while True:
                user_response = inquirer.prompt(menu)["response"]
                if user_response == "Select Bots":
                    bot = self.bot_selector(15)
                elif user_response == "Select config file":
                    file = pd.read_csv(self.file_selector())
                elif user_response == "Set configs limit":
                    try:

                        num_configs = [
                            inquirer.Text(
                                "num_configs",
                                message="Type the number of configs you wish to apply from a given file: ",
                            )
                        ]
                        self.num_configs = int(inquirer.prompt(num_configs)["num_configs"])
                    except ValueError:
                        print(
                            "Invalid input value for the number of configs to apply from a given file. Please type a digit:"
                        )
                        num_configs = [
                            inquirer.Text(
                                "num_configs",
                                message="Type the number of configs you wish to apply from a given file: ",
                            )
                        ]
                        self.num_configs = int(inquirer.prompt(num_configs)["num_configs"])

                elif user_response == "Set create limit":
                    create_limit = [
                        inquirer.Text("limit", message="Type how many top bots to create ")
                    ]
                    create_limit_response = inquirer.prompt(create_limit)["limit"]
                    self.limit = int(create_limit_response)

                elif user_response == 'Change backtesting date':
                    self.write_date()

                elif user_response == "Start Backtesting":
                    if type(self.bot) == list:
                        for b in self.bot:
                            self.bt(b)
                            self.create_mh_bots(b)
                    else:
                        self.bt(self.bot)
                        self.create_mh_bots(self.bot)
                elif user_response == "Main Menu":
                    break

                elif user_response == 'Test create':
                    self.bot =  [x for x in self.c.customBotApi.get_all_custom_bots().result if x.botType == 15][0]
                    self.limit = 5
                    self.configs = pd.read_csv('./bots.csv')
                    self.create_mh_bots(self.bot)
if __name__ == "__main__":
    mh = MadHatterBot()
    mh.menu()