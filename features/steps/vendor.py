import nose.tools as nt
from behave import *

from src.VendingMachine import VendingMachine

use_step_matcher("parse")


@given('I am a vendor')
def step_impl(context):
    pass


@given('order a "{item}" for "{price}" dollar')
def step_impl(context, item, price):
    pass


@when('I order a "{item}"')
def step_impl(context, item):
    context.vending_machine = VendingMachine(item)
    print(type(context.vending_machine))


@when('I insert "{payment}" dollar')
def step_impl(context, payment):
    pass


@then('the displays says "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)
