from behave import *

from src.VendingMachine import VendingMachine

use_step_matcher("re")


@given("I am a vendor")
def step_impl(context):
    pass


@when("I give the vending machine coins")
def step_impl(context):
    context.vending_machine = VendingMachine()
    context.value = context.vending_machine.insert_coins()


@then("the machine collects the money")
def step_impl(context):
    assert context.value == "Thank you for your purchase"
