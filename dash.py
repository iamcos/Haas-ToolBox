class HaasDash(MarketData):
    def __init__(self):
        MarketData.__init__(self)

    def markets_dropdown(self):
        markets = self.get_all_markets()
        markets_dropdown = [
            {"label": str(x), "value": str(x)} for x in markets.pricesource.unique()
        ]
        return markets_dropdown

    def primarycoin_dropdown(self, pricesource):
        df = self.get_all_markets()
        pairs = df[df["pricesource"] == pricesource]

        return pairs.primarycurrency.unique()

    def secondary_coin_dropdown(self, pricesource, primarycurrency):
        df = self.get_all_markets()
        df = self.get_all_markets()
        pairs = df[df["pricesource"] == pricesource][
            df["primarycurrency"] == primarycurrency
            ]
        return pairs.secondarycurrency.unique()