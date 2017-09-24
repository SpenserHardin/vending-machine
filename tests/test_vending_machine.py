from src.vending_machine import VendingMachine
import nose.tools as nt


class TestVendingMachine:
    def test_input_coins_updates_display_when_payment_is_suffice(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.insert_payment(1)
        nt.assert_equals(vending_machine.DISPLAY, 'Thank you')

    def test_input_coins_does_not_update_display_when_payment_is_insufficient(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.insert_payment(.50)
        nt.assert_equals(vending_machine.DISPLAY, 'Insert Coins')
