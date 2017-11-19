import nose.tools as nt
from behave import *

from src.coin_validator import CoinValidator
from src.model.coin import Coin
from src.model.product import Product
from src.vending_machine import VendingMachine

use_step_matcher("parse")

COINS_VALUE = {'.25': 5.670}
COINS_DIAMETER = {5.670: 0.955}

@given('I am a vendor')
def step_impl(context):
    pass


@given('display says "Insert Coins"')
def step_impl(context):
    pass


@given('order an item for "{price}" dollar')
def step_impl(context, price):
    order_item(context, price)


@given('I purchase an item for "{price}"')
def step_impl(context, price):
    order_item(context, price)


@given('I have inserted "{payment}"')
def step_impl(context, payment):
    context.vending_machine.PAYMENT = float(payment)


def order_item(context, price):
    validator = CoinValidator()
    product = Product('Item', float(price))
    context.vending_machine = VendingMachine(product, validator, float(price))


@when("I go to order an item")
def step_impl(context):
    order_item(context, 1.00)


@when('I insert "{payment}"')
def step_impl(context, payment):
    coin = create_coin(payment)
    print(coin)
    context.change = context.vending_machine.insert_coins(coin)


@when('I insert another "{payment}"')
def step_impl(context, payment):
    coin = create_coin(payment)
    context.change = context.vending_machine.insert_coins(coin)


def create_coin(payment):
    weight = COINS_VALUE[payment]
    diameter = COINS_DIAMETER[weight]
    coin = Coin(weight, diameter)
    return coin


@then('the displays says "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)


@step('"{change}" cents is returned')
def step_impl(context, change):
    nt.assert_equals(context.change, float(change))
