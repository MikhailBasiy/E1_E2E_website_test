from pages.product_card_page import ProductCardPage
import requests
import pytest

from logging_settings import get_logger

logger = get_logger(__name__)


@pytest.mark.parametrize("product_url", list(range(3)), indirect=True)
def test_product_card_price(browser, product_url):
    product_page = ProductCardPage(browser, product_url)
    product_page.open()
    product_page.get_product_data()
    