from scripts.config_manager import ConfigManager
from InquirerPy import inquirer


class BotSellector:

  def bot_selector(self,botType,multi=False):
      config_manager = ConfigManager().check_config()
      # config_manager.check_config()
      client = config_manager

      bots = [
        x
        for x in client.customBotApi.get_all_custom_bots().result
        if x.botType == botType
        ]

      bots.sort(key=lambda x:x.name,reverse=False)
      b2 = [{'name':f"{i.name} {i.priceMarket.primaryCurrency}-"
        f"{i.priceMarket.secondaryCurrency}, {i.roi}",'value':i} for i in bots]

      if multi != True:
        bots = inquirer.select(

            message="Select SINGLE BOT using arrow and ENTER keys",
            choices=b2,
            ).execute()

        self.bot = bots
        self.bots = [self.bot]
        return bots


      else:
        bots = inquirer.select(

            message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
                "   Confirm selection using ENTER.",
            choices=b2,
            multiselect=True
            ).execute()
        self.bots = bots
        return bots
