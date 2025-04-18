import pytest
import requests

from logging_settings import get_logger
from pages.product_card_page import ProductCardPage

logger = get_logger(__name__)


# @pytest.mark.parametrize("item", list(range(20)), indirect=True) ###TODO: testing simple opening pages () using requests lib
# def test_product_card_pages_open(item):
#     assert


@pytest.mark.parametrize("catalog_item", list(range(3)), indirect=True)
def test_product_card_data(browser, catalog_item):
    product_page = ProductCardPage(browser, catalog_item.href)
    product_page.open()
    product_page.get_product_data()
    product_page.compare_titles(catalog_item.title)
    product_page.compare_prices(catalog_item.price, catalog_item.price_discount)
    product_page.compare_case_colors(catalog_item.color_active)
