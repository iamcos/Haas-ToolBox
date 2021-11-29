from marketdata import MarketData
from tradingview_ta import Interval, TA_Handler
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
import pandas as pd

from InquirerPy import inquirer
from pprint import pprint as print
from haasomeapi.enums.EnumPlatform import EnumPlatform
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumCustomBotType import EnumCustomBotType
from haas import Haas



class TradingView(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.exchange = None
        self.signals = None
        self.accounts = None
        self.markets_to_create = None
        self.bottype = None

 

        self.accounts = self.get_accounts_with_details()


    def process_csv(self):
        csvs = self.get_csv_files()
        # print(csvs)
        selected_csv = inquirer.select(
            message="Select csv file with markets to create:", choices=csvs
        ).execute()
        csv = pd.read_csv(selected_csv)
        columns = csv.columns
        ticker = inquirer.select(
            message="Please select column with ticker or coin pair data: ",
            choices=columns,
        ).execute()
        
        signal = inquirer.select(
            message="Please select column with Buy/Sell data: ", choices=columns
        ).execute()

        signals_to_use = inquirer.select(
            message="Select Signal values to create pairs for",
            choices=csv[signal].unique(),
            multiselect=True,
        ).execute()
        markets_sorted = csv[[ticker, signal]]
        markets_sorted.reset_index(inplace=True)
        try:
            markets_sorted.rename(columns={ticker:'Ticker'},inplace=True)
        except Exception as e:
            print('No Worries, but',e,"exception has been called, which in this case isn't a problem i belibe")
        ticker = "Ticker"
        markets_sorted.drop_duplicates(subset=ticker, inplace=True)
        for i in range(len(markets_sorted.index)):
            try:
                markets_sorted.Ticker.iloc[i] = markets_sorted.Ticker.iloc[i].replace('PERP',"")   
                print(f"'{markets_sorted.Ticker.iloc[i]}',prep")
            except Exception as e:
                print('market sorted error at lines 97 in tradingviewtoolbox',e)
            try:
                markets_sorted.Ticker.iloc[i] = markets_sorted.Ticker.iloc[i].replace('2021',"")   
                print(f"'{markets_sorted.Ticker.iloc[i]}',20201")
            except Exception as e:
                print('market sorted error at lines 97 in tradingviewtoolbox',e)
        markets_to_create = markets_sorted[markets_sorted[signal].isin(signals_to_use)]
        markets_to_create.reset_index(drop=True, inplace=True)
        print(markets_to_create)
        print(markets_sorted.Ticker[0:5])
        all_markets = MarketData().get_all_markets()
        all_markets_on_selected_exchange = all_markets[
            all_markets.pricesource == self.exchange.connectedPriceSource
        ]

        print([x.contractName for x in all_markets.marketobj.to_list()][-1:-5])
        markets_on_exchange = pd.merge(
            markets_to_create,
            all_markets_on_selected_exchange,
            how="outer",
            indicator="Exist",
            on="Ticker",
        )
        print(markets_on_exchange)
        markets_on_exchange = markets_on_exchange.loc[
            markets_on_exchange["Exist"] == "both"
        ]
        markets_on_exchange.reset_index(drop=True, inplace=True)
        print(markets_on_exchange)
        print(f'{len(markets_on_exchange.index)} markets from CSV file has been identified in Haas')
        self.markets_to_create = markets_on_exchange

    def create_bots_for_selected_markets(self):
        print(self.markets_to_create)
        for i in range(len(self.markets_to_create.index)):
            try:
                newbot = self.client.customBotApi.new_custom_bot_from_market(
                    self.exchange.guid,
                    self.bottype,
                    f"TW {self.markets_to_create['marketobj'][i].primaryCurrency}/{self.markets_to_create['marketobj'][i].secondaryCurrency}",
                    self.markets_to_create["marketobj"][i]
                )
               
                # print(newbot.errorCode, newbot.errorMessage, "in creation of new bot")
                # print('NEWBOT',newbot.__dict__)
                
                
            except Exception as e:
                print(e)
    
    def setup_ping_pong_bot(self,bot):
        if EnumCustomBotType[self.bottype].value == 2:
            bot = self.client.customBotApi.setup_ping_pong_bot(self.exchange.guid, bot.guid, bot.name, bot.priceMarket.primaryCurrency, bot.priceMarket.secondaryCurrency, bot.customTemplate, bot.priceMarket.contractName, bot.leverage, bot.amountType, bot.priceMarket.minimumTradeAmout if bot.currentTradeAmount < bot.priceMarket.minimumTradeAmout else  bot.currentTradeAmount, 0, bot.priceMarket.fee, bot)
            print(bot.errorCode, bot.errorMessage)
        else:
            pass
        
    def main(self):

        self.exchange = self.select_exchange()[0]
        self.select_bottype_to_create()
        self.process_csv()
        self.create_bots_for_selected_markets()

    def get_analysis(
        self, symbol="BTCUSDT", exchange="Binance", interval=Interval.INTERVAL_1_MONTH
    ):
        analysis = TA_Handler(
            symbol=symbol, screener="crypto", exchange=exchange, interval=interval
        )

        return analysis


if __name__ == "__main__":
    TradingView().main()
