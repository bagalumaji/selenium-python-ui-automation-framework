from selenium import webdriver

from enums.browser import Browser


class DriverFactory:
    _driver_factory = {
        Browser.CHROME: lambda: webdriver.Chrome(),
        Browser.FIREFOX: lambda: webdriver.Firefox()
    }

    @staticmethod
    def get_driver(browser:Browser):
        return DriverFactory._driver_factory.get(browser)()
