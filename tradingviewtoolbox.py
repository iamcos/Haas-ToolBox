from scalperbot import ScalperBot
from marketdata import MarketData
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
import pandas as pd
from haas import Haas

class TradingView:
    def __init__(self):
        Haas.__init__(self)
        
        
    def tw_to_haas_market_translator(self):
        accounts = self.c.accountDataApi.get_all_account_details().result
        accounts_guid = list(accounts.keys())

        accounts_with_details = []
        for a in accounts_guid:
            acc = self.c.accountDataApi.get_account_details(a).result
            # if acc.isSimulatedAccount:
            # 	if len(accounts_with_details) == 0:
            # 	print("Create Simulated acoounts for markets you desire bots to be created")
            # time.sleep(10)
            accounts_with_details.append(acc)
        
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
        print(newbot.errorCode, newbot.errorMessage, "in creation of new bot")
        print(
            f"TW {market_object.primaryCurrency}/{market_object.secondaryCurrency} "
            f"has been created"
            f"ed"
        )
        return newbot.result

    def csv_to_marketobjects(self):
        tw_df = self.format_tw_csv()
        markets = MarketData().get_all_markets()
        """
		Merging databases into one that contains data from both
		"""
        print(tw_df, markets)
        
        combined_df = pd.merge(tw_df, markets, how="outer", indicator="Exist", on='Ticker')
        print('Before',combined_df[:5])
        combined_df = combined_df.loc[combined_df["Exist"] == "both"]
        combined_df = combined_df[['Ticker','primarycurrency','secondarycurrency','pricesource_y','marketobj']]
        combined_df = combined_df.rename(columns ={'pricesource_y':'pricesource'})
        print('after',combined_df[:5],f'totalling {len(combined_df.index)} pairs')
       

        return combined_df

    def format_tw_csv(self):
        csv_columns = [
            "Ticker",
            "Coin",
            "primarycoin",
            "secondarycoin",
            "Exchange",
            "Market",
            "primarycurrency",
            "secondarycurrency",
        ]

        tw2 = pd.DataFrame()
        tw = pd.read_csv(self.file_selector("./autocreate"))
        

        priceSources = []

        for i in ["Ticker", "ticker"]:
            if i in tw.columns:
                tw2["Ticker"] = tw[i]
                try:
                    if "Exchange".lower() or "Exchange" in tw.columns:
                        Exchange = tw["Exchange"].values
                    
                except Exception as e:
                    print(e, f"No Exchange in file.It will be selected at a later step.")
                    tw2["Exchange"] = None
                    for i in tw2["Exchange"]:
                        try:
                            priceSources.append(EnumPriceSource[i].value)
                        except Exception as e:
                            print(e, "format_tw_csv")
                            priceSources.append(None)
            
            tw2["pricesource"] = priceSources

            return tw2

    def tw_to_scalpers(self, file=None):

        markets_df = self.csv_to_marketobjects()
        accounts_with_details = self.tw_to_haas_market_translator()
        print("Accounts with details:", accounts_with_details)
        botlist = [
            bot
            for bot in self.c.customBotApi.get_all_custom_bots().result
            if bot.botType == 3
        ]
        # print(botlist)
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

                newbots.append(bot)

        sb = ScalperBot()

        sb.bot = newbots
        self.read_limits()
        sb.backtest()
