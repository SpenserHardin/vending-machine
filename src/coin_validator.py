from src.dime import Dime
from src.nickel import Nickel
from src.penny import Penny
from src.quarter import Quarter


class CoinValidator(object):
    coins = {5.670: 'quarter', 2.268: 'dime', 5.000: 'nickel', 2.5: 'penny'}

    def determine_coin(self, coin):
        coin_type = self.coins.get(coin.weight)
        if coin_type == 'quarter':
            my_coin = Quarter(coin.weight)
            return my_coin.coin_value
        if coin_type == 'dime':
            my_coin = Dime(coin.weight)
            return my_coin.coin_value
        if coin_type == 'nickel':
            my_coin = Nickel(coin.weight)
            return my_coin.coin_value
        else:
            my_coin = Penny(coin.weight)
            return my_coin.coin_value
