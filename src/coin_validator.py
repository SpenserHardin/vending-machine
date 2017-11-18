from src.model.quarter import Quarter


class CoinValidator:
    coins = {5.670: .25, 2.268: .10, 5.000: .05, 2.5: .01}

    def determine_coin(self, coin):
        return self.coins.get(coin.weight)

    @staticmethod
    def calculate_coin(coin):
        if (coin.weight == Quarter.weight) & (coin.diameter == Quarter.diameter):
            return Quarter()
        else:
            return "UnIdentified Coin"

