from pages.catalog_page import CatalogPage

from logging_settings import get_logger

logger = get_logger(__name__)


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()


def test_catalog_not_empty(browser, items_data):
    catalog = CatalogPage(browser)
    catalog.open()
    assert len(items_data) > 0


def test_catalog_items_have_prices(browser, items_data):
    catalog = CatalogPage(browser)
    catalog.open()
    assert all([item.price for item in items_data])


# def test_active_color():
#     return
