from src.vending_machine import VendingMachine
import nose.tools as nt


class TestVendingMachine():
    def test_input_coins_checks_if_payment_pays_for_item(self):
        vending_machine = VendingMachine('coke', 1)
        vending_machine.insert_payment(1)
        nt.assert_equals(vending_machine.DISPLAY, 'Thank you')
