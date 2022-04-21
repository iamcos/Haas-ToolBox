from InquirerPy import inquirer
from numpy import NaN
import pandas as pd
from share_mad_hatter import ShareMadHatter


class Menus:
    def menu(self):
        live_menu = [
            "Select Bots",
            "Start Backtesting",
            "Set BT mode",
            "Set create limit",
            "Set configs limit",
            "Select config file",
            "Change backtesting date",
            "Find Stoploss",
            "Bot Management",
            "Main Menu",
        ]

        while True:
            self.read_limits()
            response = inquirer.select(
                message=f"{self.limit} will be created, {self.num_configs} configs in queue",
                choices=live_menu,
            ).execute()
            if response == "Select Bots":
                bot = self.bot_selector(15, multi=True)
            elif response == "Select config file":
                file = self.csv_file_selector()
                # self.configs.roi = NaN
            elif response == "Save bots to OBJ file":
                self.save_bots_to_file(self.bots)
            elif response == "Set configs limit":
                self.set_configs_limit()
            elif response == "Set ROI treshold limit":
                self.set_acceptable_roi_threshold()
            elif response == "Set BT mode":
                self.set_backtesting_mode()

            elif response == "Set create limit":
                self.set_create_limit()

            elif response == "Change backtesting date":
                self.write_date()

            elif response == "Find Stoploss":
                while True:
                    response = inquirer.select(
                        message="Stoploss menu:",
                        choices=[
                            "Set stoploss range",
                            "Find stoploss",
                            "Back",
                        ],
                    ).execute()
                    if response == "Find stoploss":
                        if not self.bots:
                            self.get_first_bot()
                        for b in self.bots:
                            self.bot = b
                            self.find_stoploss()

                    elif response == "Set stoploss range":
                        self.set_stoploss_range()

                    elif response == "Back":
                        break

            elif response == "Config optimisation":
                self.bruteforce_menu()

            elif response == "Bot Management":
                ShareMadHatter.share_mh(self)

            elif response == "Start Backtesting":
                if self.configs is not pd.DataFrame:
                    self.configs = pd.read_csv("../../config/bots.csv")
                    self.configs.roi = NaN
                for bot in self.bots:
                    self.bot = bot
                    self.bt()
                    self.create_top_bots()

            elif response == "Main Menu":
                break

    def intervals_menu(self):
        try:
            range = self.ranges.bot.intervals.selected
        except:
            range = self.ranges.bot.intervals.selected = self.select_intervals()

        while True:
            response = inquirer.select(
                message=f"Selected intervals: {range} :",
                choices=[
                    "Select Bots",
                    "Select Intervals",
                    "Backtest Selected Intervals",
                    "Backtest all Intervals",
                    "Back",
                ],
            ).execute()

            if response == "Select Intervals":
                self.ranges.bot.intervals.selected = self.select_intervals()

            elif response == "Backtest Selected Intervals":

                self.bt_intervals()

            elif response == "Backtest all Intervals":
                self.ranges.bot.intervals.selected = self.ranges.bot.intervals.list
                self.bt_intervals()

            elif response == "Select Bots":
                bot = self.bot_selector(15)
            elif response == "Back":
                break

    def select_intervals(self):

        intervals = inquirer.select(
            message="Select required intervals using space, confirm with enter: ",
            choices=self.ranges.bot.intervals.list,
            multiselect=True,
        ).execute()

        self.config.set("MH_LIMITS", "selected_intervals", intervals)
        self.write_file()

        return intervals

    def bbl_menu(self):

        live_menu = [
            "Select Bot",
            "Change length range",
            "Change BT date",
            "Backtest range",
            "Back",
        ]

        while True:
            response = inquirer.select(
                message=f"BB Length range: {self.ranges.indicators.bBands.length}",
                choices=live_menu,
            ).execute()
            if response == "Select Bot":
                bot = self.bot_selector(15)
            elif response == "Change length range":
                start = inquirer.text(
                    "Define bBands Length range start: ").execute()
                stop = inquirer.text(
                    "Define bBands Length range stop: ").execute()
                step = inquirer.text(
                    "Define bBands Length range step: ").execute()
                self.ranges.indicators.bBands.length = start, stop, step
                # print(f'bBands Length range now set to {start}{stop} with step {step}')
                try:
                    self.config.add_section("MH_INDICATOR_RANGES")
                except:
                    pass
                self.config.set(
                    "MH_INDICATOR_RANGES",
                    "length_range",
                    str(self.ranges.indicators.bBands.length),
                )
                self.write_file()
            elif response == "Backtest range":
                self.backtest_bbands_length()
            elif response == "Back":
                break

    def bruteforce_menu(self):
        live_menu = [
            # "Interval",
            # 'Signal Consensus',
            "bBands length",
            # 'bBands Devup',
            # 'bBands Devdown',
            # 'MA Type',
            # 'Rsi Length',
            # 'Rsi Buy',
            # 'Rsi Sell',
            # 'MACD Slow',
            # 'MACD Fast',
            # 'MACD Signal',
        ]
        self.parameter = {}
        response = inquirer.select(
            message="Select a parameter to bruteforce:",
            choices=live_menu
        ).execute()

        if response == "Interval":
            self.response = response
            self.intervals_menu()
        elif response == "Signal Consensus":
            self.response = response
            self.bt_consensus()
        elif response == "bBands length":
            self.bbl_menu()
        elif response == "bBands Devup":
            pass
        elif response == "bBands Devdown":
            pass
        elif response == "MA Type":
            pass
        elif response == "Rsi Length":
            pass
        elif response == "Rsi Buy":
            pass
        elif response == "Rsi Sell":
            pass
        elif response == "MACD Slow":
            pass
        elif response == "MACD Fast":
            pass
        elif response == "MACD Signal":
            pass
