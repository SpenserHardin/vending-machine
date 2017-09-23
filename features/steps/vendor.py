from behave import *

from src.VendingMachine import VendingMachine

use_step_matcher("re")

MESSAGE = ''


@given("I am a vendor")
def step_impl(context):
    pass


@when("I give the vending machine coins")
def step_impl(context):
    vending_machine = VendingMachine()
    MESSAGE = vending_machine.insert_coins()


@then("the machine collects the money")
def step_impl(context):
    assert MESSAGE == "Thank you for your purchase"
