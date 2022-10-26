from behave import *
from time import sleep


@given(u'I am on the secure page')
def step_impl(context):
    context.secure_page.go_page_home()


@when(u'Page finish to load')
def step_impl(context):
    sleep(1)


@when(u'I press logout button')
def step_impl(context):
    context.secure_page.press_logout_button()


@given(u'A message with text "{text_message}" appears')
def step_impl(context, text_message):
    assert text_message in context.secure_page.get_flash_message_text()


@when(u'I press x button on the message')
def step_impl(context):
    context.secure_page.press_x_message_button()
    sleep(1)


@then(u'Message will not be displayed')
def step_impl(context):
    assert context.login_page.get_flash_message_text() == False

