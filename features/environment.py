from browser import Chrome, Firefox, Edge
from pages.drop_down_page import DropDownPage
from pages.forgot_pwd_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def before_all(context):
    chosen_browser = input("Chose the browser you want to use for test (Chrome, Firefox, Edge):\n")
    if chosen_browser == "Chrome":
        context.browser = Chrome()
    elif chosen_browser == "Firefox":
        context.browser = Firefox()
    elif chosen_browser == "Edge":
        context.browser = Edge()

    context.home_page = HomePage(context.browser.driver)
    context.login_page = LoginPage(context.browser.driver)
    context.forgot_pwd_page = ForgotPasswordPage(context.browser.driver)
    context.secure_page = SecurePage(context.browser.driver)
    context.drop_down_page = DropDownPage(context.browser.driver)


def after_all(context):
    context.browser.close()
