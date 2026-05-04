from behave import when, then

@when('I click a button')
def step_impl(context):
    pass

@then('I should see text')
def step_impl(context):
    assert True

@then('I should not see text')
def step_impl(context):
    assert True

@then('I should see a message')
def step_impl(context):
    assert True