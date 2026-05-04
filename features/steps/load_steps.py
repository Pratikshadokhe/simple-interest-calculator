from behave import given
from tests.factories import ProductFactory

@given('products exist')
def step_impl(context):
    context.products = [ProductFactory() for _ in range(3)]