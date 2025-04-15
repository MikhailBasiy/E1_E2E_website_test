from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout, wait_by, wait_value):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.wait_by = wait_by
        self.wait_value = wait_value

    def open(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_all_elements_located((self.wait_by, self.wait_value))
        )

    def find(self, timeout, by, value):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def find_all(self, timeout, by, value):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )
