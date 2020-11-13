from builtins import Exception

import pandas as pd
import inquirer

from ratelimit import limits, sleep_and_retry

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
            self.bot = fcb.fcb_menu()


        elif answer["resp"] == "Create Order Bots bots from Tradingview CSV file":
            self.main_screen()

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


    def apply_configs_menu(self):
        options = [
            "Select Bot",
            "Select file with configs",
            "Apply configs",
            "Main Menu",
        ]
        config_questions = [inquirer.List("response", "Select an option: ", options)]

        while True:
            response = inquirer.prompt(config_questions)
            if response["response"] in options:
                ind = options.index(response["response"])
            if ind == 0:
                bot = self.bot_selector()
            elif ind == 1:
                file = pd.read_csv(self.file_selector())
            elif ind == 2:
                # print(self.configs)

                configs = self.configs.sort_values(by="roi", ascending=False)
                configs.drop_duplicates()
                configs.reset_index(inplace=True, drop=True)
                while True:
                    print(configs)
                    print(
                        "To apply bot type config number from the left column and hit return."
                    )
                    print("To return to the main menu, type q and hit return")
                    resp = input("Config number: ")
                    try:
                        if int(resp) >= 0:

                            BotDB().setup_bot_from_csv(
                                self.bot, configs.iloc[int(resp)]
                            )
                            # print(Haas().read_ticks)
                            BotDB().bt_bot(self.bot, Haas().read_ticks())
                        else:
                            break
                    except ValueError as e:
                        break

            elif ind == 3:
                break


    def multiple_bot_auto_bt_menu(self):
        self.num_configs = 1
        self.limit = 1
        menu = [
            inquirer.List(
                "response",
                message="Please chose an action:",
                choices=[
                    "Select Bots",
                    "Select config file",
                    "Set configs limit",
                    "Set create limit",
                    "Start Backtesting",
                    "Main Menu",
                ],
            )
        ]

        while True:
            user_response = inquirer.prompt(menu)["response"]
            if user_response == "Select Bots":
                bot = self.multiple_bot_sellector()
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



            elif user_response == "Start Backtesting":

                for b in self.bot:
                    self.bt(b)
                    self.create_mh_bots(b)

            elif user_response == "Main Menu":
                break

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
        if self.limit > len(self.configs.index):
            self.limit == len(self.configs.index)
            print(f'create limit bigger than bots, setting it to {self.limit}')
        for c in range(self.limit):
            print(self.client)
            bl = [x.guid for x in self.client.customBotApi.get_all_custom_bots().result if x.botType == 15]

            print(bl)
            name = f"{b.name} #{c}: {b.roi}%"
            new_bot = self.client.customBotApi.clone_custom_bot_simple(b.accountId, b.guid, name)
            # new_bot = self.client.customBotApi.new_custom_bot(b.accountId, b.botType, name,
            #                                                   b.priceMarket.primaryCurrency,
            #                                                   b.priceMarket.secondaryCurrency,
            #                                                   b.priceMarket.contractName)
            print(new_bot.__dict__)
            print(new_bot.errorCode, new_bot.errorMessage)
            bl2 = [x.guid for x in self.client.customBotApi.get_all_custom_bots().result if x.botType == 15]
            print(bl2)
            for i in bl:
                if i not in bl2:
                    print(i.guid
                          )
                    i2 = BotDB().bt_bot(i, 5)
                    # print(i2.__dict__)
                    # print([{x:i2.__dict__[x]} for x in i2.__dict__])

                    BotDB().setup_bot_from_csv(i2, self.configs.iloc[c])

                    # BotDB().setup_bot_from_obj(i2,self.configs.iloc[c])
                    BotDB().bt_bot(i2, Haas().read_ticks())
            name = f"{b.name} #{c}: {b.roi}%"
            # new_bot = self.client.customBotApi.clone_custom_bot_simple(b.accountId, b.guid, name).result
            new_bot = self.client.customBotApi.new_custom_bot(b.accountId, b.botType, name,
                                                              b.priceMarket.primaryCurrency,
                                                              b.priceMarket.secondaryCurrency,
                                                              b.priceMarket.contractName)
            print(new_bot.errorCode, new_bot.errorMessage)
            bl2 = [x.guid for x in self.client.customBotApi.get_all_custom_bots().result if x.botType == 15]
            print(bl2)
            for i in bl:
                if i not in bl2:
                    print(i.guid
                          )
                    i2 = BotDB().bt_bot(i, 5)
                    # print(i2.__dict__)
                    # print([{x:i2.__dict__[x]} for x in i2.__dict__])

                    BotDB().setup_bot_from_csv(i2, self.configs.iloc[c])

                    # BotDB().setup_bot_from_obj(i2,self.configs.iloc[c])
                    BotDB().bt_bot(i2, Haas().read_ticks())
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
    def multiple_bot_sellector(self):
        print("BB")
        bots = MadHatterBot().return_botlist()
        b2 = [
            (
                f"{i.name} {i.priceMarket.primaryCurrency}-{i.priceMarket.secondaryCurrency}, {i.roi}",
                i,
            )
            for i in bots
        ]
        print("BB")
        question = [
            inquirer.Checkbox(
                "bots",
                message="Select one or more bots using spacebar and then press return",
                choices=b2,
            )
        ]
        selection = inquirer.prompt(question)
        try:
            self.bot = selection["bots"]
        except TypeError:
            print("No bot has been selected, you must select one")
            self.multiple_bot_sellector()
        return selection["bots"]

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



