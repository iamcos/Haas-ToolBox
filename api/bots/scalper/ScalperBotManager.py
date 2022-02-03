import datetime

from InquirerPy import inquirer
import numpy as np
import pandas as pd
from alive_progress import alive_bar

from tqdm import tqdm

from api.Haas import Haas


class ScalperBotManager(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.ticks = self.read_ticks()
        self.safetythreshold = ["", "", ""]
        self.targetpercentage = ["", "", ""]

    def return_scalper_bots(self):
        bl = self.client.customBotApi.get_all_custom_bots().result
        bot_list = [x for x in bl if x.botType == 3]
        return bot_list

    def setup_scalper_bot(self, bot, targetpercentage, safetythreshold):

        do = self.client.customBotApi.setup_scalper_bot(
            accountguid=bot.accountId,
            botguid=bot.guid,
            botname=bot.name,
            primarycoin=bot.priceMarket.primaryCurrency,
            secondarycoin=bot.priceMarket.secondaryCurrency,
            templateguid=bot.customTemplate,
            contractname=bot.priceMarket.contractName,
            leverage=bot.leverage,
            amountType=bot.amountType,
            tradeamount=bot.currentTradeAmount,
            position=bot.coinPosition,
            fee=bot.currentFeePercentage,
            targetpercentage=targetpercentage,
            safetythreshold=safetythreshold,
        )
        print('result: ', do.errorCode, do.errorMessage)
        return do.result

    def set_target_percentage_range(self):
        start = inquirer.text(
            message="Define start of the target percentage range",

        ).execute()
        end = inquirer.text(message="Define end of the target percentage range",
                            ).execute()
        step = inquirer.text(
            message="Define number of steps between start and end",
        ).execute()

        self.targetpercentage = [start, end, step]

    def set_safetythreshold_range(self):
        start = inquirer.text(
            message="Define start of the safety threshold range", ).execute()
        end = inquirer.text(
            message="Define end of the safety threshold range", ).execute()
        step = inquirer.text(
            message="Define number of steps between start and end",
        ).execute()

        self.safetythreshold = [start, end, step]

    def bt_date_to_unix(self):
        min = self.config_parser["BT DATE"].get("min")
        hour = self.config_parser["BT DATE"].get("hour")
        day = self.config_parser["BT DATE"].get("day")
        month = self.config_parser["BT DATE"].get("month")
        year = self.config_parser["BT DATE"].get("year")
        btd = datetime.datetime(int(year), int(
            month), int(day), int(hour), int(min))
        return btd

    def backtest(self):
        safety_combinations = list(np.arange(
            float(self.safetythreshold[0]),
            float(self.safetythreshold[1]),
            float(self.safetythreshold[2]),
        ))
        target_combinations = list(np.arange(
            float(self.targetpercentage[0]),
            float(self.targetpercentage[1]),
            float(self.targetpercentage[2]),
        ))
        total_combs = len(safety_combinations) * len(target_combinations)
        btd = self.bt_date_to_unix()
        if self.bots is not None:
            for bot in self.bots:
                self.bot = bot
                with alive_bar(total_combs, title=f"{self.bot.name} backtesting. ") as bar:
                    results = []
                    columns = ["roi", "safetythreshold", "targetpercentage"]

                    for s in tqdm(
                            np.arange(
                                float(self.safetythreshold[0]),
                                float(self.safetythreshold[1]),
                                float(self.safetythreshold[2]),
                            )
                    ):

                        for t in tqdm(
                                np.arange(
                                    float(self.targetpercentage[0]),
                                    float(self.targetpercentage[1]),
                                    float(self.targetpercentage[2]),
                                )
                        ):

                            self.setup_scalper_bot(
                                bot,
                                targetpercentage=round(t, 2),
                                safetythreshold=round(s, 2),
                            )

                            bt_result = self.client.customBotApi.backtest_custom_bot(
                                bot.guid, self.read_ticks()
                            ).result

                            try:
                                print("ROI: ", bt_result.roi, round(t, 2))
                                total_results = {
                                    "roi": bt_result.roi,
                                    "targetpercentage": round(t, 2),
                                    "safetythreshold": round(s, 2),
                                }

                                results.append(
                                    [bt_result.roi, round(t, 2), round(s, 2)]
                                )
                            except Exception as e:
                                print('backtesting error: ', e)

                    df_res = pd.DataFrame(
                        results, columns=columns, index=range(len(results))
                    )
                    df_res.sort_values(by="roi", ascending=False, inplace=True)
                    df_res.reset_index(inplace=True, drop=True)
                    # print(df_res)
                    self.setup_scalper_bot(
                        bot,
                        df_res.safetythreshold.iloc[0],
                        df_res.targetpercentage.iloc[0],
                    )

                    self.client.customBotApi.backtest_custom_bot(
                        bot.guid, self.read_ticks())
        else:
            self.select_multiple_bots_by_type(3)

    def menu(self):
        while True:
            user_response = inquirer.select(
                message="Please chose an action:",
                choices=[
                    "Select bots",
                    "Set range for safety threshold",
                    "Set range for target percentage",
                    "Backtest",
                    "backtest every bot",
                    "Change backtesting date",
                    'Populate with bots',
                    "Main menu",
                ],
            ).execute()
            if user_response == "Select bots":
                self.select_multiple_bots_by_type(3)
            elif user_response == "Set range for safety threshold":
                self.set_safetythreshold_range()
            elif user_response == "Set range for target percentage":
                self.set_target_percentage_range()
            elif user_response == "Change backtesting date":
                self.write_date()
            elif user_response == 'Populate with bots':
                self.populate_virtual_wallet()

            elif user_response == "Backtest":
                self.backtest()
            elif user_response == "backtest every bot":
                sb = ScalperBotManager()
                sb.bot = self.client.customBotApi.get_all_custom_bots().result

                sb.backtest()
            elif user_response == "Main menu":
                break

    def populate_virtual_wallet(self):
        accounts = self.client.accountDataApi.get_all_account_details().result
        a = [(f"{accounts[i].name},{accounts[i].isSimulatedAccount}-",
              accounts[i]) for i in accounts]

        self.accounts = inquirer.select(
            message="Select markets", choices=a).execute()

        self.markets_selector()
        print(self.accounts)
        for i in self.accounts:
            for m in self.markets:
                try:
                    self.client.customBotApi.new_custom_bot(
                        accountguid=i,
                        bottype=3,
                        botname=f'{m.primaryCurrency} {m.secondaryCurrency}',
                        primarycoin=m.primaryCurrency,
                        secondarycoin=m.secondaryCurrency,
                        contractname=m.contractName)

                except Exception as e:
                    print(e, i)