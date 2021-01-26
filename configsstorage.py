import pandas as pd
class ConfigsManagment:
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
            stored_configs, how="outer",on=columns, indicator=True
        ).loc[lambda x: x["_merge"] == "left_only"]
        
       
        try:
          unique_configs.drop("_merge", axis=1,inplace=True)
        except Exception as e:
          print(e)
        try:
          stored_configs.drop("_merge", axis=1,inplace=True)
        except Exception as e:
          print(e)
        
       
        stored_configs = pd.concat([unique_configs,stored_configs],ignore_index=True,keys=columns)
        print("unique configs", unique_configs)
        print(f"Duplicate configs removed, {len(unique_configs.index)} new")
        print(f'stored configs {stored_configs}')
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
  
            if isinstance(first_config,pd.DataFrame) and isinstance(second_config,pd.DataFrame):
                first_config = self.configs.iloc[first_config]
                second_config = self.configs.iloc[second_config]

            changes  = pd.merge(first_config,second_config,how='outer', on=self.configs.columns).set_index(['key_0'],drop=True)
            changes.replace(True,1,inplace=True)
            changes.replace(False,0,inplace=True)
            changes = self.clean_df(changes.T)
            changes = changes.append(changes.diff(axis=0).iloc[1])
            changes.reset_index(inplace=True, drop=True)
            # changes.rename_axis('DA',inplace=True)
            print(changes)
            return changes
            
            
                        
         
