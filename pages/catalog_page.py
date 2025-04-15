import re
from collections import namedtuple

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from logging_settings import get_logger


logger = get_logger(__name__)


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(
            browser,
            url="https://www.e-1.ru/catalog/vse_shkafy_kupe/",
            timeout=10,
            wait_by=By.XPATH,
            wait_value="//div[@class='price font-bold font_mxs']//span[@class='price_value']",
        )

    def get_catalog_items(self):
        Item = namedtuple("Item", ["title", "price"])
        items_lst = []
        items = self.find_all(
            10,
            By.XPATH,
            "//div[@class='price font-bold font_mxs']//span[@class='price_value']",
        )
        for item in items:
            logger.debug(f"{item}")
            price = item.find_element(
                By.XPATH,
                "//div[contains(@class, 'price') and contains(@class, 'font-bold')]",
            ).text
            logger.debug(f"price is {price}")
            title = item.find_element(
                By.XPATH, "//img[contains(@class, 'img-responsive')]"
            ).get_attribute("title")
            logger.debug(f"title is {title}")
            price = re.search(r"\d", price)
            i = Item(title=title, price=price)
            items_lst.append(i)
        return items_lst

    # def next_page(self):
    #     try:
    #         WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
    #             (By.Class, "flex-next")
    #         )).click()
    #     except NoSuchElementException:
