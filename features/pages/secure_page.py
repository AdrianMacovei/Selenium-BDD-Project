from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from features.pages.login_page import LoginPage


class SecurePage(BasePage):

    URL = "https://the-internet.herokuapp.com/secure"

    def go_page_home(self):
        login_page = LoginPage(self.driver)
        login_page.go_page_home()
        login_page.send_value_to_input_fields('"username"', "tomsmith")
        login_page.send_value_to_input_fields('"password"', "SuperSecretPassword!")
        login_page.press_login_button()

    def press_logout_button(self):
        logout_selector = (By.XPATH, "//a[@href='/logout']")
        self.driver.find_element(*logout_selector).click()

    def get_page_header_text(self):
        return self.driver.find_element(By.TAG_NAME, "h2").text

    def get_flash_message_text(self):
        try:
            flash_message = self.driver.find_element(By.XPATH, "//div[@id='flash']")
            return flash_message.text
        except NoSuchElementException as e:
            return False

    def press_x_message_button(self):
        close_selector = (By.XPATH, "//a[@class='close']")
        flash_box = (By.XPATH, "//div[@id='flash-messages']")
        self.driver.find_element(*flash_box).find_element(*close_selector).click()
