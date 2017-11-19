from behave import *

from features.utils.constants import THANK_YOU, INSERT_COINS
from src.coin_validator import CoinValidator
from src.model.coin import Coin
from src.model.dime import Dime
from src.model.nickel import Nickel
from src.model.penny import Penny
from src.model.product import Product
from src.model.quarter import Quarter
from src.vending_machine import VendingMachine

use_step_matcher("parse")
coins_weight = {'Quarter': 5.670, 'Dime': 2.268, 'Nickel': 5.000, 'Penny': 2.5}
coins = {'Quarter': Quarter(), 'Dime': Dime(), 'Nickel': Nickel(), 'Penny': Penny()}


@given('I have a "{coin}"')
def step_impl(context, coin):
    context.coin = coins.get(coin)
    print(context.coin)


@when('I insert a "{payment}" into the vending machine')
def step_impl(context, payment):
    product = Product('item', context.coin.value)
    context.vending_machine = VendingMachine(product, CoinValidator(), product.price)
    coin = Coin(context.coin.weight, context.coin.diameter)
    context.vending_machine.insert_coins(coin)


@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
    assert context.vending_machine.DISPLAY == THANK_YOU


@then("the vending machine does not accepts the coin")
def step_impl(context):
    assert context.vending_machine.DISPLAY == INSERT_COINS
