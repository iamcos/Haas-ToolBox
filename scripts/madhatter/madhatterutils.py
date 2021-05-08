def set_ranges(self):
        class UtilClass:
            pass

        ranges = UtilClass()
        ranges.bot = UtilClass()
        ranges.indicators = UtilClass()
        ranges.safeties = UtilClass()

        interval = [
            1,
            2,
            3,
            4,
            5,
            6,
            10,
            12,
            15,
            20,
            30,
            45,
            60,
            90,
            120,
            150,
            180,
            240,
            300,
            600,
            1200,
            2400,
        ]

        signalconsensus = allowmidsells = resetmiddle = requirefcc = True, False

        stoploss = 0.5, 5.0, 0.1
        intervals = UtilClass()
        intervals.list = interval

        ranges.bot.intervals = intervals
        ranges.bot.signalconsensus = signalconsensus

        bBands = UtilClass()
        bBands.matype = 0, 9, 1
        bBands.length = 7, 9, 1
        bBands.devup = 1.0, 1.2, 0.1
        bBands.devdown = 1.0, 1.2, 0.1

        rsi = UtilClass()
        rsi.length = 2, 21, 1
        rsi.buy = 51, 99, 1
        rsi.sell = 2, 49, 1

        macd = UtilClass()
        macd.fast = 2, 59, 1
        macd.slow = 40, 80, 1
        macd.signal = 3, 21, 1

        ranges.indicators.bBands = bBands
        ranges.indicators.rsi = rsi
        ranges.indicators.macd = macd
        ranges.safeties.stoploss = stoploss

        self.ranges = ranges

        return ranges