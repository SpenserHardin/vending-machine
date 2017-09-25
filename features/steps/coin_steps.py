from behave import *

use_step_matcher("parse")


@given('I have a "{coin}"')
def step_impl(context, coin):
    pass


@when('I insert a "{coin}" into the vending machine')
def step_impl(context, coin):
    pass


@then('the vending machine accepts the "{coin}"')
def step_impl(context, coin):
    pass