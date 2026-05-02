@given('the following products')
def step_impl(context):
    context.products = context.table
