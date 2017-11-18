class CoinValidator(object):
    coins = {5.670: .25, 2.268: .10, 5.000: .05, 2.5: .01}

    def determine_coin(self, coin):
        return self.coins.get(coin.weight)
