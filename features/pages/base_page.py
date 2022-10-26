
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_page_home(self):
        self.driver.get(self.URL)
        