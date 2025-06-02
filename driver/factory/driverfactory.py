import logging

from selenium import webdriver

from enums.browser import Browser

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverFactory:
    _driver_factory = {
        Browser.CHROME: lambda: webdriver.Chrome(),
        Browser.FIREFOX: lambda: webdriver.Firefox()
    }

    @classmethod
    def get_driver(cls, browser: Browser):
        try:
            driver = cls._driver_factory.get(browser)()
            logger.info(f"{browser.name} driver created successfully.")
            return driver
        except TypeError:
            logger.error(f"No driver found for browser: {browser.name}")
            raise ValueError(f"No driver found for browser: {browser.name}")


