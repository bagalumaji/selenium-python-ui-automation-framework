import pytest

from config.config_reader import ConfigReader
from driver.driver import Driver
from enums.browser import Browser
from exceptions.browser_not_supported_exception import BrowserNotSupportedException

@pytest.fixture()
def setup_and_teardown():
    config = ConfigReader()
    Driver.init_driver(get_browser(config.browser()))
    yield
    Driver.quit_driver()

def get_browser(browser_name) -> Browser:
    try:
        browser = Browser(browser_name)
        return browser
    except Exception:
        raise BrowserNotSupportedException(browser_name)