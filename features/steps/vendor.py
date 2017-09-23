import nose.tools as nt
from behave import *

from src.VendingMachine import VendingMachine

use_step_matcher("parse")


@given('I am a vendor')
def step_impl(context):
    pass


@when('I order a "{item}"')
def step_impl(context, item):
    context.vending_machine = VendingMachine(item)
    print(type(context.vending_machine))


@then('the displays says "{msg}"')
def step_impl(context, msg):
    nt.assert_equals(context.vending_machine.DISPLAY, msg)
