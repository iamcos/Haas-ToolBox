import inquirer
from ratelimit import limits, sleep_and_retry
from time import sleep
from haas import Haas


class InteractiveBT(Haas):
    def __init__(self):
        Haas.__init__(self)

        self.ticks = Haas().read_ticks()

    @sleep_and_retry
    @limits(calls=2, period=1)
    def monitor_bot(self):
				
        bot_config = self.bot_config(self.bot).drop(["obj",'roi','trades'], axis=1)
        self.bot = self.c.customBotApi.get_custom_bot(self.bot.guid,15).result
        bt_results = []
        go_on = 'y'
        while go_on == 'y':
          sleep(1)
          self.bot = self.c.customBotApi.get_custom_bot(self.bot.guid, 15).result
          # go_on = input('Press S to stop')
          config_now = self.bot_config(self.bot).drop(["obj",'roi','trades'], axis=1)
          
          change = config_now.equals(bot_config)
          print(bot_config)
          print(config_now)
          print(change)
          if not change:
              bt = self.c.customBotApi.backtest_custom_bot(
                  self.bot.guid, self.ticks
              ).result
              bt_results.append(self.bot_config(bt))
              bot_config = self.bot_config(bt).drop(["obj",'roi','trades'], axis=1)

if __name__ == "__main__":
    ib = InteractiveBT()
    ib.bot_selector(15)
    ib.monitor_bot()
