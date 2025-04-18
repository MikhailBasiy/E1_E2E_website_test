import re

from selenium.webdriver.common.by import By

from logging_settings import get_logger
from pages.base_page import BasePage
from models import ProductPageItem

logger = get_logger(__name__)


class ProductCardPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(
            browser,
            url,
            timeout=30,
            wait_by=By.XPATH,
            wait_value="//div[@class='price font-bold font_mxs']//span[@class='price_value']",
        )

    def get_product_data(self):
        title = self.browser.find_element(
            By.XPATH, "//img[@class='product-detail-gallery__picture']"
        ).get_attribute("title")

        prices = self.browser.find_elements(
            By.XPATH,
            ".//span[@class='price_value']",
        )[
            :2
        ]  # there're 30 elements
        price, price_discount = [re.sub(r"/D", "", el.text) for el in prices]

        product_props = self.browser.find_elements(
            By.XPATH,
            "//div[@class='product-param-choose-block bx_catalog_item_scu_block']//li[@class='active']/i",
        )[
            3:
        ]  # to skip useless tags
        logger.debug(len(product_props))
        color_active, profile_color, layout = [
            el.get_attribute("title").split(": ")[1]
            for el in product_props  # "Цвет профиля: Серебро профиль", "Компоновка: Прайм 2х"
        ]

        self.i = ProductPageItem(
            title, price, price_discount, color_active, profile_color, layout
        )
        # logger.debug(f"{self.url}, {title}")
        # logger.debug(f"{self.url}, {price}")
        # logger.debug(f"{self.url}, {price_discount}")
        logger.debug(f"{color_active}, {profile_color}, {layout}")

    def compare_titles(self, title_in_catalog):
        assert (
            self.i.title == title_in_catalog
        ), f"Названия в карточке ({self.i.title}) и в каталоге ({title_in_catalog}) не совпадают"

    def compare_prices(self, price_in_catalog, price_discount_in_catalog):
        assert (
            self.i.price == price_in_catalog
        ), f"Цены в карточке ({self.i.price}) и в каталоге ({price_in_catalog}) не совпадают"
        assert (
            self.i.price_discount == price_discount_in_catalog
        ), f"Цены в карточке ({self.i.price_discount}) и в каталоге ({price_discount_in_catalog}) не совпадают"

    def compare_case_colors(self, case_color_in_catalog):
        assert (
            self.i.color_active == case_color_in_catalog
        ), f"Цвета корпуса в карточке ({self.i.color_active}) и в каталоге ({case_color_in_catalog}) не совпадают"
