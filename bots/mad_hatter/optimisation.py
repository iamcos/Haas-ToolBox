from InquirerPy import inquirer
import pandas as pd
from haasomeapi.enums.EnumMadHatterSafeties import EnumMadHatterSafeties
from numpy.ma import arange


class Optimize:
    """Stoploss/parameter bruteforcers and useful tools are located here"""

    def set_stoploss_range(self):
        """User defined range for stoploss bruteforcer."""

        start = inquirer.text(
            message="Write stoploss range starting number: "
        ).execute()
        stop = inquirer.text(message="Write stoploss range ending number: ").execute()
        step = inquirer.text(message="Write stoploss range stepping number: ").execute()

        try:
            self.config.add_section("MH_LIMITS")
        except Exception:
            print(f'Error while adding section MH_LIMITS')

        self.config.set("MH_LIMITS", "stoploss_range_start", start)
        self.config.set("MH_LIMITS", "stoploss_range_stop", stop)
        self.config.set("MH_LIMITS", "stoploss_range_step", step)
        self.write_file()
        self.read_limits()

    def find_stoploss(self):
        """Finds stoploss within a given range unless not:
        then it keeps going untill backtesting results are as good as without it.

        How it works:
        1) Backtest bot before it with stoploss set to 0. This ROI is used as target for stoploss_range
        bruteforcer to reach.

        User sets backtesting range before hand via the menu or by editing config.ini file directly.
        """
        print(
            f"{self.bot.name} selected. Market data is being fetched, backtesting initiated..."
        )
        bt_results = []
        self.haas.client.customBotApi.set_mad_hatter_safety_parameter(
            self.bot.guid, EnumMadHatterSafeties(0), round(0, 2)
        )
        do = self.haas.client.customBotApi.backtest_custom_bot(self.bot.guid, self.read_ticks())
        expected_roi = do.result.roi
        # bt_results.append([expected_roi,0])
        print(f"Target ROI: {expected_roi}% with stoploss set to 0")
        if not self.extended_range:
            start, stop, step = self.stoploss_range
        else:
            start, stop, step = self.extended_range
        for i in arange(start, stop, step):
            self.haas.client.customBotApi.set_mad_hatter_safety_parameter(
                self.bot.guid, EnumMadHatterSafeties(0), round(i, 2)
            )

            do2 = self.haas.client.customBotApi.backtest_custom_bot(
                self.bot.guid, self.read_ticks()
            )
            bt_results.append([do2.result.roi, round(i, 2)])
            print(
                f"Current stoploss {round(i,2)} : ROI {do2.result.roi}% with {expected_roi}% set as target"
            )

        bt_results = pd.DataFrame(bt_results, columns=["roi", "stoploss"])
        bt_results.sort_values(by="roi", ascending=False, inplace=True)
        bt_results.drop_duplicates()
        bt_results.reset_index(inplace=True, drop=True)
        print("Stoploss results: ", bt_results)
        print(
            f"Best result for bot {self.bot.name,bt_results.stoploss.iloc[0]}: {bt_results.roi.iloc[0]} is O.K."
        )
        if bt_results.roi.iloc[0] >= expected_roi:
            print(
                f"Stoploss {bt_results.stoploss.iloc[0]} does not interfiere with bot performance. Will be applied"
            )
            do = self.haas.client.customBotApi.set_mad_hatter_safety_parameter(
                self.bot.guid, 0, bt_results.stoploss.iloc[0]
            )
            do = self.haas.client.customBotApi.backtest_custom_bot(
                self.bot.guid, self.read_ticks()
            )
            self.extended_range = None
        else:
            print(
                f"{bt_results.stoploss.iloc[0]} produces {bt_results.roi.iloc[0]} which is smaller than "
                f"{expected_roi}."
            )
            print("Within a given  range acceptible stoploss has not been found.")
            print(f"Expanding stoploss range by 5 steps.")
            start = stop + step
            stop = stop + step * 6
            self.extended_range = [start, stop, step]
            print(f"Stoploss search has been expanded by 5 more steps")
            self.find_stoploss()

    def bt_intervals(self):
        try:
            if self.ranges.bot.intervals.selected:
                if self.bot:

                    bot = self.bot
                    self.bt_interval(bot)

                if self.bots:
                    for bot in self.bots:
                        bot = self.bot
                        self.bt_interval(bot)
                else:
                    self.bots = [self.bot]
            else:
                print("Select Intervals first")
                self.bt_intervals()
        except Exception as e:
            print("error in bt_intervals", e)
            self.ranges.bot.intervals.selected = self.select_intervals()
            self.bt_intervals()

    def bt_interval(self, bot):
        config = self.bot_config(bot)
        intervals = self.ranges.bot.intervals.selected
        bt_results = []
        print(f"Initiating {bot.name} backtesting process...")
        rangelen = len(intervals)
        new_configs = s = pd.DataFrame(
            [config.iloc[0].tolist()] * rangelen, columns=config.columns
        )
        new_configs.interval = intervals

        configs = self.remove_already_backtested(new_configs)
        if len(configs.index):
            for i in configs.index:
                do = self.haas.client.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
                    botName=bot.name,
                    botGuid=bot.guid,
                    accountGuid=bot.accountId,
                    primaryCoin=bot.priceMarket.primaryCurrency,
                    secondaryCoin=bot.priceMarket.secondaryCurrency,
                    contractName=bot.priceMarket.contractName,
                    leverage=bot.leverage,
                    templateGuid=bot.customTemplate,
                    position=bot.coinPosition,
                    fee=bot.currentFeePercentage,
                    tradeAmountType=bot.amountType,
                    tradeAmount=bot.currentTradeAmount,
                    useconsensus=bot.useTwoSignals,
                    disableAfterStopLoss=bot.disableAfterStopLoss,
                    interval=configs.loc[int(i), "interval"],
                    includeIncompleteInterval=bot.includeIncompleteInterval,
                    mappedBuySignal=bot.mappedBuySignal,
                    mappedSellSignal=bot.mappedSellSignal,
                )
                print("interval testing", do.errorMessage, do.errorMessage)
                bt = self.haas.client.customBotApi.backtest_custom_bot(
                    bot.guid, self.read_ticks()
                )
                bot_config = self.bot_config(bt.result)
                print(
                    f'  BT result: {bt.result.roi}% with interval {configs.loc[int(i),"interval"]} minutes'
                )
                bt_results.append(bot_config)
        else:
            bt_results.append(config)
        bt_results = pd.concat(bt_results)
        bt_results2 = pd.DataFrame(bt_results)
        bt_results2.sort_values(by="roi", ascending=False, inplace=True)
        bt_results2.drop_duplicates()
        bt_results2.reset_index(inplace=True, drop=True)
        self.store_results(bt_results2)

        return bt_results

    def bt_consensus(self, bot):

        bt_results = []
        print(f"Initiating {bot.name} backtesting process...")
        for i in self.parameter["signalconsensus"]:
            do = self.haas.client.customBotApi.setup_mad_hatter_bot(  # This code sets time interval as main goalj
                botName=bot.name,
                botGuid=bot.guid,
                accountGuid=bot.accountId,
                primaryCoin=bot.priceMarket.primaryCurrency,
                secondaryCoin=bot.priceMarket.secondaryCurrency,
                contractName=bot.priceMarket.contractName,
                leverage=bot.leverage,
                templateGuid=bot.customTemplate,
                position=bot.coinPosition,
                fee=bot.currentFeePercentage,
                tradeAmountType=bot.amountType,
                tradeAmount=bot.currentTradeAmount,
                useconsensus=i,
                disableAfterStopLoss=bot.disableAfterStopLoss,
                interval=bot.interval,
                includeIncompleteInterval=bot.includeIncompleteInterval,
                mappedBuySignal=bot.mappedBuySignal,
                mappedSellSignal=bot.mappedSellSignal,
            )
            # print('interval testing',do.errorMessage,do.errorMessage)
            bt = self.haas.client.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks())
            bot_config = self.bot_config(bt.result)
            print(f"{bt.result.roi}% with consensus {i}")
            bt_results.append(bot_config)
        bt_results = pd.concat(bt_results)
        bt_results2 = pd.DataFrame(bt_results)
        bt_results2.sort_values(by="roi", ascending=False, inplace=True)
        bt_results2.reset_index(inplace=True, drop=True)
        self.store_results(bt_results2)
        return bt_results

    def backtest_bbands_length(self):
        bot = self.bots[0]
        configs = self.bot_config(bot)
        start, stop, step = self.ranges.indicators.bBands.length
        bbl_range = range(start, stop + step, step)
        rangelen = len(bbl_range)
        new_configs = s = pd.DataFrame(
            [configs.iloc[0].tolist()] * rangelen, columns=configs.columns
        )
        new_configs.bbl = bbl_range

        configs = self.remove_already_backtested(new_configs)

        for i in range(len(configs.index)):

            do = self.setup_bot_from_df(bot=self.bot, config=configs.iloc[i])
            # do = self.c.customBotApi.set_mad_hatter_indicator_parameter(
            # 		bot.guid,EnumMadHatterIndicators.BBANDS,0,int(configs.bbl.iloc[i])
            # 		)
            print(f"{bot.name} bBands Length set to {int(configs.bbl.iloc[i])}")

            # print('bBands L',do.errorCode,do.errorMessage)
            print("Now backtesting...")
            bt = self.haas.client.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks())
            # print(bt.errorCode,bt.errorMessage)
            print(f"{int(configs.bbl.iloc[i])} length ROI: {bt.result.roi} %")
            configs.loc[i, "roi"] = bt.result.roi
            configs.loc[i, "obj"] = bt.result
        self.store_results(configs)
