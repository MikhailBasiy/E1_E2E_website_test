import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'none'
    # options.add_argument('--ignore-certificate-errors')   # Check if it works
    # options.add_argument('--ignore-ssl-errors')           # Check if it works
    options.add_argument('--blink-settings=imagesEnabled=false')
    # options.add_argument('--headless=new')
    options.add_argument('log-level=3')
    # options.add_argument('--disable-gpu')                 # for docker container
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()