from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logging_settings import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, browser, url, timeout, wait_by, wait_value):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.wait_by = wait_by
        self.wait_value = wait_value

    def open(self):
        self.browser.get(self.url)
        wait = WebDriverWait(self.browser, self.timeout)
        wait.until(self._tag_has_correct_value)

        WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_all_elements_located((self.wait_by, self.wait_value))
        )
        logger.debug(f"{self.url} sucessfully downloaded")

    def _tag_has_correct_value(self, browser):
        try:
            el = self.browser.find_element(self.wait_by, self.wait_value)
            return el.text not in ("", "0")
        except Exception:
            return False
