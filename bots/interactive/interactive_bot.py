from time import sleep
import datetime
from InquirerPy import inquirer
import pandas as pd
from ratelimit import limits, sleep_and_retry

from bots.mad_hatter.mad_hatter_bot import MadHatterBot


class InteractiveBot(MadHatterBot):
    """
        TODO:
            * IDEA: combine backtests of a single parameter into a list.
            After moving to a different parameter, have previous best param
            autoset.
        """

    def __init__(self):
        MadHatterBot.__init__(self)

    @sleep_and_retry
    @limits(calls=5, period=1)
    def monitor_bot(self):
        bot_config = self.get_bot_config_as_dataframe(self.bot)
        bt_results = [bot_config]
        self.bot = self.c.customBotApi.backtest_custom_bot(self.bot.guid, self.ticks).result

        print(f'Selected {self.bot.name} bot is being monitored for changes to config.')

        print(f'  1. Have Bot Remote (keypress 1) Visible')
        print(f'  2. Have selected bot open in Haas Browser interface.')
        print(f'  3. Open the bot in Full Screen view by')
        print(f'        clicking the "Full screen" button')
        print(f'   4. Navigate to indicator parameters tab.')
        print(f'         i. Click on any integer parameter.')
        print(f'         ii. Change it by UP or DOWN keyboard keys')
        print(
            f'         iii. Jump between parameters via "TAB" and keyboard keys '
            f'"Shift+TAB" ')
        print(f'             On change bot gets instantly backtested')

        print(f'\n       To stop the process, use Clear bot command in Haas web '
              f'interface.')
        print(f'             Then open Bot Log:it must be empty, else set fix error.')
        print(f'             You may need to set trading amount or change coin position')
        print(f'\n           Rerun Clear bot command, check for empty log .')

        while self.bot.botLogBook:
            # print(self.bot.botLogBook)
            sleep(1.5)
            self.bot = self.haas.client.customBotApi.get_custom_bot(self.bot.guid, 15)
            if self.bot.errorCode.value == 100:
                self.bot = self.bot.result
            else:
                print('False')
                return False
            config_now = self.get_bot_config_as_dataframe(self.bot)

            configs_are_the_same = config_now.drop(["obj", 'roi', 'trades'], axis=1).equals(
                bot_config.drop(["obj", 'roi', 'trades'], axis=1))

            if not configs_are_the_same:
                # print(self.bot.botLogBook)
                bt = self.c.customBotApi.backtest_custom_bot(
                    self.bot.guid, self.ticks
                ).result
                bot_config = self.get_bot_config_as_dataframe(
                    self.c.customBotApi.get_custom_bot(self.bot.guid, 15).result)
                # print('bot_config',bot_config)
                bt_results.append(bot_config)
                print(bot_config.drop(["obj"], axis=1))

        bot = self.bot
        bt_results = pd.concat(bt_results)
        bt_results = self.save_and_sort_results(bt_results)
        self.store_results(bt_results)
        configs = self.config_storage[bot.guid]
        print(configs)
        if self.limit >= len(configs.index):
            self.limit = len(configs.index)
        for c in range(self.limit):
            self.setup_bot_from_df(bot, configs.iloc[c], print_errors=False)
            bot = self.haas.client.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks()).result
            name = f"{c},{datetime.datetime.today().month}-{datetime.datetime.today().day}," \
                   f"{configs.roi.iloc[c]}"
            self.haas.client.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, name)
            print(f'{name} bot has been created')
        return bt_results

    def menu(self):
        self.read_limits()
        while True:
            resp = inquirer.select(message=f'{self.bot_print()}', choices=[
                'Select Bot',
                'Set Create Limit',
                'Change BT Data',
                'Start AssistedBT',
                'Back',
            ]
                                   ).execute()
            if resp == 'Select Bot':
                self.select_single_bot_by_type(15)
            if resp == 'Set Create Limit':
                self.limit = inquirer.text('Type number top of configs to create as bots at the end?').execute()
                self.write_file()
            if resp == 'Change BT Data':
                self.write_date()
            if resp == 'Start AssistedBT':
                self.monitor_bot()
            if resp == 'Back':
                break

    def bot_print(self):
        if self.bot:
            return f'{self.bot.name} selected.'
        else:
            return 'No Bot selected'


def main():
    ib = InteractiveBot()
    ib.menu()


if __name__ == "__main__":
    main()