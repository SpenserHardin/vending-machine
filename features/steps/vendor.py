import nose.tools as nt
from behave import *

from src.vending_machine import VendingMachine

use_step_matcher("parse")


@given('I am a vendor')
def step_impl(context):
    pass


@given('display says "Insert Coins"')
def step_impl(context):
    pass


@given('order a "{item}" for "{price}" dollar')
def step_impl(context, item, price):
    context.vending_machine = VendingMachine(item, float(price))


@given('I purchase a "{item}" for "{price}"')
def step_impl(context, item, price):
    context.vending_machine = VendingMachine(item, float(price))


@given('I have inserted "{payment}"')
def step_impl(context, payment):
    context.vending_machine.insert_payment(float(payment))


@when('I order a "{item}"')
def step_impl(context, item):
    context.vending_machine = VendingMachine(item)


@when('I insert "{payment}"')
def step_impl(context, payment):
    context.change = context.vending_machine.insert_payment(float(payment))


@when('I insert another "{payment}"')
def step_impl(context, payment):
    context.change = context.vending_machine.insert_payment(float(payment))


@then('the displays says "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)


@step('"{change}" cents is returned')
def step_impl(context, change):
    nt.assert_equals(context.change, change)
