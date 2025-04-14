from pages.catalog_page import CatalogPage


def test_open_catalog(browser):
    catalog = CatalogPage(browser)
    catalog.open()


def test_catalog_not_empty(browser):
    catalog = CatalogPage(browser)
    catalog.open()
    assert len(catalog.get_catalog_items()) > 0



# def test_active_color():
#     return