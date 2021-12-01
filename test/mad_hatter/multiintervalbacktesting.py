# backtest 1 day, get the best results.
# backtest 3 days, get good results but keep one day same or better.
# backtest 7 days, get good results but keep 3 days and one day same or better.
# backtest 2 weeks, get good results but keep the rest at par.
# if higher results worse - find good config by doing a random search by changing a single parameter at a time for a few steps here and there.
# take into account multipe configs with similar results.
# if better not possible, go down one level and optimize more on it, then go higher.


class BacktestingManager:
    def __init__(self):
        pass

    def assest_current_state(self):
        pass

    def add_new_backtesting_interval(self):
        pass

    def store_results(self):
        pass

    def choose_next_indicator(self):
        pass

    def choose_next_parameter(self):
        pass

    def edit_parameter(self):
        pass

    def define_parameter_field(self, indicators):
        field = []
        for indicator in indicators:
            for param in indicator:
                param = {indicator.guid: {param.title: param.value}}
                field.append(param)

    def backtesting_logic(self):
        pass

    def estimate_possible_profits(self):
        pass
