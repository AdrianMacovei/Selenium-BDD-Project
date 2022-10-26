from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    def send_value_to_input_fields(self, field_name, value):
        input_selector = (By.XPATH, f"//input[@id={field_name}]")
        self.driver.find_element(*input_selector).send_keys(value)

    def press_login_button(self):
        login_selector = (By.XPATH, "//i[contains(text(),'Login')]")
        self.driver.find_element(*login_selector).click()

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

