from behave import *

from src.coin import Coin
from src.coin_validator import CoinValidator
from src.vending_machine import VendingMachine

use_step_matcher("parse")

THANK_YOU = 'Thank you'
COINS = {'Quarter': {'weight': 5.670, 'value': .25},
         'Dime': {'weight': 2.268, 'value': .10}}


@given('I have a "{coin}"')
def step_impl(context, coin):
    context.quarter = '5.670'


@when('I insert a "{payment}" into the vending machine')
def step_impl(context, payment):
    coin = Coin(COINS[payment]['weight'])
    validator = CoinValidator()
    context.vending_machine = VendingMachine('item', validator, COINS[payment]['value'])
    context.vending_machine.insert_coins(coin)


@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
    assert context.vending_machine.DISPLAY == THANK_YOU
