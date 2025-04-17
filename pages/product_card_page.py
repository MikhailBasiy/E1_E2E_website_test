from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logging_settings import get_logger

logger = get_logger(__name__)


class ProductCardPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(
            browser,
            url,
            timeout=15,
            wait_by=By.XPATH,
            wait_value="//div[@class='price font-bold font_mxs']//span[@class='price_value']" # "//div[@class='prices_block']//div[contains(@class, 'price')]"
        )

    def get_product_data(self):
        price = self.browser.find_element(By.XPATH, "//div[@class='price font-bold font_mxs']//span[@class='price_value']").text
        price = re.sub(r"\D", "", price)
        logger.debug(f"{self.url}, {price}")