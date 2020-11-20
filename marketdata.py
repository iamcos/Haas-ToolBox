from haas import Haas

import time
import pandas as pd

from haasomeapi.enums.EnumErrorCode import EnumErrorCode


from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.HaasomeClient import HaasomeClient

class MarketData(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.config = Haas().config
        self.c = HaasomeClient(self.ip, self.secret)
        self.ticks = Haas().read_ticks()

    def to_df_for_ta(self, market_history):
        """
        Transforms List of Haas MarketData into Dataframe
        """
        market_data = [
            {
                "Date": x.unixTimeStamp,
                "Open": x.open,
                "High": x.highValue,
                "Low": x.lowValue,
                "Close": x.close,
                "Buy": x.currentBuyValue,
                "Sell": x.currentSellValue,
                "Volume": x.volume,
            }
            for x in market_history
        ]
        # print(market_data)
        df = pd.DataFrame(market_data)

        try:
            df["Date"] = pd.to_datetime(df["Date"], unit="s")

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
    # @limits(calls=5, period=15)
    def get_market_data(self, priceMarketObject, interval, depth):
        """
        Returns dataframe full of candlestick data including volume in any interval and depth supported by Haasonline.

        """
        marketdata = self.c.marketDataApi.get_history_from_market(
            priceMarketObject, interval, depth
        )
        # print('get_market_data', 'errorcode', marketdata.errorCode,
        #       'errormessage', marketdata.errorMessage)
        if marketdata.errorCode == EnumErrorCode.SUCCESS:

            if type(marketdata.result) == list:
                if len(marketdata.result) > 0:
                    df = self.to_df_for_ta(marketdata.result)
                    return df
                else:
                    time.sleep(5)
                    return self.get_market_data(priceMarketObject, interval, depth)
            else:
                time.sleep(10)
                return self.get_market_data(priceMarketObject, interval, depth)
        else:
            time.sleep(10)
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

        data.rename(uppercase, axis="columns", inplace=True)
        data["Data"] = pd.to_datetime(data["Data"])
        dti = pd.DatetimeIndex([x for x in data["Date"]])
        data.set_index(dti, inplace=True)
        # print(data)
        return data