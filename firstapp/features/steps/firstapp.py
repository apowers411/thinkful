@when(u'I go to the home page')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see the front page')
def step_impl(context):
    assert context.browser.title == "Who's talking"
    