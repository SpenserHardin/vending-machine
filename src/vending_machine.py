class VendingMachine(object):

    DISPLAY = 'Insert Coins'

    def __init__(self, item, price=None):
        self.item = item
        self.price = price

    def insert_payment(self, payment):
        if payment == self.price:
            self.DISPLAY = 'Thank you'
