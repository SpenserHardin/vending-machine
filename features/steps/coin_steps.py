from behave import *

from src.vending_machine import VendingMachine

use_step_matcher("parse")

THANK_YOU = 'Thank you'


@given('I have a "{coin}"')
def step_impl(context, coin):
    context.quarter = '5.670'


@when('I insert a "{coin}" into the vending machine')
def step_impl(context, coin):
    context.vending_machine = VendingMachine('item', .25)
    context.vending_machine.insert_coins(coin)


@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
    assert context.vending_machine.DISPLAY == THANK_YOU
