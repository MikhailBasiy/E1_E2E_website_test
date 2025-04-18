import re
from collections import namedtuple

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logging_settings import get_logger
from models import CatalogItem
from pages.base_page import BasePage

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

    def get_items_data(self):
        items_data: list[namedtuple] = []
        items = self.browser.find_elements(
            By.XPATH, "//div[contains(@class, 'inner_content')]"
        )
        for item in items:
            title = item.find_element(
                By.XPATH, ".//img[contains(@class, 'img-responsive')]"
            ).get_attribute("title")
            # logger.debug(f"title is {title}")
            prices = item.find_elements(
                By.XPATH,
                ".//span[@class='price_value']",
            )
            price, price_discount = [re.sub(r"/D", "", el.text) for el in prices]
            # logger.debug(f"price is {price}")
            # logger.debug(f"price_discount is {price_discount}")

            href = item.find_element(
                By.XPATH, ".//div[@class='item-title']/a"
            ).get_attribute("href")
            # logger.debug(f"href is {href}")
            color_active = item.find_element(
                By.XPATH,
                ".//ul[@class='list_values_wrapper']/li[@class='item active']/i",
            ).get_attribute("title")
            color_active = re.sub("Цвет корпуса: ", "", color_active)
            # logger.debug(f"color_active is {color_active}")

            i = CatalogItem(title, href, price, price_discount, color_active)
            items_data.append(i)
        return items_data

    # def next_page(self):
    #     try:
    #         WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
    #             (By.Class, "flex-next")
    #         )).click()
    #     except NoSuchElementException:
