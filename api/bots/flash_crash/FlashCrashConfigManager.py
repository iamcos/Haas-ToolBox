from api.MainContext import config_manager

class FlashCrashConfigManager:

    def __init__(self) -> None:
        self.pricespread
        self.percentageboost
        self.multiplyer
        self.multiplyer_min
        self.multiplyer_max


    def read_limits(self):
        try:
            vars = ['pricespread_start', 'pricespread_end', 'pricespread_step']
            self.pricespread = self.read_range(vars)

        except Exception as e:
            print(e)

        try:
            vars = ["percentageboost_start", "percentageboost_end",
                    "percentageboost_step"]
            self.percentageboost = self.read_range(vars)

        except Exception as e:
            print(e)
        try:
            vars = ["percentageboost_start", "percentageboost_end",
                    "percentageboost_step"]
            self.multiplyer = self.read_range(vars)
        except Exception as e:
            print(e)
        try:
            vars = ['multiplyer_min_end', 'multiplyer_min_start', 'multiplyer_min_step']
            self.multiplyer_min = self.read_range(vars)
        except Exception as e:
            print(e)
        try:
            vars = ['multiplyer_max_start', 'multiplyer_max_stop', 'multiplyer_max_step']
            self.multiplyer_max = self.read_range(vars)
        except Exception as e:
            print(e)

        try:
            vars = ['Total_buy', 'Total_sell']
            self.totalbuy, self.totalsell = self.read_range(vars)
        except Exception as e:
            print(e)

    def read_range(self, vars=vars):
        return [x for x in [config_manager.config_parser.get("FCB_LIMITS", p) for p in vars]]
