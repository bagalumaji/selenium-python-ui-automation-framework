import logging

from selenium import webdriver

from enums.browser import Browser

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverFactory:
    """
    Factory class to create WebDriver instances based on the browser type.
    """
    _driver_factory = {
        Browser.CHROME: lambda: webdriver.Chrome(),
        Browser.FIREFOX: lambda: webdriver.Firefox()
    }

    @classmethod
    def get_driver(cls, browser: Browser):
        """
        Retrieve a WebDriver instance for the specified browser.
        :param browser: Browser enum value indicating the browser type.
        :return: WebDriver instance.
        """
        try:
            driver = cls._driver_factory.get(browser)()
            logger.info(f"{browser.name} driver created successfully.")
            return driver
        except TypeError:
            logger.error(f"No driver found for browser: {browser.name}")
            raise ValueError(f"No driver found for browser: {browser.name}")


# class DriverFactory:
#     _driver_factory = {
#         Browser.CHROME: lambda: webdriver.Chrome(),
#         Browser.FIREFOX: lambda: webdriver.Firefox()
#     }
#
#     @classmethod
#     def get_driver(cls, browser: Browser):
#         return cls._driver_factory.get(browser)()
