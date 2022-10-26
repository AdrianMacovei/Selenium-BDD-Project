from behave import *


@given(u'I am on login page')
def step_impl(context):
    context.login_page.go_page_home()


@when(u'I enter {input_field} {value}')
def step_impl(context, input_field, value):
    if value != "None":
        context.login_page.send_value_to_input_fields(input_field, value)


@when(u'I press login button')
def step_impl(context):
    context.login_page.press_login_button()


@then(u'I will be redirected to the secure page')
def step_impl(context):
    assert context.browser.get_current_url() == context.secure_page.URL


@then(u'A message with text "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.login_page.get_flash_message_text()


@then(u'I will remain on the login page')
def step_impl(context):
    assert context.browser.get_current_url() == context.login_page.URL


@given(u'ALl steps in scenario "Login with valid/invalid credentials" are done')
def step_impl(context):
    context.execute_steps(u'''
      Given I am on login page
      When I enter "username" tomsmith
      And I enter "password" something!342
      And I press login button
      Then I will remain on the login page
      And A message with text "Your password is invalid!" appears
    ''')
