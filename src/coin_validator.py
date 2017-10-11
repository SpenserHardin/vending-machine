class CoinValidator(object):
    @staticmethod
    def determine_coin(coin):
        if coin.weight == 5.670:
            return Quarter.coin_value
        if coin.weight == 2.268:
            return Dime.coin_value
        if coin.weight == 5.000:
            return Nickel.coin_value
        if coin.weight == 2.5:
            return Penny.coin_value


class Quarter(object):
    coin_value = .25


class Dime(object):
    coin_value = .10


class Nickel(object):
    coin_value = .05


class Penny(object):
    coin_value = .01
