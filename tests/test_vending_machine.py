from src.vending_machine import VendingMachine


class TestVendingMachine(object):
    def test_input_coins_updates_display_when_payment_is_suffice(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.insert_payment(1)
        assert vending_machine.DISPLAY == 'Thank you'

    def test_input_coins_does_not_update_display_when_payment_is_insufficient(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.insert_payment(.50)
        assert vending_machine.DISPLAY == 'Insert Coins'

    def test_payment_attribute_is_zero_when_no_payment_has_been_made(self):
        vending_machine = VendingMachine('coke', 1)
        assert vending_machine.PAYMENT == 0

    def test_input_coins_tracks_payment_amount(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.PAYMENT = .50
        vending_machine.insert_payment(.50)
        assert vending_machine.DISPLAY == 'Thank you'

    def test_input_coins_returns_change(self):
        expected_change = .25
        vending_machine = VendingMachine('coke', 1)
        vending_machine.PAYMENT = .75
        actual_change = vending_machine.insert_payment(.50)
        assert actual_change == expected_change
