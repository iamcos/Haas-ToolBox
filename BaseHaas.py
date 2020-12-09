import datetime
import time
from builtins import Exception

import inquirer
import pandas as pd
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from ratelimit import limits,sleep_and_retry


class MainMenu(Haas):
    def __init__(self):
        self.Haas = Haas()
        self.bot = None
        self.file = None
        self.configs = None
        self.client = self.Haas.client()
        Haas.__init__(self)

    def main_screen(self):

        choices = [
            "Scalper Bots",
            "Mad-Hatter Bots",
            "Set BT date",
            'AssistedBT',
            "Development Features",
            "Quit",
        ]
        loop_count = 10

        # os.system('clear')
        questions = [
            inquirer.List(
                "resp",
                "Select an option using keyboard up and down keys, then hit Return : ",
                choices=choices,
            )
        ]

        while True:

            answers = inquirer.prompt(questions)

            if answers['resp'] == 'AssistedBT':
                BT = InteractiveBT().backtest(loop_count)
            if answers['resp'] == "Mad-Hatter Bots":
                bt = self.multiple_bot_auto_bt_menu()

            if answers['resp'] == "Select and apply config to bot":
                self.apply_configs_menu()

            if answers['resp'] == 'Set BT date':
                Haas().write_date()

            if answers['resp'] == "Scalper Bots":
                self.scalper_bot_menu()

            if answers['resp'] == 'Loops':
                loop_count = input("Type New Loop Count: ")
                print(f"Auto BT lool count has been set to: {loop_count}")

            if answers['resp'] == "Development Features":
                file = self.dev_features()

            # if answers['resp'] =='':

            if answers['resp'] == 'Quit':
                break

    def dev_features(self):
        question = [
            inquirer.List(
                "resp",
                "Select Something",
                ["Create Scalper bots from Tradingview CSV file", 'Flash Crash Bot', "Main Menu"],
            )
        ]
        # 'Create Scalper bots from Tradingview CSV file', 'Create Mad-Hatter bots from Tradingview CSV file',
        # 'Create Ping-Pong bots from Tradingview CSV file', 'Create Order Bots bots from Tradingview CSV file'])]

        answer = inquirer.prompt(question)
        if answer["resp"] == "Create Scalper bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(3)
        elif answer["resp"] == "Create Mad-Hatter bots from Tradingview CSV file":
            file = pd.read_csv(self.file_selector())
            new_bots = self.tw_to_bots(15, file)
        elif answer["resp"] == "Create Ping-Pong bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(2)
        elif answer["resp"] == "Create Order Bots bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(4)
        elif answer["resp"] == "Flash Crash Bot":
            fcb = FlashCrashBot()
            self.bot = fcb.menu()


        elif answer["resp"] == "Create Order Bots bots from Tradingview CSV file":
            self.main_screen()
    
    def return_marketobjects_from_tradingview_csv_file(self):
        tw_df = self.format_tw_csv()
        markets = MarketData().get_all_markets()
        '''
        Merging databases into one that contains data from both
        '''
        combined_df = pd.merge(tw_df, markets, how='outer', indicator='Exist')
        combined_df = combined_df.loc[combined_df['Exist'] == 'both']

        # print(len(combined_df.index)-len(tw_df.index),'from Tradingview csv were not identified')
        missing = pd.merge(tw_df, combined_df, how='outer', indicator='Missing')
        missing = missing.loc[missing['Missing'] != 'both']

        # prints combined lisst of tickers from tw and combined db
        # print(list(zip(tw_df.sort_values(by='Ticker', ascending=False)['Ticker'].values,combined_df.sort_values(by='Ticker', ascending=False)['Ticker'].values)))
        # print('tw_df',len(tw_df),'markets',len(markets),'combined_df',len(combined_df),'missing',len(missing))
        return combined_df

    @sleep_and_retry
    @limits(calls=2, period=1)
    def tw_to_bots(self, file=None):

        markets_df = self.return_marketobjects_from_tradingview_csv_file()
        accounts_with_details = self.tw_to_haas_market_translator()
        botlist = [
            bot
            for bot in self.c.customBotApi.get_all_custom_bots().result
            if bot.botType == 3
        ]
        print(botlist)
        da = set(
            [
                x.priceSource
                for x in markets_df.marketobj.values
                if x.priceSource
                   in [a.connectedPriceSource for a in accounts_with_details]
            ]
        )

        print(da)
        for m in markets_df.marketobj.values:
            for a in accounts_with_details:
                if m.priceSource == a.connectedPriceSource:

                    try:
                        bot = self.create_bots_from_tradingview_screener(3, m, a)

                    except Exception as e:
                        print(e)
        botlist2 = self.c.customBotApi.get_all_custom_bots().result
        newbots = []
        for bot in botlist2:
            if bot not in botlist:
                self.setup_bot(bot, 3)
                newbots.append(bot)

        sb = ScalperBotClass()

        sb.bot = newbots
        sb.targetpercentage = [0.5, 5, 0.2]
        sb.safetythreshold = [1, 5, 0.2]
        sb.backtest()

    def tw_to_haas_market_translator(self):

        accounts = self.c.accountDataApi.get_all_account_details().result
        accounts_guid = list(accounts.keys())

        accounts_with_details = []
        for a in accounts_guid:
            acc = self.c.accountDataApi.get_account_details(a).result
            if acc.isSimulatedAccount:
                accounts_with_details.append(acc)
        if len(accounts_with_details) == 0:
            print("Create Simulated acoounts for markets you desire bots to be created")
            time.sleep(10)
        return accounts_with_details

    def create_bots_from_tradingview_screener(self, enumbot, market_object, account):

        newbot = self.c.customBotApi.new_custom_bot(
            account.guid,
            enumbot,
            f"TW {market_object.primaryCurrency}/{market_object.secondaryCurrency}",
            market_object.primaryCurrency,
            market_object.secondaryCurrency,
            market_object.contractName,
        )
        print(newbot.errorCode, newbot.errorMessage, 'in creation of new bot')
        print(
            f"TW {market_object.primaryCurrency}/{market_object.secondaryCurrency} has been created"
            f"ed"
        )
        return newbot.result


    

    def file_selector(self, path="."):
        files = BotDB().get_csv_files(path)
        # print(files[0:5])
        question = [
            inquirer.List("file", "Please Select file from list: ", [i for i in files])
        ]

        selection = inquirer.prompt(question)
        self.file = selection["file"]
        self.configs = BotDB().read_csv(self.file)
        return self.file







def time_limited_test_menu():
    if datetime.date.today() < datetime.date(2020, 8, 24):
        test_menu()
    else:
        print(
            "Trial has ended. Contact Cosmos directly via twitter or discord for more."
        )
        time.sleep(120)
        print("Exiting ...")
        time.sleep(5)


def test_menu():
    M = MainMenu()
    a = M.main_screen()



def scalper_test_menu():
    # sc = ScalperBot().return_scalper_bots()
    # print(sc)
    s = ScalperBotClass()
    bots = s.scalper_bot_menu()

    # ms = ScalperBot().markets_selector()


def figuring_futures():
    mm = MainMenu()

    bots = mm.c.customBotApi.get_all_custom_bots().result
    for i in bots:
        if i.botType == 15:
            print(i)
            print(EnumPriceSource(i.priceMarket.priceSource))
            markets = mm.c.marketDataApi.get_price_markets(
                i.priceMarket.priceSource
            ).result
            for market in markets:
                print(market.__dict__)

    markets = mm.c.accountDataApi.get_all_account_details().result
    ks = markets.keys()
    for i in ks:
        print(markets[i].__dict__)

if __name__ == "__main__":
    # main()
    test_menu()
