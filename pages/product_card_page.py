from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class ProductCardPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(
            browser,
            url,
            timeout=10,
            wait_by=By.XPATH,
            wait_value="//span[@class='price_value']"
        )