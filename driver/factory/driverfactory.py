from selenium import webdriver

from enums.browser import Browser


class DriverFactory:
    _driver_factory = {
        Browser.CHROME: lambda: webdriver.Chrome(),
        Browser.FIREFOX: lambda: webdriver.Firefox()
    }

    @classmethod
    def get_driver(cls, browser: Browser):
        return cls._driver_factory.get(browser)()
