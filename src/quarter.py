from src.coin import Coin


class Quarter(Coin):
    def __init__(self, weight):
        super().__init__(weight)
        self.coin_value = .25
