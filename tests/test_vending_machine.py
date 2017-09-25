from src.vending_machine import VendingMachine

THANK_YOU = 'Thank you'
INSERT_COINS = 'Insert Coins'


class TestVendingMachine(object):

    def setup(self):
        self.vending_machine = VendingMachine('Coke', 1)

    def test_input_coins_updates_display_when_payment_is_suffice(self):
        self.vending_machine.insert_coins(1)
        assert self.vending_machine.DISPLAY == THANK_YOU

    def test_input_coins_does_not_update_display_when_payment_is_insufficient(self):
        self.vending_machine.insert_coins(.50)
        assert self.vending_machine.DISPLAY == INSERT_COINS

    def test_payment_attribute_is_zero_when_no_payment_has_been_made(self):
        assert self.vending_machine.PAYMENT == 0

    def test_input_coins_tracks_payment_amount(self):
        self.vending_machine.PAYMENT = .50
        self.vending_machine.insert_coins(.50)
        assert self.vending_machine.DISPLAY == THANK_YOU

    def test_input_coins_returns_change(self):
        expected_change = .25
        self.vending_machine.PAYMENT = .75
        actual_change = self.vending_machine.insert_coins(.50)
        assert actual_change == expected_change
