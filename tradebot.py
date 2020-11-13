from haasomeapi.enums.EnumIndicator import EnumIndicator

class TradeBot(Haas):
    def __init__(self):
        Haas.__init__(self)
        self.config = Haas().config
        self.c = HaasomeClient(self.ip, self.secret)
        self.ticks = Haas().read_ticks()

    def return_bot(self, guid):
        bot = self.c.tradeBotApi.get_trade_bot(guid).result
        return bot

    def get_indicators(self, bot):
        """
        returns all tradebot indicators as a list
        """

        idd = list([bot.indicators[x] for x in bot.indicators])
        return idd

    def select_indicator(self, indicators):

        for i, b in enumerate(indicators):
            print(i, indicators[i].indicatorTypeFullName)
        uip = input("Select indicator")

        indicator = indicators[int(uip)]
        print("select indicator", indicator)
        return indicator

    def setup_indicator(self, bot, indicator):
        setup = self.c.TradeBotApi.setup_indicator(
            bot.guid,
            indicator.guid,
            bot.priceMarket,
            bot.priceMarket.primaryCurrency,
            bot.priceMarket.secondaryCurrency,
            bot.priceMarket.contractName,
            indicator.timer,
            indicator.chartType,
            indicator.deviation,
        )
        print(
            f"Indicator setup was a {setup.errorCode.value}, {setup.errorMessage.value}"
        )

    def get_interfaces(self, bot, indicator):

        interfaces = []
        for interface in bot.indicators[indicator.guid].indicatorInterface:
            interfaces.append(
                {
                    "title": interface.title,
                    "value": interface.value,
                    "options": interface.options,
                    "step": interface.step,
                }
            )

        return interfaces

    def get_full_interfaces(self, bot, indicator):
        interfaces = {}
        for interface in bot.indicators[indicator.guid].indicatorInterface:
            interfaces[
                EnumIndicator(bot.indicators[indicator.guid].indicatorType).name
            ] = self.dict_from_class(interface)

        return interfaces

    def get_enums_for_indicators(self, bot):
        icc = ic()
        indicators_enums = {}
        for indicator in bot.indicators:
            indicator_enum = icc().get_indicator_enum_data(
                bot.indicators[indicator].indicatorInterface.indicatorType
            )
            indicators.append(indicator_enum)
        return indicators_enums

        return indicators

    def add_indicator(self, bot, indicator):
        failed = []
        try:
            add = self.c.tradeBotApi.add_indicator(bot.guid, indicator)
            if add.result:
                print(
                    "Indicator", EnumIndicator(indicator).name, " added to ", bot.name
                )
            else:
                print("Adding indicator didn't work out")

        except:
            failed.append(indicator)
        return failed

    def edit_indicator(self, bot, indicator, field, value):
        print(indicator)
        indicator_config = self.c.tradeBotApi.edit_bot_indicator_settings(
            bot.guid, indicator.guid, field, value
        )
        interfaces = self.get_interfaces(bot, indicator)
        return indicator_config

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

    def select_bot_get_indicator(self, bot):
        indicators = self.get_indicators(bot)
        indicator = self.select_indicator(indicators)
        return indicator


