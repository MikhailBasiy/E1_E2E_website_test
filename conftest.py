from collections import namedtuple

import pytest
from selenium import webdriver

from pages.catalog_page import CatalogPage
from pages.product_card_page import ProductCardPage


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "none"
    options.add_argument("--blink-settings=imagesEnabled=false")
    # options.add_argument('--headless=new')
    options.add_argument("log-level=3")
    # options.add_argument('--disable-gpu')                 # for docker container
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def catalog_items(browser):
    catalog_page = CatalogPage(browser)
    catalog_items: list[namedtuple] = catalog_page.get_items_data()
    return catalog_items


@pytest.fixture()
def catalog_item(request, catalog_items):
    return catalog_items[request.param]


# @pytest.fixture(scope="session")
# def product_data():
#     product_page = ProductCardPage()
#     return product_page.get_product_data()
