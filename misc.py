
 def apply_configs_menu(self):
 options = [
		 "Select Bot",
		 "Select file with configs",
		 "Apply configs",
		 "Main Menu",
 ]
 config_questions = [inquirer.List("response", "Select an option: ", options)]

 while True:
		 response = inquirer.prompt(config_questions,theme=GreenPassion())
		 if response["response"] in options:
				 ind = options.index(response["response"])
		 if ind == 0:
				 bot = self.bot_selector()
		 elif ind == 1:
				 file = pd.read_csv(self.file_selector())
		 elif ind == 2:
				 # print(self.configs)

				 configs = self.configs.sort_values(by="roi", ascending=False)
				 configs.drop_duplicates()
				 configs.reset_index(inplace=True, drop=True)
				 while True:
						 print(configs)
						 print(
								 "To apply bot type config number from the left column and hit
								 return."
						 )
						 print("To return to the main menu, type q and hit return")
						 resp = input("Config number: ")
						 try:
								 if int(resp) >= 0:

										 self.setup_bot_from_df(
												 self.bot, configs.iloc[int(resp)]
										 )
										 # print(Haas().read_ticks)
										 self.bt_bot(self.bot, Haas().read_ticks())
								 else:
										 break
						 except ValueError as e:
								 break

		 elif ind == 3:
				 break


						 # bt = self.c.customBotApi.backtest_custom_bot_on_market(
						 # 		bot.accountId,
						 # 		bot.guid,
						 # 		int(depth),
						 # 		bot.priceMarket.primaryCurrency,
						 # 		bot.priceMarket.secondaryCurrency,
						 # 		bot.priceMarket.contractName,
						 # 		)

>>>
# new_bot = self.c.customBotApi.clone_custom_bot_simple(b.accountId, b.guid, name)
				 # new_bot = self.c.customBotApi.new_custom_bot(b.accountId, b.botType,
				 name,
				 #
				 b.priceMarket.primaryCurrency,
				 #
				 b.priceMarket.secondaryCurrency,
				 #
				 b.priceMarket.contractName)


def optimize(self):
 configs = self.config_storage[self.bot.guid]
 config = configs.iloc[0]
 cols = [
		 "interval",
		 "signalconsensus",
		 "fcc",
		 "resetmiddle",
		 "allowmidsells",
		 "matype",
		 "rsil",
		 "rsib",
		 "rsis",
		 "bbl",
		 "devup",
		 "devdn",
		 "macdfast",
		 "macdslow",
		 "macdsign",
		 "trades",
		 "roi",
		 ]
 intervals = [1,2,3,4,5,6,10,12,15,20,30,45,60,90,120,150,180,240,360,720,1440,
 2880]
 for i in config.columns:
		 if i == 'interval':
				 time_intervals_to_test = arange(i)

def finetune(self):
 if self.bot is None:
		 bl = self.c.customBotApi.get_all_custom_bots()
		 botlist = [x for x in bl.result if x.botType == 15]
		 bot = botlist[0]
		 print(bot.guid,bot.botType)
		 bot = self.c.customBotApi.backtest_custom_bot_on_market(
												 bot.accountId,
												 bot.guid,
												 1,
												 bot.priceMarket.primaryCurrency,
												 bot.priceMarket.secondaryCurrency,
												 bot.priceMarket.contractName,
												 ).result
		 print(bot)
		 self.bot = bot
 menu = []
 steps = 4
 config = self.bot_config(self.bot)
 print(config)

 rsil_minus_range = [x for x in range(int(config.rsil.iloc[0]),
 int(config.rsil.iloc[0])-4, -1) if x >1]
 rsil_plus_range = [x for x in range(int(config.rsil.iloc[0]),
 int(config.rsil.iloc[0])+4, 1) if x < 60]

 rsil_total_range = [x for x in range(2,100,1)]
 rsil = int(config.rsil.loc[0])
 if rsil in [0,1,2]:
	 rsil_neighbours_in_total_range = rsil_total_range[rsil-steps:rsil+steps]
	 print(rsil_neighbours_in_total_range)
 elif rsil-steps <=0:
		 rsil_neighbours_in_total_range = rsil_total_range[rsil:rsil + steps*2]
		 print(rsil_neighbours_in_total_range)


