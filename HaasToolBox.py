
import inquirer
import pandas as pd

from inquirer.themes import GreenPassion

from botdb import BotDB
from flashcrashbottools import FlashCrashBot
from haas import Haas
from interactivebt import InteractiveBT as AssistedBT
from madhatter import MadHatterBot

from scalperbot import ScalperBot
from tradingviewtoolbox import TradingView
import datetime
class HaasToolBox(Haas,TradingView):
    def __init__(self):
        Haas.__init__(self)

    def main_screen(self):

        choices = [
            "Mad-Hatter Bots",
            'Flash-Crash Bots',
            'AssistedBT',
            "Scalper Bots",
            'Create bots from CSV',
            "Quit",
            ]
        loop_count = 10

        # os.system('clear')
        questions = [
            inquirer.List(
                "resp",
                "Choose action: ",
                choices=choices,
            )
        ]

      

        answers = inquirer.prompt(questions,theme=GreenPassion())


        if answers['resp'] == "Mad-Hatter Bots":
            mh = MadHatterBot()
            mh.mh_menu()

        if answers['resp'] == "Scalper Bots":
            sb = ScalperBot()
            sb.scalper_bot_menu()

        if answers['resp'] == "Flash-Crash Bots":
            fcb = FlashCrashBot()
            d = fcb.menu()
        if answers['resp'] == "AssistedBT":
            abt = AssistedBT()
            m = abt.menu()

        if answers['resp'] == "Create bots from CSV":
            multicreate_choices = ['Scalper',
                                   # 'PingPong',
                                   # 'FlashCrash'
                                   # 'Mad-Hatter',
                                   ]
    
            questions2 = [
                inquirer.List('resp','Select below: ',choices=multicreate_choices)]
            
            multicreate_answer = inquirer.prompt(questions2)['resp']
            
            if multicreate_answer == 'Mad-Hatter':
                pass
            elif multicreate_answer == 'Scalper':
                # new_bots = self.tw_to_bots(3)
                new_bots = self.tw_to_scalpers()
            elif multicreate_answer == 'PingPong':
                pass
            elif multicreate_answer == 'FlashCrash':
                pass


        if answers['resp'] == 'Quit':
            KeyboardInterrupt()

        # irrelevant answers:
        #
        # if answers['resp'] == 'AssistedBT':
        #     BT = InteractiveBT().backtest(loop_count)
        if answers['resp'] == "Select and apply config to bot":
            self.apply_configs_menu()
        if answers['resp'] == "Development Features":
            file = self.dev_features()

        if answers['resp'] == 'Loops':
            loop_count = input("Type New Loop Count: ")
            print(f"Auto BT lool count has been set to: {loop_count}")
        if answers['resp'] == 'Set BT date':
            Haas().write_date()

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
            if response["response"] == "Select Bot":
                bot = self.bot_selector()
            if response["response"] == "Select file with configs":
                file = pd.read_csv(self.file_selector())
            if response["response"] == "Apply configs":
                configs = self.config_storage(self.bot.guid).sort_values(by="roi", ascending=False)
                configs.drop_duplicates()
                configs = self.clean_df(configs)
                while True:
                    print(configs)
                    print(
                        "To apply bot type config number from the left column and hit return."
                    )
                    print("To return to the main menu, type q and hit return")
                    resp = input("Config number: ")
                   
                    if int(resp) >= 0:
                 
                        self.setup_bot_from_csv(self.bot, configs.iloc[int(resp)]
                                )
                           
                        self.bt(self.bot)
                    else:
                        break
             

            elif ind == 3:
                break


    def multiple_bot_auto_bt_menu(self):
   
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

                for b in self.bots:
                    self.bot = b
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
        bt_results = self.iterate_csv(self.configs[0:self.num_configs], b, depth=Haas().read_ticks())
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
                    i2 = self.bt(i)
                    # print(i2.__dict__)
                    # print([{x:i2.__dict__[x]} for x in i2.__dict__])

                    self.setup_bot_from_csv(i2, self.configs.iloc[c])

                    # BotDB().setup_bot_from_obj(i2,self.configs.iloc[c])
                    self.bt(i2)
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
                    i2 = self.bt(i)
                    # print(i2.__dict__)
                    # print([{x:i2.__dict__[x]} for x in i2.__dict__])

                    self.setup_bot_from_csv(i2, self.configs.iloc[c])

                    # BotDB().setup_bot_from_obj(i2,self.configs.iloc[c])
                    self.bt(i)
   


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


def main():

    mm = HaasToolBox()
    mm.main_screen()


if __name__ == '__main__':
    main()