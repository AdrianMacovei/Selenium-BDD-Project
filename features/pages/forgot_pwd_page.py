from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    URL = "https://the-internet.herokuapp.com/forgot_password"

    def get_page_header_text(self):
        return self.driver.find_element(By.TAG_NAME, "h2").text
