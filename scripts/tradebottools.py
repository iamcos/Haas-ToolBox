from pandas import pandas as pd
from haas import Haas
from haasomeapi.dataobjects.custombots.dataobjects.Indicator import Indicator
from haasomeapi.dataobjects.custombots.dataobjects.Safety import Safety
from haasomeapi.dataobjects.custombots.dataobjects.Insurance import Insurance


class TradeBotConfigManager:
    def __init__(self):

        self.configs_storage = []

    def define_interface(self, interface):
        """define_interface identies and returns parameters interface based on the type of input interface

        Args:
                        interface (type:interface): input interface

        Returns:
                        correct parameters interface for agiven type of Interface
        """

        if type(interface) == Indicator:
            indicatorinterface = interface.indicatorInterface
        elif type(interface) == Safety:
            indicatorinterface = interface.safetyInterface
        elif type(interface) == Insurance:
            indicatorinterface = interface.insuranceInterface
        return indicatorinterface

    def create_bot_config(self, tradebot):
        """create_bot_config creates dataframe cohtaining guid and parameters of each markte interface for tradebot and returns it

        Args:
                        tradebot (tradebot): TradeBot object

        Returns:
                        total_df: combined dataframe of individual dataframes created for each interface
        """

        dfs = []
        dicts = []

        indicators = tradebot.indicators
        safeties = tradebot.safeties
        insurances = tradebot.insurances
        bot_internals = [indicators, safeties, insurances]

        for feature in bot_internals:
            for k, v in feature.items():
                interface = self.define_interface(v)
                if len(interface) > 0:
                    interface_params = {}
                    for num, param in enumerate(interface):

                        df = pd.DataFrame(
                            data=[interface[num].value, interface[num].options],
                            columns=[interface[num].title],
                        ).T
                        # print(df)

                        dfs.append(df)
                        dicts.append(interface_params)
            total_df = pd.concat(dfs, ignore_index=True)
        total_df.name = tradebot.roi
        # print("Total dfs:", total_df.columns)
        # print('dict of bot',dicts)
        return total_df

    def tradebot_parameter_selector(self, tradebot):
        if type(v) == Indicator:
            interface = v.indicatorInterface
        elif type(v) == Safety:
            interface = v.safetyInterface

        elif type(v) == Insurance:
            interface = v.insuranceInterface
