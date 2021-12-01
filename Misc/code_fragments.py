#Mad Hatter finetuner

def finetune(self, bot):
    config = self.bot_config(bot)
    config.drop(
        [
            "interval",
            "signalconsensus",
            "resetmiddle",
            "allowmidsells",
            "matype",
            "fcc",
            "trades",
            "roi",
        ],
        axis="columns",
        inplace=True,
    )
    columns = config.columns
    tuning_configs = pd.DataFrame(columns=columns)
    for i in config.columns:
        v = config.i.values
        if int(v):
            if v >= 5:
                for n in range(v, v + 3, 1):
                    pass
                for n in range(v - 3, v, 1):
                    pass
            elif v <= 2:
                pass
            elif v < 5:
                for n in range(v, v + 3):
                    pass
                for n in range(v - 2, v, 1):
                    pass



    def auto_bt_menu(self):
        self.num_configs = 200

        options = [
            "Select Bot",
            "Select config file",
            "Set Limit",
            "Start Backtesting",
            "Main Menu",
        ]
        question = [inquirer.List("autobt", "Select action: ", options)]

        while True:
            response = inquirer.prompt(question)
            if response["autobt"] in options:
                ind = options.index(response["autobt"])
            if ind == 0:
                bot = self.bot_selector()
            elif ind == 1:
                file = pd.read_csv(self.file_selector())
            elif ind == 2:
                self.num_configs = int(
                    input(
                        "Type the number of configs you wish to apply from a given file: "
                    )
                )
            elif ind == 3:
                if self.num_configs > len(self.configs.index):
                    self.num_configs == len(self.configs.index)
                else:
                    pass
                configs = self.configs.sort_values(by="roi", ascending=False)[
                          0: self.num_configs
                          ]
                configs.drop_duplicates()
                configs.reset_index(inplace=True, drop=True)
                print(configs)
                bt_results = BotDB().iterate_csv(
                    configs, self.bot, depth=Haas().read_ticks()
                )
                filename = (
                        str(bot.name.replace("/", "_"))
                        + str("_")
                        + str(datetime.date.today().month)
                        + str("-")
                        + str(datetime.date.today().day)
                        + str("_")
                        + str(len(bt_results))
                        + str(".config")
                )
                bt_results.to_csv(filename)
            elif ind == 4:
                break
