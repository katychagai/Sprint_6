import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from src.config import get_settings
from src.pages.home_faq_page import HomeFaqPage


@pytest.fixture(scope="session")
def settings():
    return get_settings()


@pytest.fixture
def driver(settings):
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(settings.page_load_timeout)
    
    yield driver
    driver.quit()


@pytest.fixture
def faq_page(driver, settings):
    page = HomeFaqPage(driver, settings.base_url)
    page.open_faq()
    return page