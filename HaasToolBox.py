from InquirerPy import inquirer
import pandas as pd

from flashcrashbottools import FlashCrashBot
from haas import Haas
from interactivebt import InteractiveBT as AssistedBT
from madhatter import MadHatterBot
from tradebot import Trade_Bot
from scalperbot import ScalperBot
from tradingviewtoolbox import TradingView

# https://github.com/tmbo/questionary - inquirer analog

class HaasToolBox():
    # def __init__(self):
    #      Haas.__init__(self)

    def main_screen(self):

        choices = [
            "Mad-Hatter Bots",
            'Trade Bots',
            "Flash-Crash Bots",
            "AssistedBT",
            "Scalper Bots",
            "TradingView",
            "Quit",
        ]
        loop_count = 10


        resp = inquirer.select(
            message="Choose action: ",
            choices=choices,
        ).execute()

        if resp == "Mad-Hatter Bots":
            mh = MadHatterBot()
            mh.mh_menu()
        if resp == "Trade Bots":
            tb = Trade_Bot()
            tb.menu()
        if resp == "Scalper Bots":
            sb = ScalperBot()
            sb.scalper_bot_menu()

        if resp == "Flash-Crash Bots":
            fcb = FlashCrashBot()
            d = fcb.menu()
        if resp == "AssistedBT":
            abt = AssistedBT()
            m = abt.menu()

        if resp == "TradingView":
            tw = TradingView().main()

        if resp == "Quit":
            KeyboardInterrupt()

        if resp == "Select and apply config to bot":
            self.apply_configs_menu()

    def dev_features(self):

        resp = inquirer.select(
            "resp",
            "Select Something",
            [
                "Set Exchange",
                "Set Signals",
                "Create Scalper bots",
                "Flash Crash Bot",
                "Main Menu",
            ],
        ).execute()

        if resp == "Create Scalper bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(3)
        elif resp == "Create Mad-Hatter bots from Tradingview CSV file":
            file = pd.read_csv(self.csv_file_selector())
            new_bots = self.tw_to_bots(15, file)
        elif resp == "Create Ping-Pong bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(2)
        elif resp == "Create Order Bots bots from Tradingview CSV file":
            new_bots = self.tw_to_bots(4)
        elif resp == "Flash Crash Bot":
            fcb = FlashCrashBot()
            self.bot = fcb.menu()

    def apply_configs_menu(self):
        options = [
            "Select Bot",
            "Select file with configs",
            "Apply configs",
            "Main Menu",
        ]

        while True:
            response = inquirer.select(
                message="Select an option: ", choices=options
            ).execute()
            if response == "Select Bot":
                bot = self.bot_selector()
            if response == "Select file with configs":
                file = pd.read_csv(self.csv_file_selector())
            if response == "Apply configs":
                configs = self.config_storage(self.bot.guid).sort_values(
                    by="roi", ascending=False
                )
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

                        self.setup_bot_from_csv(self.bot, configs.iloc[int(resp)])

                        self.bt(self.bot)
                    else:
                        break

            elif ind == 3:
                break

    def multiple_bot_auto_bt_menu(self):

        while True:
            response = inquirer.select(
                message="Please chose an action:",
                choices=[
                    "Select Bots",
                    "Select config file",
                    "Set configs limit",
                    "Set create limit",
                    "Start Backtesting",
                    "Main Menu",
                ],
            ).execute()
            if response == "Select Bots":
                bot = self.multiple_bot_sellector()
            elif response == "Select config file":
                file = pd.read_csv(self.csv_file_selector())
            elif response == "Set configs limit":
                try:
                    num_configs = inquirer.text(
                        message="Type the number of configs you wish to apply from a given file: ",
                    ).execute()

                    self.num_configs = num_configs
                except ValueError:
                    print(
                        "Invalid input value for the number of configs to apply from a given file. Please type a digit:"
                    )
                    num_configs = inquirer.text(
                        message="Type the number of configs you wish to apply from a given file: ",
                    ).execute()
                    self.num_configs = num_configs

            elif response == "Set create limit":

                limit = inquirer.text(
                    message="Type how many top bots to create "
                ).execute()
                self.limit = int(limit)

            elif response == "Start Backtesting":

                for b in self.bots:
                    self.bot = b
                    self.bt(b)
                    self.create_mh_bots(b)

            elif response == "Main Menu":
                break


    def create_mh_bots(self, b):
        if self.limit > len(self.configs.index):
            self.limit == len(self.configs.index)
            print(f"create limit bigger than bots, setting it to {self.limit}")
        for c in range(self.limit):
            print(self.c)
            bl = [
                x.guid
                for x in self.c.customBotApi.get_all_custom_bots().result
                if x.botType == 15
            ]

            print(bl)
            name = f"{b.name} #{c}: {b.roi}%"
            new_bot = self.c.customBotApi.clone_custom_bot_simple(
                b.accountId, b.guid, name
            )

            print(new_bot.__dict__)
            print(new_bot.errorCode, new_bot.errorMessage)
            bl2 = [
                x.guid
                for x in self.c.customBotApi.get_all_custom_bots().result
                if x.botType == 15
            ]
            print(bl2)
            for i in bl:
                if i not in bl2:
                    print(i.guid)
                    i2 = self.bt(i)

                    self.setup_bot_from_csv(i2, self.configs.iloc[c])

                    self.bt(i2)
            name = f"{b.name} #{c}: {b.roi}%"

            new_bot = self.c.customBotApi.new_custom_bot(
                b.accountId,
                b.botType,
                name,
                b.priceMarket.primaryCurrency,
                b.priceMarket.secondaryCurrency,
                b.priceMarket.contractName,
            )
            print(new_bot.errorCode, new_bot.errorMessage)
            bl2 = [
                x.guid
                for x in self.c.customBotApi.get_all_custom_bots().result
                if x.botType == 15
            ]
            print(bl2)
            for i in bl:
                if i not in bl2:
                    print(i.guid)
                    i2 = self.bt(i)

                    self.setup_bot_from_csv(i2, self.configs.iloc[c])

                    self.bt(i)


def main():

    mm = HaasToolBox()
    mm.main_screen()


if __name__ == "__main__":
    main()
