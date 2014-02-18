@when(u'I go to the tip calculator')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000')

@then(u'I should see the calculator form')
def step_impl(context):
    assert context.browser.title == "Tip Calculator"
@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
    br = context.browser
    br.get('http://127.0.0.1:5000')
    meal_cost = br.find_element_by_name("meal_cost")
    meal_cost.send_keys("30")
    tip_percentage = br.find_element_by_name("tip_percentage")
    tip_percentage.send_keys("20")
    br.find_element_by_id("submit").click()

@then(u'I should see the results page')
def step_impl(context):
    br = context.browse
    assert br.find_element_by_id('results')

