import pytest
from selenium import webdriver
from collections import namedtuple
from pages.catalog_page import CatalogPage


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
def items_data(browser):
    catalog_page = CatalogPage(browser)
    items_data: list[namedtuple] = catalog_page.get_items_data()
    return items_data


@pytest.fixture()
def product_url(request, items_data):
    return items_data[request.param].href
