from src.Quarter import Quarter


class CoinValidator(object):
    coins = {5.670: 'quarter', 2.268: .10, 5.000: .05, 2.5: .01}

    def determine_coin(self, coin):
        value = self.coins.get(coin.weight)
        if value == 'quarter':
            my_coin = Quarter(coin.weight)
            return my_coin.coin_value
        else:
            return value
