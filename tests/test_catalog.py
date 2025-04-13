from pages.catalog_page import CatalogPage


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()


# def test_items_shown 