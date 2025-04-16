from pages.catalog_page import CatalogPage

from logging_settings import get_logger

logger = get_logger(__name__)


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()


def test_catalog_not_empty(browser):
    catalog = CatalogPage(browser)
    catalog.open()
    assert len(catalog.get_items_data()) > 0


def test_catalog_items_have_prices(browser):
    catalog = CatalogPage(browser)
    catalog.open()
    assert all([item.price for item in catalog.get_items_data()])


# def test_active_color():
#     return
