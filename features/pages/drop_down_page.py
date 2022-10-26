from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class DropDownPage(BasePage):

    URL = "https://the-internet.herokuapp.com/dropdown"


    def get_page_header_text(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text