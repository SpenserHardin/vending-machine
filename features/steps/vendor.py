from behave import *

use_step_matcher("re")


@given("I am a vendor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I give the vending machien coins")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("the machine collects the money")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass