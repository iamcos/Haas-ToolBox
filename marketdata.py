import time

import pandas as pd
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from BaseHaas_orig import BotDB
from haas import Haas
from ratelimit import limits

class MarketData(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.tries = 10
        self.current_try = 0



    def to_df_for_ta(self,market_history):
        """
        Transforms List of Haas MarketData into Dataframe
        """
        market_data = [
            {
                "Date":x.unixTimeStamp,
                "Open":x.open,
                "High":x.highValue,
                "Low":x.lowValue,
                "Close":x.close,
                "Buy": x.currentBuyValue,
                "Sell": x.currentSellValue,
                "Volume": x.volume,
            }
            for x in market_history
        ]
        df = pd.DataFrame(market_data)
        
        try:
            df["Date"] = pd.to_datetime(df["Date"], unit="s")
            dti = pd.DatetimeIndex([x for x in df["Date"]])
            df.set_index(dti,inplace=True)
        except:
            print("Whops")
            # print(df)
        return df

    def get_all_markets(self):
        """
        Returns dataframe with "primarycurrency", "secondarycurrency",'pricesource','marketobj','Ticker'
        Ticker is primarycurrency, secondarycurrency in one word
        """
        markets = [
            (i.primaryCurrency, i.secondaryCurrency, i.priceSource, i)
            for i in self.c.marketDataApi.get_all_price_markets().result
        ]
        df = pd.DataFrame(
            markets,
            columns=(
                ["primarycurrency", "secondarycurrency", "pricesource", "marketobj"]
            ),
        )
        df.drop_duplicates(inplace=True, ignore_index=True)
        df["Ticker"] = df.primarycurrency.values + df.secondarycurrency.values
        return df

    def return_priceMarket_object(
            self,
            pricesource: EnumPriceSource,
            primarycoin=None,
            secondarycoin=None,
            ticker=None,
    ):
        """
        Works in one of two ways:
        1. pricesource,primarycoin,secondarycoin = marketobject
        2. pricesource, ticker = marketobject
        """

        df = self.get_all_markets()

        if ticker != None:
            marketobj = df[df["Ticker"] == ticker][
                df["pricesource"] == pricesource
                ].marketobj.values[0]
            return marketobj
        else:
            marketobj = df[df["pricesource"] == pricesource][
                df["primarycurrency"] == primarycoin
                ][df["secondarycurrency"] == secondarycoin].marketobj.values[0]
            return marketobj

    # @sleep_and_retry
    @limits(calls=5, period=15)
    def get_market_data(self, priceMarketObject, interval, depth):
        """
        Returns dataframe full of candlestick data including volume in any interval and depth supported by Haasonline.

        """
        marketdata = self.c.marketDataApi.get_history_from_market(
            priceMarketObject, int(interval), int(depth)
        )
        # print('get_market_data', 'errorcode', marketdata.errorCode,
        #       'errormessage', marketdata.errorMessage)
        if marketdata.errorCode.value == 100:

            if type(marketdata.result) == list:
                if len(marketdata.result) > 0:
                    df = self.to_df_for_ta(marketdata.result)
                    return df
                else:
                    time.sleep(5)
                    print('marketdata length is zero')
                    print(marketdata.errorMessage,marketdata.errorMessage)
                    print(marketdata.result)
                    self.current_try =+1
                    if self.tries == self.current_try:
                        self.current_try = 0
                        return None
                    return self.get_market_data(priceMarketObject, interval, depth)
            else:
                time.sleep(10)
                print('marketdata is not list')
                return self.get_market_data(priceMarketObject, interval, depth)
        else:
            time.sleep(10)
            print('marketdata is syncing')
            return self.get_market_data(priceMarketObject, interval, depth)


    
    def save_market_data_to_csv(self, marketData, marketobj):
        """
        Saves provided MarketData dataframe to CSV file in a name format provided below
        """
        filename = f"{EnumPriceSource(marketobj.priceSource).name}-{marketobj.primaryCurrency}-{marketobj.secondaryCurrency}-{len(marketData)}.csv"
        if len(marketData) > 0:
            marketData.to_csv(f"./market_data/{filename}")
            print(
                f"{EnumPriceSource(marketobj.priceSource).name} | {marketobj.primaryCurrency} | {marketobj.secondaryCurrency} sucessfuly saved to csv"
            )
            return f"sucessfully saved {filename} to market_data folder, with {len(marketData)} ticks included"
        else:
            return f"Market Data is empty. {filename} has not been saved."

    def read_csv(self, file, nrows=None):
        """
        Reads MarketData csv file into a dataframe
        """
        data = BotDB().read_csv(file, nrows=nrows)

        def uppercase(x):
            return str(x).capitalize()

        data.rename(uppercase,axis="columns",inplace=True)
        data["Date"] = pd.to_datetime(data["Date"])
        dti = pd.DatetimeIndex([x for x in data["Date"]])
        data.set_index(dti,inplace=True)
        # print(data)
        return data

    

if __name__ == "__main__":
    pass
