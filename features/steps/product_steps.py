from behave import *
import nose.tools as nt

from features.utils.constants import COINS
from src.coin import Coin
from src.coin_validator import CoinValidator
from src.vending_machine import VendingMachine

use_step_matcher("parse")


class Chips:
    def __init__(self):
        self.price = .50


class Cola:
    def __init__(self):
        self.price = 1.00

PRODUCTS = {
    'Chips': Chips(),
    'Cola': Cola()
}


@given('I order a "{product}"')
def step_impl(context, product):
    product = PRODUCTS[product]
    validator = CoinValidator()
    context.vending_machine = VendingMachine(product, validator, product.price)


@when("I select the respective button")
def step_impl(context):
    pass


@then("the product is dispensed")
def step_impl(context):
    pass


@step('the machine displays "{msg}"')
def step_impl(context, msg):
        nt.assert_equals(context.vending_machine.DISPLAY, msg)


@step('I have inserted "{amount:d}" "{coin_type}"')
def step_impl(context, amount, coin_type):
    coin = Coin(COINS[coin_type]['weight'])
    for x in range(amount):
        context.vending_machine.insert_coins(coin)
