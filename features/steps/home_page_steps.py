from behave import *


@given(u'I am on home page')
def step_impl(context):
    context.home_page.go_page_home()


@when(u'I press {name} link')
def step_impl(context, name):
    context.home_page.go_to(name)


@then(u'I am redirected to {name_of} page')
def step_impl(context, name_of):
    assert context.browser.get_current_url() == f"https://the-internet.herokuapp.com/{name_of}"


@then(u'The title text is {page_title}')
def step_impl(context, page_title):
    if page_title == "Login Page":
        assert context.login_page.get_page_header_text() == page_title
    elif page_title == "Forgot Password":
        assert context.forgot_pwd_page.get_page_header_text() == page_title
    elif page_title == "Dropdown List":
        assert context.drop_down_page.get_page_header_text() == page_title
    elif page_title == " Secure Area":
        assert context.secure_page.get_page_header_text == page_title
