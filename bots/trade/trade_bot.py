
from haas import Haas
from InquirerPy.utils import patched_print as print
from haasomeapi.apis.TradeBotApi import TradeBotApi
from InquirerPy import inquirer
from scripts.trade_bot_editor import TradeBotEditor


class Trade_Bot(Haas, TradeBotEditor):
    def __init__(self):
        Haas.__init__(self)
        self.tradebot = None
        self.tradebotapi = TradeBotApi(self.ip, self.secret)
        self.value = None


    def menu(self):
        while True:
            if not self.tradebot:
                self.tradebot = self.select_tradebot()

            else:
                choices = [
                    "Select interface",
                    "Select another Trade Bot",
                    "Quit",
                ]
                user_selection = inquirer.select(
                    message="Select action:", choices=choices
                ).execute()

                if user_selection == "Select another Trade Bot":

                    self.tradebot = None
                    self.tradebot = self.select_tradebot()

                if user_selection == "Select interface":
                    self.select_interface()
                if user_selection == "Quit":
                    break


if __name__ == "__main__":
    tb = Trade_Bot()
    tb.menu()
