from src.coin_validator import CoinValidator
from src.model.coin import Coin
from src.model.penny import Penny
from src.model.product import Product
from src.model.quarter import Quarter
from src.vending_machine import VendingMachine

THANK_YOU = 'Thank you'
INSERT_COINS = 'Insert Coins'


class TestVendingMachine(object):

    def setup(self):
        self.coin = Quarter()
        self.product = Product('Coke', .50)
        self.validator = CoinValidator()
        self.vending_machine = VendingMachine(self.product, self.validator, .50)

    def test_input_coins_updates_display_when_payment_is_suffice(self):
        product = Product('Coke', .25)
        vending_machine = VendingMachine(product, self.validator, .25)
        vending_machine.insert_coins(self.coin)
        assert vending_machine.DISPLAY == THANK_YOU

    def test_input_coins_does_not_update_display_when_payment_is_insufficient(self):
        self.vending_machine.insert_coins(self.coin)
        assert self.vending_machine.DISPLAY == INSERT_COINS

    def test_payment_attribute_is_zero_when_no_payment_has_been_made(self):
        assert self.vending_machine.PAYMENT == 0

    def test_input_coins_tracks_payment_amount(self):
        self.vending_machine.PAYMENT = .25
        self.vending_machine.insert_coins(self.coin)
        assert self.vending_machine.DISPLAY == THANK_YOU

    def test_input_coins_returns_change(self):
        expected_change = .05
        self.vending_machine.PAYMENT = .30
        actual_change = self.vending_machine.insert_coins(self.coin)
        assert actual_change == expected_change

    def test_input_coins_does_not_allow_pennies(self):
        expected_change = .01
        penny = Penny()
        actual_change = self.vending_machine.insert_coins(penny)
        assert actual_change == expected_change
        assert self.vending_machine.DISPLAY == INSERT_COINS

