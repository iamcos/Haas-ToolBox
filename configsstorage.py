import pandas as pd
from InquirerPy import inquirer
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumPlatform import EnumPlatform
import os
import datetime
class ConfigsManagment:
    def create_bots_from_csv(self):
        exchange = self.select_exchange()
        market = self.market_selector(exchange)
        configs = self.configs = self.csv_file_selector()
        rois = self.configs.roi.to_list()
        selected_configs = inquirer.select(message='Select one or more results', choices=rois,multiselect=True).execute()
        bots = self.create_bots(exchange, market, configs, selected_configs)
        return bots

    def create_bots(self,exchange,market,configs,selected_configs):
                acountId = exchange[0].__dict__['guid']
                    
                for i in selected_configs:
                    name = f"{market.primaryCurrency} {market.secondaryCurrency}"
                    new_bot = self.c.customBotApi.new_custom_bot(
                        acountId,
                        15,
                        name,
                        market.primaryCurrency,
                        market.secondaryCurrency,
                        market.contractName,
                    )
                    print(new_bot.errorCode, new_bot.errorMessage,'new bot')
                    print(new_bot.__dict__)
                    bot = new_bot.result
                    print(bot,'bot')
                
                    self.setup_bot_from_df(bot, configs[configs.roi == i].iloc[0], print_errors=False)
                    bot = self.check_bot_trade_ammount(bot)
                    bot = self.c.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks()).result
                    # bot2 = self.c.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, f"{bot.name}.{bot.roi}")
                    # bot = self.c.customBotApi.setup_mad_hatter_bot()
                    bot = self.c.customBotApi.setup_mad_hatter_bot(
                            # This code sets time interval
                            botName= f"{market.primaryCurrency} {market.secondaryCurrency} {bot.roi}%",
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
                            interval=bot.interval,
                            includeIncompleteInterval=bot.includeIncompleteInterval,
                            mappedBuySignal=bot.mappedBuySignal,
                            mappedSellSignal=bot.mappedSellSignal,
                        )
                    

    def create_from_csv(self):
        bot = None
        menu_items = [
                     "Select exchange",
                    "Select markets",
                    "Select config file",
                    'Select configs',
                    "Create Bots"
                    
                        ]
        
        while True:
            response = inquirer.select('Make a choice:', choices=menu_items).execute()
            if response == "Select exchange":
                    exchange = self.select_exchange()
                    print(exchange[0].__dict__)
            elif response == "Select markets":
                market = self.market_selector(exchange)
            elif response == "Select config file":
                configs = self.configs = self.csv_file_selector()
            elif response == 'Select configs':
                rois = self.configs.roi.to_list()
                selected_configs = inquirer.select(message='Select one or more results', choices=rois,multiselect=True).execute()
    
            elif response == 'Create Bots':
                if bot == None:
                    acountId = exchange[0].__dict__['guid']
                    
                for i in selected_configs:
                    name = f"{market.primaryCurrency} {market.secondaryCurrency}"
                    new_bot = self.c.customBotApi.new_custom_bot(
                        acountId,
                        15,
                        name,
                        market.primaryCurrency,
                        market.secondaryCurrency,
                        market.contractName,
                    )
                    # print(new_bot.errorCode, new_bot.errorMessage,'new bot')
                    # print(new_bot.__dict__)
                    bot = new_bot.result
                    # print(bot,'bot')
                
                    self.setup_bot_from_df(bot, configs[configs.roi == i].iloc[0], print_errors=False)
                    bot = self.check_bot_trade_ammount(bot)
                    bot = self.c.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks()).result
                    # bot2 = self.c.customBotApi.clone_custom_bot_simple(bot.accountId, bot.guid, f"{bot.name}.{bot.roi}")
                    # bot = self.c.customBotApi.setup_mad_hatter_bot()
                    bot = self.c.customBotApi.setup_mad_hatter_bot(
                            # This code sets time interval
                            botName= f"{market.primaryCurrency} {market.secondaryCurrency} {bot.roi}%",
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
                            interval=bot.interval,
                            includeIncompleteInterval=bot.includeIncompleteInterval,
                            mappedBuySignal=bot.mappedBuySignal,
                            mappedSellSignal=bot.mappedSellSignal,
                        )
                    # print(bot.errorCode, bot.errorMessage)
    
    def match_exchange_with_bot(self,botobject):
        bot_exchange = EnumPriceSource(botobject.priceMarket.priceSource).value
        accounts = self.get_accounts_with_details()
        matching_accounts = [
                    {
                            "name": f"{EnumPriceSource(i.connectedPriceSource).name} {i.name} {EnumPlatform(i.platformType).name} "
                            f"",
                            "value": i,
                    }
                    for i in accounts if EnumPriceSource(i.connectedPriceSource).value == bot_exchange
            ]
        if len(matching_accounts)>1:
            
            selected_exchange = [
                        inquirer.select(
                                message="Select exchange account by pressing Return or Enter ",
                                choices=matching_accounts,
                        ).execute()
                ]
            return selected_exchange
        elif len(matching_accounts)==1:
            return matching_accounts
        else:
             return None
            
    



    def store_results(self, bt_results):

        if self.bot.guid in self.config_storage:
            configs = self.config_storage[self.bot.guid]

            configs.append(bt_results)
            configs.reset_index(inplace=True, drop=True)
            configs.sort_values(by="roi", ascending=False)
            configs.drop_duplicates(subset=self.columns, inplace=True)

            self.config_storage[self.bot.guid] = configs
            print(
                f"backtesting results have been added to current backtesting session storage pool."
            )

        else:
            self.config_storage[self.bot.guid] = bt_results

    def remove_already_backtested(self, new_configs):
        """Drops already processed configs from input dataframe.


        Args:
          new_configs (dataframe): dataframe with bot configs

        Returns:
          dataframe: that contains configs not yet tested
        """
        columns = self.columns
        if self.bot.guid in self.config_storage:

            stored_configs = self.config_storage[self.bot.guid]

            unique_configs = new_configs.merge(
                stored_configs, how="outer", on=columns, indicator=True
            ).loc[lambda x: x["_merge"] == "left_only"]

            try:
                unique_configs.drop("_merge", axis=1, inplace=True)
            except Exception as e:
                print(e)
            try:
                stored_configs.drop("_merge", axis=1, inplace=True)
            except Exception as e:
                print(e)

            stored_configs = pd.concat(
                [unique_configs, stored_configs], ignore_index=True, keys=columns
            )
            print("unique configs", unique_configs)
            print(f"Duplicate configs removed, {len(unique_configs.index)} new")
            print(f"stored configs {stored_configs}")
            self.config_storage[self.bot.guid] = stored_configs
            return unique_configs

        else:
            return new_configs

    def find_difference_between_two_configs(self, first_config, second_config):
        """Returns the difference in configuration parameters between two configs.
        It subtracts one config from another, creating new row with difference in it.
        Can either accept config as dataframe with one row or as integer number
        that represents index of required config in self.configs

        Args:
            first_config [integer] : dataframe containing config or config's index position
            second_config [integer] : dataframe containing config or config's index position

        Returns:
            [dataframe]: containing first config, second config and difference in configuration parameters as rows.

        """

        if isinstance(first_config, pd.DataFrame) and isinstance(
            second_config, pd.DataFrame
        ):
            first_config = self.configs.iloc[first_config]
            second_config = self.configs.iloc[second_config]

        changes = pd.merge(
            first_config, second_config, how="outer", on=self.configs.columns
        ).set_index(["key_0"], drop=True)
        changes.replace(True, 1, inplace=True)
        changes.replace(False, 0, inplace=True)
        changes = self.clean_df(changes.T)
        changes = changes.append(changes.diff(axis=0).iloc[1])
        changes.reset_index(inplace=True, drop=True)
        # changes.rename_axis('DA',inplace=True)
        print(changes)
        return changes
   
    def create_bots_from_obj(self):
        botobjs = self.return_bot_objects()
        exchange = self.match_exchange_with_bot(botobjs[0])
        acountId = exchange[0].__dict__['guid']
        for obj in botobjs:
            market = obj.priceMarket
            name = f"{market.primaryCurrency} {market.secondaryCurrency}"
            bot = self.c.customBotApi.new_custom_bot(
                        acountId,
                        15,
                        name,
                        market.primaryCurrency,
                        market.secondaryCurrency,
                        market.contractName).result
                    
            self.setup_bot_from_obj(bot,obj,print_errors=True)
            bot = self.check_bot_trade_ammount(bot)
            bot = self.c.customBotApi.backtest_custom_bot(bot.guid, self.read_ticks()).result
            bot = self.c.customBotApi.setup_mad_hatter_bot(
                            # This code sets time interval
                            botName= f"{market.primaryCurrency} {market.secondaryCurrency} {bot.roi}%",
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
                            interval=bot.interval,
                            includeIncompleteInterval=bot.includeIncompleteInterval,
                            mappedBuySignal=bot.mappedBuySignal,
                            mappedSellSignal=bot.mappedSellSignal,
                        )
    def save_and_sort_results(self, bt_results, obj=True, csv=True):
        if obj:
            os.makedirs("./botstorage/", exist_ok=True)
            obj_file_name = (
                f'./botstorage/{self.bot.priceMarket.primaryCurrency}_{self.bot.priceMarket.secondaryCurrency}_'
                f"{datetime.date.today().month}"
                f"_{datetime.date.today().day}.obj"
            )

            objects = bt_results.obj
            try:
                prev_file = pd.read_pickle(obj_file_name)
            except Exception as e:
                print(e,'exception')
                objects.to_pickle(obj_file_name)
            else:
                prev_file.append(objects,ignore_index=True)
            
            prev_file.to_pickle(obj_file_name)
            print('objects file size now: ',len(objects))

        if csv:
            filename = (
                f'{self.bot.priceMarket.primaryCurrency}_{self.bot.priceMarket.secondaryCurrency}_{datetime.date.today().month}_{"-"}_{datetime.date.today().day}_{"_"}_{len(bt_results)}_{".csv"}')
            to_csv = bt_results.drop("obj", axis=1)
            to_csv.sort_values(by="roi", ascending=False, inplace=True)
            to_csv.drop_duplicates() #subset=to_csv.columns[~to_csv.columns.isin(['roi','obj'])]
            to_csv.reset_index(inplace=True, drop=True)
            to_csv.to_csv(filename)

        bt_results2 = bt_results.sort_values(by="roi", ascending=False)
        bt_results2.drop_duplicates() #subset=bt_results2.columns[~bt_results2.columns.isin(['roi','obj'])]
        bt_results2.reset_index(inplace=True, drop=True)
        return bt_results2

    def obj_file_selector(self):
        files = self.get_obj_files()
        file = inquirer.select(message="Please Select file from list: ", choices=[i for i in files]).execute()
        return file

    def get_days(self,x):
        if len(x.completedOrders)>0:
            diff = datetime.datetime.today()-pd.to_datetime(x.completedOrders[0].unixAddedTime,unit='s')
            # print(diff)
            return f'{diff.days} days ago'
        else:
            return 'No trade history'
    def return_bot_objects(self):
        files = []
        for file in os.listdir("./botstorage/"):
            # if file.endswith(".obj") or file.endswith('.json'):
            if file.endswith(".obj"):
                files.append(file)
        file = inquirer.select(message="MH Bots: ",choices=files,
            ).execute()  # where b bot object returned from dic[x] name list
        objects = pd.read_pickle(f"./botstorage/{file}")
        n = [[f"{x.name}| ROI: {x.roi}"][0] for x in objects]
        b = [x for x in objects]  # creates list of names
        dic = dict(zip(b,n))  # creates zipped obj/names list
        format = "%m/%d/%Y"
        
        bot_list = [{'name': f"{x.name} {x.priceMarket.primaryCurrency}/{x.priceMarket.secondaryCurrency} {x.roi}% {self.get_days(x)}", 'value':x} for x in objects]
        botobjects = inquirer.select(message="    Name     Ticker     Roi   Last Trade ",choices=bot_list,
            multiselect=True).execute()  # where b bot object returned from dic[x] name list
        return botobjects
    
    def csv_file_selector(self):
        """[Displays multiple files and allows for t heir selection
        Selection then sets self.file path for reference and
        reads confis into a database self.configs]

        Args:
            path (str, optional): [description]. Defaults to ".".

        tsm
        """
        files = self.get_csv_files()
        # print(files[0:5])
        file = inquirer.select(message="Please Select file from list: ", choices=[i for i in files]).execute()

        configs =self.configs = pd.read_csv(file)
        return configs
