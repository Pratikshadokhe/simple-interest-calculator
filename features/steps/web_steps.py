@when('I click the button')
def step_impl(context):
    context.driver.find_element("id", "btn").click()

@then('I should see "{text}"')
def step_impl(context, text):
    assert text in context.driver.page_source

@then('I should not see "{text}"')
def step_impl(context, text):
    assert text not in context.driver.page_source

@then('I see message "{msg}"')
def step_impl(context, msg):
    assert msg in context.driver.page_source