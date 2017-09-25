class VendingMachine(object):

    DISPLAY = 'Insert Coins'
    PAYMENT = 0

    def __init__(self, item, price=None):
        self.item = item
        self.price = price

    def insert_coins(self, payment):
        self.PAYMENT += payment
        if self._payment_is_sufficient():
            self._update_display()
            return self._calculate_change()

    def _calculate_change(self):
        return self.PAYMENT - self.price

    def _payment_is_sufficient(self):
        return self.PAYMENT >= self.price

    def _update_display(self):
        self.DISPLAY = 'Thank you'
