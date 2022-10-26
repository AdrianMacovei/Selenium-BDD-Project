from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://the-internet.herokuapp.com/"

    def go_to(self, link_text):
        link_element = self.driver.find_element(By.LINK_TEXT, link_text)
        link_element.click()
