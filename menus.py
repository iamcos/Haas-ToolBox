import inquirer
from inquirer.themes import GreenPassion
from numpy import NaN
import pandas as pd
import questionary
class Menus:
    
    def mh_menu(self):
        live_menu = [
            
            "Select Bots",
        "Select config file",
            "Set configs limicet",
            "Set create limit",
            "Find Stoploss",
            
            "Config optimisation",
            "Change backtesting date",
            
            "Start Backtesting",
            "Main Menu",
            ]
        dev_menu = [
            "test",
            "Select Bots",
            "Select config file",
            "Set configs limit",
            "Set create limit",
            "Find Stoploss",
            # 'AssistedBT',
            "Config optimisation",
            "Change backtesting date",
            "Start Backtesting",
            "Completed Backtests",
            "Main Menu",
            ]
        
        self.read_limits()
        menu = [
            inquirer.List(
                "response",
                message=f"Create: {self.limit}, Configs: {self.num_configs}",
                choices=live_menu if self.live else dev_menu,
                )
            ]
        
        while True:
            response = inquirer.prompt(menu,theme=GreenPassion())["response"]
            if response == "Select Bots":
                bot = self.bot_selector(15,multi=True)
            elif response == "Select config file":
                file = pd.read_csv(self.file_selector())
                self.configs.roi = NaN
            elif response == "Set configs limit":
                self.set_configs_limit()
            
            elif response == "Set create limit":
                self.set_create_limit()
            elif response == "AssistedBT":
                pass
            
            elif response == "Change backtesting date":
                self.write_date()
            
            elif response == "test":
                self.bbl_menu()
            
            elif response == "Completed Backtests":
                menu = [
                    inquirer.List(
                        "response",
                        "Chose",
                        choices=[
                            "Select bot from db",
                            "Print results",
                            "Save results to file",
                            "Back",
                            ],
                        )
                    ]
                while True:
                    response = inquirer.prompt(menu)["response"]
                    
                    if response == "Select bot from db":
                        if self.config_storage:
                            guids = list(self.config_storage.keys())
                            bl = [
                                (x.name,x)
                                for x in
                                self.c.customBotApi.get_all_custom_bots().result
                                if x.botType == 15
                                if bot.guid in guids
                                ]
                            menu = [inquirer.List("response","Select Bot",choices=bl)]
                            while True:
                                bot = inquirer.prompt(menu)["response"]
                    
                    if response == "Print results":
                        self.print_completed_configs()
                    
                    elif response == "Save results to file":
                        pass
                    elif response == "Back":
                        break
            
            elif response == "Find Stoploss":
                stoploss_menu = [
                    inquirer.List(
                        "stoploss",
                        "Stoploss menu:",
                        choices=[
                            "Set stoploss range",
                            "Find stoploss",
                            "Back",
                            ],
                        )
                    ]
                while True:
                    response = inquirer.prompt(stoploss_menu)["stoploss"]
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
            elif response == "Start Backtesting":
                if self.configs is not pd.DataFrame:
                    self.configs = pd.read_csv("./bots.csv")
                    self.configs.roi = NaN
                for b in self.bots:
                    
                    self.bot = b
                    
                    self.bt()
                    self.create_top_bots()
            
            elif response == "Main Menu":
                break
    
    
    def intervals_menu(self):
        try:
            range = self.ranges.bot.intervals.selected
        except:
            range = self.ranges.bot.intervals.selected = self.select_intervals()
        i_menu = [
            inquirer.List(
                "response",
                message=f"Selected intervals: { range} :",
                choices=[
                    "Select Bots",
                    "Select Intervals",
                    "Backtest Selected Intervals",
                    "Backtest all Intervals",
                    "Back",
                    ],
                )
            ]
        
        while True:
            response = inquirer.prompt(i_menu)["response"]
            
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
            elif response == "test":
                pass
    
    def select_intervals(self):
        
        intervals = [
            inquirer.Checkbox(
                "intervals",
                message="Select required intervals using space, confirm with enter: ",
                choices=self.ranges.bot.intervals.list,
                )
            ]
        selected_intervals = inquirer.prompt(intervals)["intervals"]
        self.config.set("MH_LIMITS", "selected_intervals", str(selected_intervals))
        self.write_file()
        
        return selected_intervals
    
    def bbl_menu(self):
        
        live_menu = [
            # 'test',
            "Select Bot",
            "Change length range",
            "Change BT date",
            "Backtest range",
            # 'Discover profit',
            "Back",
            ]
        dev_menu = [
            "test",
            "Select Bot",
            "Change length range",
            "Change BT date",
            "Backtest range",
            "Discover profit",
            "Back",
            ]
        
        bbl_menu = [
            inquirer.List(
                "response",
                message=f"BB Length range: {self.ranges.indicators.bBands.length}",
                choices=live_menu if self.live else dev_menu,
                )
            ]
        while True:
            response = inquirer.prompt(bbl_menu)["response"]
            if response == "Select Bot":
                bot = self.bot_selector(15)
            elif response == "Change length range":
                start = int(inquirer.text("Define bBands Length range start: "))
                stop = int(inquirer.text("Define bBands Length range stop: "))
                step = int(inquirer.text("Define bBands Length range step: "))
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
            elif response == "test":
                self.get_first_bot()
                self.ranges.indicators.bBands.length = 2, 5, 1
                self.backtest_bbands_length()
                self.ranges.indicators.bBands.length = 3, 7, 1
                self.backtest_bbands_length()
            elif response == "Back":
                break
    
    
    def bruteforce_menu(self):
        live_menu = [
            "Interval",
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
        dev_menu = [
            "test",
            "Interval",
            # 'Signal Consensus',
            # 'bBands length',
            # 'bBands Devup',
            # 'bBands Devdown',
            # 'MA Type',
            # 'Rsi Length',
            # 'Rsi Buy',
            # 'Rsi Sell',
            # 'MACD Slow',
            # 'MACD Fast',
            # 'MACD Signal',
            "New configs",
            ]
        
        self.parameter = {}
        bf_menu = [
            inquirer.List(
                "response",
                message="Select a parameter to bruteforce:",
                choices=live_menu if self.live else dev_menu,
                )
            ]
        
        response = inquirer.prompt(bf_menu)["response"]
        
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
        elif response == "New configs":
            ranges = self.create_configs_from_top_results()