from behave import *
import nose.tools as nt
from features.utils.constants import COINS
from src.coin import Coin
from src.coin_validator import CoinValidator
from src.model.product import Product
from src.vending_machine import VendingMachine

use_step_matcher("parse")


@given('I order "{product}" for "{price}"')
def step_impl(context, product, price):
    product = Product(product, float(price))
    validator = CoinValidator()
    context.vending_machine = VendingMachine(product, validator, product.price)


@when("I select the respective button")
def step_impl(context):
    pass


@when('I have inserted "{amount:d}" "{coin_type}"')
def step_impl(context, amount, coin_type):
    coin = Coin(COINS[coin_type]['weight'])
    for x in range(amount):
        context.vending_machine.insert_coins(coin)


@then("the product is dispensed")
def step_impl(context):
    pass


@then('the machine displays "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)

