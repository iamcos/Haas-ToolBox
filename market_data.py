import time

import pandas as pd
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from api.Haas import Haas
from ratelimit import limits, sleep_and_retry


class MarketData(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.tries = 10
        self.current_try = 0

    def to_df_for_ta(self, market_history):
        """
        Transforms List of Haas market_data tick objects into Dataframe and returns it.
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
        df = pd.DataFrame(market_data)

        try:
            df["Date"] = pd.to_datetime(df["Date"], unit="s")
            dti = pd.DatetimeIndex([x for x in df["Date"]])
            df.set_index(dti, inplace=True)
        except:
            print("Whops")
        return df

    def get_all_markets(self):
        """
        Gets all supported by Haas market objects.
        Returns dataframe with "primarycurrency", "secondarycurrency",'pricesource','marketobj','Ticker'
        Ticker is primarycurrency, secondarycurrency joined.
        """
        markets = [
            (i.primaryCurrency, i.secondaryCurrency, i.contractName, int(i.priceSource), i)
            for i in self.client.marketDataApi.get_all_price_markets().result
        ]
        df = pd.DataFrame(
            markets,
            columns=(
                ["primarycurrency", "secondarycurrency", "contract", "pricesource", "marketobj"]
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
                ].marketobj.to_list()
            return marketobj
        else:
            marketobj = df[df["pricesource"] == pricesource][
                df["primarycurrency"] == primarycoin
                ][df["secondarycurrency"] == secondarycoin].marketobj.to_list()[0]
            return marketobj

    @sleep_and_retry
    @limits(calls=3, period=30)
    def get_market_data(self, priceMarketObject, interval, depth):
        """
        Returns dataframe full of candlestick data including volume in any interval and depth supported by Haasonline.

        """
        marketdata = self.client.marketDataApi.get_history_from_market(
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
                    print(marketdata.errorMessage, marketdata.errorMessage)
                    # print(marketdata.result)
                    self.current_try = +1
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

    def return_market_ticker(self, priceMarket):
        ticker = self.client.marketDataApi.get_price_ticker_from_market(priceMarket).result
        return ticker

    @sleep_and_retry
    @limits(calls=1, period=1)
    def last_market_trades_to_df(self, priceMarket):

        last_trades = self.client.marketDataApi.get_last_trades_from_market(priceMarket).result
        trades = [
            {

                "TradeType": x['TradeType'],
                "amount": x['Amount'],
                "price": x['Price'],
                "UnixTimestamp": pd.to_datetime(x['UnixTimestamp'], unit="s"),
            }
            for x in last_trades.lastTrades
        ]
        trades_df = pd.DataFrame(trades)
        return trades_df

    def save_market_data_to_csv(self, marketData, marketobj):
        """
        Saves provided market_data dataframe to CSV file in a name format provided below
        """
        filename = f"{EnumPriceSource(marketobj.priceSource).name}-{marketobj.primaryCurrency}-{marketobj.secondaryCurrency}-{len(marketData)}.config"
        if len(marketData) > 0:
            marketData.to_csv(f"./market_data/{filename}")
            print(
                f"{EnumPriceSource(marketobj.priceSource).name} | {marketobj.primaryCurrency} | {marketobj.secondaryCurrency} sucessfuly saved to config"
            )
            return f"sucessfully saved {filename} to market_data folder, with {len(marketData)} ticks included"
        else:
            return f"Market Data is empty. {filename} has not been saved."

    def read_csv(self, file, nrows=None):
        """
        Reads market_data config file into a dataframe
        """
        data = BotDB().read_csv(file, nrows=nrows)

        def uppercase(x):
            return str(x).capitalize()

        data.rename(uppercase, axis="columns", inplace=True)
        data["Date"] = pd.to_datetime(data["Date"])
        dti = pd.DatetimeIndex([x for x in data["Date"]])
        data.set_index(dti, inplace=True)
        return data


def main():
    md = MarketData()
    exchange = md.select_exchange()
    priceMarket = md.get_market_selector(exchange)
    while True:
        ticker = md.return_market_ticker(priceMarket)
        print(ticker.__dict__)


if __name__ == "__main__":
    main()
