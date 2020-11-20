import pandas as pd
import inquirer
from haas import Haas
class ScalperBotClass(Haas):
    def __init__(self):
        Haas.__init__(self)

        self.safetythreshold = [1, 5, 0.2]
        self.targetpercentage = [1, 3, 0.1]

    def return_scalper_bots(self):

        bl = self.c.customBotApi.get_all_custom_bots().result
        botlist = [x for x in bl if x.botType == 3]
        return botlist

    def bot_selector(self):
        bots = self.return_scalper_bots()
        b2 = [
            (
                f"{i.name} {i.priceMarket.primaryCurrency}-{i.priceMarket.secondaryCurrency}, {i.roi}",
                i,
            )
            for i in bots
        ]
        question = [
            inquirer.Checkbox(
                "bots",
                message="Select one or more bots using spacebar and then press return",
                choices=b2,
            )
        ]
        selection = inquirer.prompt(question)
        try:
            self.bot = selection["bots"]
        except TypeError:
            print("No bot has been selected, you must select one")
            self.bot_selector()
        return selection["bots"]

    def markets_selector(self):

        markets = self.c.marketDataApi.get_all_price_markets().result
        m2 = [
            (
                f"{EnumPriceSource(i.priceSource).name},{i.primaryCurrency}-{i.secondaryCurrency}",
                i,
            )
            for i in markets
        ]

        question = [inquirer.Checkbox("markets", message="Select markets", choices=m2)]

        selection = inquirer.prompt(question)
        self.markets = selection["markets"]
        # print(selection)
        return selection

    def setup_scalper_bot(self, bot, targetpercentage, safetythreshold):

        do = self.c.customBotApi.setup_scalper_bot(
            accountguid=bot.accountId,
            botguid=bot.guid,
            botname=bot.name,
            primarycoin=bot.priceMarket.primaryCurrency,
            secondarycoin=bot.priceMarket.secondaryCurrency,
            templateguid=bot.customTemplate,
            contractname=bot.priceMarket.contractName,
            leverage=bot.leverage,
            amountType=bot.amountType,
            tradeamount=1000,
            position=bot.coinPosition,
            fee=bot.currentFeePercentage,
            targetpercentage=targetpercentage,
            safetythreshold=safetythreshold,
        )
        print('result: ', do.errorCode, do.errorMessage)
        return do.result

    def set_targetpercentage_range(self):
        start_input = [
            inquirer.Text(
                "start",
                message="Define start of the target percentage range",
                default=0.5,
            )
        ]
        end_input = [
            inquirer.Text(
                "end", message="Define end of the target percentage range", default=1.5
            )
        ]
        step_input = [
            inquirer.Text(
                "step",
                message="Define number of steps between start and end",
                default=0.2,
            )
        ]

        start = inquirer.prompt(start_input)["start"]
        end = inquirer.prompt(end_input)["end"]
        step = inquirer.prompt(step_input)["step"]
        self.targetpercentage = [start, end, step]

    def set_safetythreshold_range(self):
        start_input = [
            inquirer.Text(
                "start", message="Define start of the safety threshold range", default=1
            )
        ]
        end_input = [
            inquirer.Text(
                "end", message="Define end of the safety threshold range", default=5
            )
        ]
        step_input = [
            inquirer.Text(
                "step",
                message="Define number of steps between start and end",
                default=0.2,
            )
        ]

        start = inquirer.prompt(start_input)["start"]
        end = inquirer.prompt(end_input)["end"]
        step = inquirer.prompt(step_input)["step"]
        self.safetythreshold = [start, end, step]

    def bt_date_to_unix(self):

        min = self.config["BT DATE"].get("min")
        hour = self.config["BT DATE"].get("hour")
        day = self.config["BT DATE"].get("day")
        month = self.config["BT DATE"].get("month")
        year = self.config["BT DATE"].get("year")
        btd = datetime.datetime(int(year), int(month), int(day), int(hour), int(min))
        return btd

    def backtest(self):
        btd = self.bt_date_to_unix()
        if len(self.bot) > 0:
            with alive_bar(len(self.bot)) as bar:
                for bot in self.bot:

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

                            bt_result = self.c.customBotApi.backtest_custom_bot(
                                bot.guid, self.ticks
                            )
                            bt_result = bt_result.result
                            try:
                                print("ROI: ", bt_result.roi, round(t, 2))
                                total_results = {
                                    "roi": bt_result.roi,
                                    "targetpercentage": round(t, 2),
                                    "safetythreshold": round(s, 2),
                                }

                                # results.append(total_results)
                                results.append(
                                    [bt_result.roi, round(t, 2), round(s, 2)]
                                )
                            except:
                                pass

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

                    self.c.customBotApi.backtest_custom_bot(bot.guid, self.ticks)

        else:
            self.bot_selector()

    def scalper_bot_menu(self):
        # choices =
        menu = [
            inquirer.List(
                "response",
                message="Please chose an action:",
                choices=[
                    "Select bots",
                    "Set range for safety threshold",
                    "Set range for target percentage",
                    "Backtest",
                    "backtest every bot",
                    "Main menu",
                ],
            )
        ]

        while True:
            user_response = inquirer.prompt(menu)["response"]
            if user_response == "Select bots":
                self.bot_selector()
            elif user_response == "Set range for safety threshold":
                self.set_safetythreshold_range()
            elif user_response == "Set range for target percentage":
                self.set_targetpercentage_range()
            elif user_response == "Backtest":
                self.backtest()
            elif user_response == "backtest every bot":
                sb = ScalperBotClass()
                sb.bot = self.c.customBotApi.get_all_custom_bots().result
                sb.targetpercentage = [0.5, 5, 0.2]
                sb.safetythreshold = [1, 2, 0.2]
                sb.backtest()
            elif user_response == "Main menu":
                break

