from src.coin import Coin


class Dime(Coin):
    def __init__(self, weight):
        super().__init__(weight)
        self.coin_value = .10
