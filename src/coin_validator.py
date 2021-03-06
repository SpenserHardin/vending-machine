from src.model.dime import Dime
from src.model.nickel import Nickel
from src.model.penny import Penny
from src.model.quarter import Quarter


class CoinValidator:
    coins = {5.670: .25, 2.268: .10, 5.000: .05, 2.5: .01}

    def determine_coin(self, coin):
        return self.coins.get(coin.weight)

    @staticmethod
    def calculate_coin(coin):
        if (coin.weight == Quarter.weight) & (coin.diameter == Quarter.diameter):
            return Quarter()
        if (coin.weight == Dime.weight) & (coin.diameter == Dime.diameter):
            return Dime()
        if (coin.weight == Nickel.weight) & (coin.diameter == Nickel.diameter):
            return Nickel()
        if (coin.weight == Penny.weight) & (coin.diameter == Penny.diameter):
            return Penny()
        else:
            return "UnIdentified Coin"

