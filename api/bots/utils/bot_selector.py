from InquirerPy import inquirer
from api.MainContext import config_manager


class BotSellector:

    def bot_selector(self, botType, multi=False):
        bots: list = [x for x in config_manager.customBotApi.get_all_custom_bots(
        ).result if x.botType == botType]

        bots.sort(key=lambda x: x.name, reverse=False)

        name: str = """{i.name} {i.priceMarket.primaryCurrency}-{i.priceMarket.secondaryCurrency}, {i.roi}"""
        bots_by_name: list = [{'name': name.format(i=i), 'value': i} for i in bots]

        if not multi:
            bots = inquirer.select(
                message="Select SINGLE BOT using arrow and ENTER keys",
                choices=bots_by_name,
            ).execute()

            return bots

        else:
            bots = inquirer.select(
                message="Select MULTIPLE BOTS (or just one) using SPACEBAR.\n"
                "   Confirm selection using ENTER.",
                choices=bots_by_name,
                multiselect=True
            ).execute()

            return bots
