from behave import *
import nose.tools as nt

from src.coin import Coin
from src.coin_validator import CoinValidator
from src.vending_machine import VendingMachine

use_step_matcher("parse")

COINS = {'Quarter': {'weight': 5.670, 'value': .25},
         'Dime': {'weight': 2.268, 'value': .10},
         'Nickle': {'weight': 5.000, 'value': .05},
         'Penny': {'weight': 2.5, 'value': .01}}


class Chips:
    def __init__(self):
        self.price = .50


PRODUCTS = {
    'Chips': Chips()
}

@given('I order a "{product}"')
def step_impl(context, product):
    product = PRODUCTS[product]
    validator = CoinValidator()
    context.vending_machine = VendingMachine(product, validator, product.price)


@when("I select the respective button")
def step_impl(context):
    pass


@step("I have inserted enough money")
def step_impl(context):
    coin = Coin(COINS['Quarter']['weight'])
    context.change = context.vending_machine.insert_coins(coin)
    context.change = context.vending_machine.insert_coins(coin)


@then("the product is dispensed")
def step_impl(context):
    pass


@step('the machine displays "{msg}"')
def step_impl(context, msg):
        nt.assert_equals(context.vending_machine.DISPLAY, msg)
