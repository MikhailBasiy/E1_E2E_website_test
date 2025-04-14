from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, \
                                       StaleElementReferenceException, \
                                       TimeoutException, \
                                       WebDriverException 

from pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(
            browser, 
            "https://www.e-1.ru/catalog/vse_shkafy_kupe/",
            (
                By.XPATH, 
                "//div[@class='price font-bold font_mxs'//span[@class='price_value']"
            )
        )

    def get_catalog_items(self):
        return self.find_all(
            10, 
            By.XPATH, 
            "//div[@class='price font-bold font_mxs']//span[@class='price_value']"
        )
         
    
    # def next_page(self):
    #     try:
    #         WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
    #             (By.Class, "flex-next")
    #         )).click()
    #     except NoSuchElementException:
    