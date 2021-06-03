import pandas as pd
from InquirerPy import inquirer
from haasomeapi.enums.EnumPriceSource import EnumPriceSource
from haasomeapi.enums.EnumPlatform import EnumPlatform

class ConfigsManagment:
    def pipeline(self):
        exchange = self.select_exchange()
        market = self.market_selector(exchange)
        configs = self.configs = self.file_selector()
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
                configs = self.configs = self.file_selector()
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
                    # print(bot.errorCode, bot.errorMessage)
            
    def select_exchange(self):
            accounts = self.get_accounts_with_details()
            accounts_inquirer_format = [
                    {
                            "name": f"{EnumPriceSource(i.connectedPriceSource).name} {i.name} {EnumPlatform(i.platformType).name} "
                            f"",
                            "value": i,
                    }
                    for i in accounts
            ]
            exchange = [
                    inquirer.select(
                            message="Select exchange account by pressing Return or Enter ",
                            choices=accounts_inquirer_format,
                    ).execute()
            ]
            return exchange

    def market_selector(self,exchange):

            market= self.c.marketDataApi.get_price_markets(EnumPriceSource(exchange[0].connectedPriceSource).value).result
            m2 = [
                { 'name':f"{i.primaryCurrency}/" #{EnumPriceSource(i.priceSource).name},
                    f"{i.secondaryCurrency}", "value" : i} for i in market
                ]

            market = inquirer.fuzzy(message="Type tickers to search:",choices=m2).execute()
            return market
 
    def get_accounts_with_details(self):
        accounts = self.c.accountDataApi.get_all_account_details().result
        accounts_with_details = list(accounts.values())
        print(accounts_with_details)
        return accounts_with_details


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
