from haasomeapi.enums.EnumIndicator import EnumIndicator
from haas import Haas
from InquirerPy import inquirer
from InquirerPy.utils import patched_print as print
from haasomeapi.apis.TradeBotApi import TradeBotApi
from InquirerPy import inquirer
from InquirerPy.separator import Separator
from InquirerPy import get_style
import time
from haasomeapi.enums.EnumIndicator import EnumIndicator
from haasomeapi.enums.EnumInsurance import EnumInsurance
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumSafety import EnumSafety
from scripts.tradebottools import TradeBotConfigManager
# from scripts.tradebotselectors import (
    # TradeBotSellectors,
# )  # previous version of selectors and new one for parameters selector is in parametersselector
from scripts.parameterselector import TradeBotEditor

def handle_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            self = args[0]
            print(e)
            return f(*args, **kw)

    return wrapper


class Trade_Bot(Haas,TradeBotEditor):
    def __init__(self):
        Haas.__init__(self)
        self.tradebot = None
        self.tradebotapi = TradeBotApi(self.ip, self.secret)
        self.selected_parameter = None
        self.step = None
        self.value = None
        self.pattern = None
        self.indicator = None
        self.safety = None
        self.insurance = None
        self.next_action = None
        self.tradebot_configs = []

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
            
                # self.tradebot_configs.append(
                #     TradeBotConfigManager().create_bot_config(tradebot=self.tradebot)
                # )
                if user_selection == "Select another Trade Bot":

                    self.tradebot = None 
                    self.tradebot = self.select_tradebot()

                if user_selection == "Select interface":
                        self.select_interface()
                if user_selection == "Quit":
                    break
    def select_interface(self):
        interface =  self.interface_selector()
        param_interfaces = self.read_interface(interface)
        param_num = []
        if param_interfaces:
            selectedInterface = self.parameter_selector(param_interfaces)
            for i, x in enumerate(param_interfaces):
                if x.title == selectedInterface.title:
                    param_num = i
            
            self.tradebot = self.iterate_parameter(interface, selectedInterface,param_num)

    def setup_indicator(self):
        setup = self.tradebotapi.setup_indicator(
            self.tradebot.guid,
            self.indicator.guid,
            self.tradebot.priceMarket,
            self.tradebot.priceMarket.primaryCurrency,
            self.tradebot.priceMarket.secondaryCurrency,
            self.tradebot.priceMarket.contractName,
            self.indicator.timer,
            self.indicator.chartType,
            self.indicator.deviation,
        )
        print(
            f"Indicator setup was a {setup.errorCode.value}, {setup.errorMessage.value}"
        )

    def add_indicator(self):

        add = self.tradebotapi.add_indicator(self.tradebot.guid, self.indicator)
        if add.result:
            print(
                "Indicator",
                EnumIndicator(self.indicator).name,
                " added to ",
                self.tradebot.name,
            )
        else:
            print("Adding indicator didn't work out")

    def remove_indicator(self, bot, indicator):
        failed = []
        try:
            add = self.c.tradeBotApi.remove_indicator(bot.guid, indicator.guid)
            if add.result:
                print(
                    "Indicator",
                    EnumIndicator(indicator).value,
                    " removed from ",
                    bot.name,
                )
            else:
                print("Removing indicator didn't work out")

        except:
            failed.append(indicator)
        return failed

    def remove_indicators(self, bot, indicator_list):
        for x in indicator_list:
            self.remove_indicator(bot, x)

    def add_multiple_indicators(self, bot, indicators):
        for x in indicators:
            self.add_indicator(bot, x)

    def add_all_indicators(self, bot):
        indicators = [x for x in range(71)]
        self.add_multiple_indicators(bot, indicators)

    def remove_all_indicators(self, bot):
        indicators = t.get_indicators(bot)
        self.remove_indicators(bot, indicators)

    def select_bot_get_indicator(self, bot):
        indicators = self.get_indicators(bot)
        indicator = self.select_indicator(indicators)
        return indicator


if __name__ == "__main__":
    tb = Trade_Bot()
    tb.menu()
