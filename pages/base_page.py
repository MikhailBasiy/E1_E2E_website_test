from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, *load_args):
        self.browser = browser
        self.url = url
        self.load_args = load_args

    def open(self):
        self.browser.get(self.url)

    def find(self, timeout, by, value):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.presence_of_element_located((by, value)))
    
    def find_all(self, timeout, by, value):
        return WebDriverWait(self.browser, timeout) \
            .until(EC.presence_of_all_elements_located((by, value)))
        