import datetime
import time

from InquirerPy import inquirer
import pandas as pd
from haasomeapi.enums.EnumFlashSpreadOptions import EnumFlashSpreadOptions
from numpy import arange

from haas import Haas


class FlashCrashBot(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.ticks = Haas().config_manager.read_ticks()
        self.bot = None
        self.pricespread = None
        self.percentageboost = None
        self.multiplyer = None
        self.multiplyer_min = None
        self.multiplyer_max = None
        self.totalbuy = None
        self.totalsell = None

    def bt(self):
        bt = self.client.customBotApi.backtest_custom_bot(self.bot.guid, self.ticks)
        orders_df = self.convert_trades_to_dataframe(bt.result)
        if bt.errorCode.value == 1021:
            for i in range(5):
                print('Market history is being loaded. Retrying in 5...')
                time.sleep(5)
                bt = self.client.customBotApi.backtest_custom_bot(
                    self.bot.guid, int(self.ticks)
                )
                if bt.errorCode.value != 1021:
                    break

        return bt.result

    def read_range(self, vars=vars):
        return [x for x in [self.config_parser["FCB_LIMITS"].get(p) for p in vars]]

    def set_total_buy(self):
        response = inquirer.text('Type Buy amount: ').execute()
        self.config_parser.set('FCB_LIMITS', 'Total_buy', response)
        self.write_file()

    def set_total_sell(self):
        response = inquirer.text('Type Sell amount: ').execute()
        self.config_parser.set('FCB_LIMITS', 'Total_sell', response)
        self.write_file()

    def setup_fcb(self, print_errors=False):
        if self.totalbuy is None:
            self.set_total_buy()
        if self.totalsell is None:
            self.set_total_sell()

        accountguid = self.bot.accountId
        botguid = self.bot.guid
        botname = self.bot.name
        primarycoin = self.bot.priceMarket.primaryCurrency
        secondarycoin = self.bot.priceMarket.secondaryCurrency
        fee = self.bot.currentFeePercentage
        baseprice = self.client.marketDataApi.get_price_ticker(
            self.bot.priceMarket.priceSource,
            self.bot.priceMarket.primaryCurrency,
            self.bot.priceMarket.secondaryCurrency,
            # self.bot.priceMarket.contractName)
            self.bot.priceMarket.contractName,
        ).result.currentBuyValue

        pricespread = self.bot.priceSpread
        priceSpreadType = EnumFlashSpreadOptions(self.bot.priceSpreadType).value
        buyamount = self.totalbuy
        sellamount = self.totalsell
        amountspread = self.bot.amountSpread
        refilldelay = self.bot.refillDelay

        percentageboost = self.bot.percentageBoost
        minpercentage = self.bot.minPercentage
        maxpercentage = self.bot.maxPercentage
        safetyenabled = self.bot.safetyEnabled
        safetytriggerlevel = self.bot.safetyTriggerLevel
        safetymovein = self.bot.safetyMoveInMarket
        safetymoveout = self.bot.safetyMoveOutMarket
        followthetrend = self.bot.followTheTrend
        followthetrendchannelrange = self.bot.followTheTrendChannelRange
        followthetrendchanneloffset = self.bot.followTheTrendChannelOffset
        followthetrendtimeout = self.bot.followTheTrendTimeout

        amounttype = self.bot.amountType

        def setup_fcb(
                accountguid=accountguid,
                botguid=botguid,
                botname=botname,
                primarycoin=primarycoin,
                secondarycoin=secondarycoin,
                fee=fee,
                baseprice=baseprice,
                priceSpreadType=priceSpreadType,
                pricespread=pricespread,
                amountspread=amountspread,
                amounttype=amounttype,
                buyamount=float(buyamount),
                sellamount=float(sellamount),
                refilldelay=refilldelay,
                safetyenabled=safetyenabled,
                safetytriggerlevel=safetytriggerlevel,
                safetymovein=safetymovein,
                safetymoveout=safetymoveout,
                followthetrend=followthetrend,
                followthetrendchannelrange=followthetrendchannelrange,
                followthetrendchanneloffset=followthetrendchanneloffset,
                followthetrendtimeout=followthetrendtimeout,
                percentageboost=percentageboost,
                minpercentage=minpercentage,
                maxpercentage=maxpercentage,
        ):
            do = self.client.customBotApi.setup_flash_crash_bot(
                accountguid=accountguid,
                botguid=botguid,
                botname=botname,
                primarycoin=primarycoin,
                secondarycoin=secondarycoin,
                fee=fee,
                baseprice=baseprice,
                priceSpreadType=priceSpreadType,
                pricespread=pricespread,
                amountspread=amountspread,
                amounttype=amounttype,
                buyamount=buyamount,
                sellamount=sellamount,
                refilldelay=refilldelay,
                safetyenabled=safetyenabled,
                safetytriggerlevel=safetytriggerlevel,
                safetymovein=safetymovein,
                safetymoveout=safetymoveout,
                followthetrend=followthetrend,
                followthetrendchannelrange=followthetrendchannelrange,
                followthetrendchanneloffset=followthetrendchanneloffset,
                followthetrendtimeout=followthetrendtimeout,
                percentageboost=percentageboost,
                minpercentage=minpercentage,
                maxpercentage=maxpercentage,
            )

            return do.result

        bt_results = []
        if self.bot.priceSpreadType <= 1:
            if self.pricespread:
                for p in arange(
                        float(self.pricespread[0]),
                        float(self.pricespread[1]),
                        float(self.pricespread[2]),
                ):
                    # print('p',p)
                    fcb_setup = setup_fcb(pricespread=round(p, 2))
                    bt = self.bt()
                    orders = bt.completedOrders
                    buy_orders = [x for x in orders if x.orderType == 1]
                    sell_orders = [x for x in orders if x.orderType == 0]

                    bt_results.append(
                        [bt.roi, bt.totalProfits, len(buy_orders), len(sell_orders), round(p, 2)]
                    )
                    print(
                        f" Spread {round(p, 2)} Total Profits: {bt.totalProfits}"
                        f" Buys: {len(buy_orders)} Sells: {len(sell_orders)}"
                    )
        df_results = pd.DataFrame(
            bt_results,
            columns=[
                "roi",
                "profits",
                'buys',
                'sells',
                "pricespread",
            ],
        )

        if self.bot.priceSpreadType == 2:
            for p in arange(
                    float(self.pricespread[0]),
                    float(self.pricespread[1]),
                    float(self.pricespread[2]),
            ):
                for b in arange(
                        float(self.percentageboost[0]),
                        float(self.percentageboost[1]),
                        float(self.percentageboost[2]),
                ):
                    resp = setup_fcb(
                        pricespread=round(p, 2), percentageboost=round(b, 2)
                    )
                    bt = self.bt()
                    bt_results.append(
                        [
                            bt.roi,
                            bt.totalProfits,
                            len(bt.completedOrders),
                            round(p, 2),
                            round(b, 2),
                        ]
                    )
                    print(
                        f"pricespread {p}, percentageboost: {b} Total "
                        f"Profits: {bt.totalProfits}"
                        f" Orders: {len(bt.completedOrders)}"
                    )
            df_results = pd.DataFrame(
                bt_results,
                columns=[
                    "roi",
                    "profits",
                    'buys',
                    'sells',
                    "pricespread",
                    "percentageboost",
                ],
            )
        if self.bot.priceSpreadType == 3:
            for multiplyer in arange(
                    float(self.multiplyer[0]),
                    float(self.multiplyer[1]),
                    float(self.multiplyer[2]),
            ):
                for min in arange(
                        float(self.multiplyer_min[0]),
                        float(self.multiplyer_min[1]),
                        float(self.multiplyer_min[2]),
                ):
                    for max in arange(
                            float(self.multiplyer_max[0]),
                            float(self.multiplyer_max[1]),
                            float(self.multiplyer_max[2]),
                    ):
                        fcb_setup = setup_fcb(
                            minpercentage=round(min, 2),
                            maxpercentage=round(max, 2),
                            percentageboost=round(multiplyer, 2),
                        )
                        bt = self.bt()
                        bt_results.append(
                            [
                                bt.roi,
                                bt.totalProfits,
                                len(bt.completedOrders),
                                round(multiplyer, 2),
                                round(min, 2),
                                round(max, 2),
                            ]
                        )
                        print(
                            f"Multiplyer {multiplyer}, min {min}, max {max} "
                            f"Total Profits:"
                            f" {bt.totalProfits}"
                            f"Orders: {len(bt.completedOrders)}"
                        )
            df_results = pd.DataFrame(
                bt_results,
                columns=[
                    "roi",
                    "profits",
                    'buys',
                    'sells',
                    "multiplyer",
                    "min",
                    "max"],
            )

        filename = (
            f'FCB_{self.bot.name.replace("/", "_")}_{datetime.date.today().month}-'
            f'{datetime.date.today().day}'
            f".csv"
        )
        df_results.sort_values(by="profits", ascending=False, inplace=True)
        df_results.drop_duplicates()
        df_results.reset_index(inplace=True, drop=True)
        df_results.to_csv(filename)
        print(df_results)
        return df_results

    def slots_to_df(self, bot):

        open_slots = [
            {
                "price": bot.slots[x]["Price"],
                "amount": bot.slots[x]["Amount"],
                "orderType": bot.slots[x]["Type"],
                "active": bot.slots[x]["ActiveSlot"],
            }
            for x in bot.slots
        ]
        # for x in self.bot.completed

        slots_df = pd.DataFrame(open_slots)
        return slots_df

    def set_price_spread_range(self):

        end = inquirer.text(message="Enter Spread End range:").execute()
        start = inquirer.text(message="Enter Spread Start range: ").execute()
        step = inquirer.text(message="Enter Step: ").execute()

        self.pricespread = [start, end, step]
        try:
            self.config_parser.add_section("FCB_LIMITS")
        except Exception as e:
            pass
        self.config_parser.set("FCB_LIMITS", "pricespread_start", self.pricespread[0])
        self.config_parser.set("FCB_LIMITS", "pricespread_end", self.pricespread[1])
        self.config_parser.set("FCB_LIMITS", "pricespread_step", self.pricespread[2])
        self.write_file()

    def set_percentage_range(self):

        start = inquirer.text(message="Enter percentage Start range: ").execute(),
        end = inquirer.text(message="Enter percentage End range:").execute(),
        step = inquirer.text(message="Enter Step: ").execute(),

        self.percentageboost = [start, end, step]
        print(self.percentageboost, self.bot)

        try:
            self.config_parser.add_section("FCB_LIMITS")
        except Exception as e:
            print(e)
        self.config_parser.set("FCB_LIMITS", "percentageboost_start", self.percentageboost[0])
        self.config_parser.set("FCB_LIMITS", "percentageboost_end", self.percentageboost[1])
        self.config_parser.set("FCB_LIMITS", "percentageboost_step", self.percentageboost[2])
        self.write_file()

    def set_multiplier_range(self):

        start = inquirer.text(message="Enter multiplyer Start range: ").execute(),
        end = inquirer.text(message="Enter multiplyer End range:").execute(),
        step = inquirer.text(message="Enter Step: ").execute()

        self.multiplyer = [start, end, step]
        print(self.multiplyer, self.bot)

        try:
            self.config_parser.add_section("FCB_LIMITS")
        except Exception as e:
            print(e)
        self.config_parser.set("FCB_LIMITS", "multiplyer_start", self.multiplyer[0])
        self.config_parser.set("FCB_LIMITS", "multiplyer_end", self.multiplyer[1])
        self.config_parser.set("FCB_LIMITS", "multiplyer_step", self.multiplyer[2])
        self.write_file()

    def set_min_range(self):

        start = inquirer.text(message="Enter min % Start range: ").execute(),
        end = inquirer.text(message="Enter min % End range:").execute(),
        step = inquirer.text(message="Enter Step: ").execute()

        self.multiplyer_min = [start, end, step]
        print(self.multiplyer_min, self.bot)

        try:
            self.config_parser.add_section("FCB_LIMITS")
        except Exception as e:
            print(e)
        self.config_parser.set("FCB_LIMITS", "multiplyer_min_start", self.multiplyer_min[0])
        self.config_parser.set("FCB_LIMITS", "multiplyer_min_end", self.multiplyer_min[1])
        self.config_parser.set("FCB_LIMITS", "multiplyer_min_step", self.multiplyer_min[2])
        self.write_file()

    def set_max_range(self):

        start = inquirer.text(message="Enter max % Start range: ").execute(),
        end = inquirer.text(message="Enter max % End range:").execute(),
        step = inquirer.text(message="Enter Step: ").execute()

        self.multiplyer_max = [start, end, step]
        print(self.multiplyer_max, self.bot)

        try:
            self.config_parser.add_section("FCB_LIMITS")
        except Exception as e:
            print(e)
        self.config_parser.set("FCB_LIMITS", "multiplyer_max_start", self.multiplyer_max[0])
        self.config_parser.set("FCB_LIMITS", "multiplyer_max_end", self.multiplyer_max[1])
        self.config_parser.set("FCB_LIMITS", "multiplyer_max_step", self.multiplyer_max[2])
        self.write_file()

    def menu(self):

        while True:
            self.read_limits()

            if self.bot is None:
                menu_items = ['Select bot', 'Quit']
                resp = inquirer.select(message='Menu:', choices=menu_items).execute()
                if resp == 'Select bot':
                    self.select_single_bot_by_type(6)
                elif resp == 'Quit':
                    break

            else:
                menu_items = ["Select another bot", 'Set Buy Amount', 'Set Sell Amount']

                if self.bot.priceSpreadType == 0 or self.bot.priceSpreadType == 1:
                    menu_items.append("Set price spread range")

                elif self.bot.priceSpreadType == 2:
                    menu_items.append("Set price spread range")
                    menu_items.append("Set percentage range")

                elif self.bot.priceSpreadType == 3:
                    menu_items.append("Set multiplier range")
                    menu_items.append("Set mib %")
                    menu_items.append("Set max %")

                menu_items.append("Set BT date")
                menu_items.append("Backtest")
                menu_items.append("Quit")

                resp = inquirer.select(message='Menu:', choices=menu_items).execute()

                if resp == "Set price spread range":
                    self.set_price_spread_range()

                if resp == "Set Buy Amount":
                    self.set_total_buy()

                if resp == "Set Sell Amount":
                    self.set_total_sell()

                if resp == "Set percentage range":
                    self.set_percentage_range()

                if resp == "Set multiplyer range":
                    self.set_multiplier_range()

                if resp == "Set mib %":
                    self.set_min_range()

                if resp == "Set max %":
                    self.set_max_range()

                if resp == "Set BT date":
                    self.write_date()

                if resp == "Backtest":
                    print(f'{self.bot.name} bot selected, backtesting procedure initiated')
                    self.setup_fcb(self.bots[0])

                if resp == "Quit":
                    break

                if resp == "Select Bot" or "Select another bot":
                    self.select_single_bot_by_type(6)


def test():
    h = FlashCrashBot()
    # print(h.__dict__)
    h.menu()


if __name__ == "__main__":
    test()