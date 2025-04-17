from pages.catalog_page import CatalogPage

from logging_settings import get_logger

logger = get_logger(__name__)


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()

def test_catalog_not_empty(items_data):
    assert len(items_data) > 0

def test_catalog_items_have_prices(items_data):
    assert all([item.price for item in items_data])

# def test_catalog_items_have_valid_href(items_data):
#     pass




# def test_active_color():
#     return
