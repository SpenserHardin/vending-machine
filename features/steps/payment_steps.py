import nose.tools as nt
from behave import *

from src.coin import Coin
from src.coin_validator import CoinValidator
from src.vending_machine import VendingMachine

use_step_matcher("parse")

COINS = {'.25': 5.670}

ITEM = "Item"

@given('I am a vendor')
def step_impl(context):
    pass


@given('display says "Insert Coins"')
def step_impl(context):
    pass


@given('order an item for "{price}" dollar')
def step_impl(context, price):
    validator = CoinValidator()
    context.vending_machine = VendingMachine(ITEM, validator, float(price))


@given('I purchase an item for "{price}"')
def step_impl(context, price):
    validator = CoinValidator()
    context.vending_machine = VendingMachine(ITEM, validator, float(price))


@given('I have inserted "{payment}"')
def step_impl(context, payment):
    context.vending_machine.PAYMENT = float(payment)


@when('I order an item')
def step_impl(context):
    validator = CoinValidator()
    context.vending_machine = VendingMachine(ITEM, validator)


@when('I insert "{payment}"')
def step_impl(context, payment):
    weight = COINS[payment]
    coin = Coin(weight)
    context.change = context.vending_machine.insert_coins(coin)


@when('I insert another "{payment}"')
def step_impl(context, payment):
    weight = COINS[payment]
    coin = Coin(weight)
    context.change = context.vending_machine.insert_coins(coin)


@then('the displays says "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)


@step('"{change}" cents is returned')
def step_impl(context, change):
    nt.assert_equals(context.change, float(change))
