    def setup_indicator(self):
        setup = self.tradebotapi.setup_indicator(
            self.tradebot.guid,
            self.indicator.guid,
            self.tradebot.priceMarket,
            self.tradebot.priceMarket.primaryCurrency,
            self.tradebot.priceMarket.secondaryCurrency,
            self.tradebot.priceMarket.contractName,
            self.indicator.timer,
            self.indicator.chartType,
            self.indicator.deviation,
        )
        print(
            f"Indicator setup was a {setup.errorCode.value}, {setup.errorMessage.value}"
        )

    def add_indicator(self):

        add = self.tradebotapi.add_indicator(self.tradebot.guid, self.indicator)
        if add.result:
            print(
                "Indicator",
                EnumIndicator(self.indicator).name,
                " added to ",
                self.tradebot.name,
            )
        else:
            print("Adding indicator didn't work out")

    def remove_indicator(self, bot, indicator):
        failed = []
        try:
            add = self.c.tradeBotApi.remove_indicator(bot.guid, indicator.guid)
            if add.result:
                print(
                    "Indicator",
                    EnumIndicator(indicator).value,
                    " removed from ",
                    bot.name,
                )
            else:
                print("Removing indicator didn't work out")

        except:
            failed.append(indicator)
        return failed

    def remove_indicators(self, bot, indicator_list):
        for x in indicator_list:
            self.remove_indicator(bot, x)

    def add_multiple_indicators(self, bot, indicators):
        for x in indicators:
            self.add_indicator(bot, x)

    def add_all_indicators(self, bot):
        indicators = [x for x in range(71)]
        self.add_multiple_indicators(bot, indicators)

    def remove_all_indicators(self, bot):
        indicators = t.get_indicators(bot)
        self.remove_indicators(bot, indicators)