from src.model.penny import Penny


class VendingMachine(object):

    DISPLAY = 'Insert Coins'
    PAYMENT = 0.0

    def __init__(self, item, validator, price=None):
        self.item = item
        self.price = price
        self.validator = validator

    def insert_coins(self, coin):
        identified_coin = self.validator.calculate_coin(coin)
        if not isinstance(identified_coin, Penny):
            self.PAYMENT += identified_coin.value
            if self._payment_is_sufficient():
                self._update_display()
                return self._calculate_change()
        else:
            return identified_coin.value

    def _calculate_change(self):
        return round(self.PAYMENT - self.item.price, 2)

    def _payment_is_sufficient(self):
        return self.PAYMENT >= self.item.price

    def _update_display(self):
        self.DISPLAY = 'Thank you'
