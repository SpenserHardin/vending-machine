from src.dime import Dime
from src.nickel import Nickel
from src.penny import Penny
from src.quarter import Quarter


class CoinValidator(object):
    coins = {5.670: 'quarter', 2.268: 'dime', 5.000: 'nickel', 2.5: 'penny'}

    def determine_coin(self, coin):
        coin_type = self.coins.get(coin.weight)
        if coin_type == 'quarter':
            return Quarter(coin.weight)
        if coin_type == 'dime':
            return Dime(coin.weight)
        if coin_type == 'nickel':
            return Nickel(coin.weight)
        else:
            return Penny(coin.weight)
