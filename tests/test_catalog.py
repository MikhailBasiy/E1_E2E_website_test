from logging_settings import get_logger
from pages.catalog_page import CatalogPage

logger = get_logger(__name__)


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()


def test_catalog_not_empty(catalog_items):
    assert len(catalog_items) > 0


def test_catalog_items_have_prices(catalog_items):
    assert all([item.price for item in catalog_items])


# def test_catalog_items_have_valid_href(items_data):
#     pass


# def test_active_color():
#     return
