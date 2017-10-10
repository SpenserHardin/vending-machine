class CoinValidator(object):
    coin_value = 0

    def determine_coin(self, coin):
        if coin.weight == 5.670:
            self.coin_value = .25
            return self.coin_value
        if coin.weight == 2.268:
            self.coin_value = .10
            return self.coin_value
        if coin.weight == 5.000:
            self.coin_value = .05
            return self.coin_value
        if coin.weight == 2.5:
            self.coin_value = .01
            return self.coin_value
