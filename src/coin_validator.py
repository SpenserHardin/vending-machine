class CoinValidator(object):
    @staticmethod
    def determine_coin(coin):
        if coin.weight == 5.670:
            return .25
        if coin.weight == 2.268:
            return .10
