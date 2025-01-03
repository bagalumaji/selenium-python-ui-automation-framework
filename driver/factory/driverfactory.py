from selenium import webdriver


class DriverFactory:
    _driver_factory = {
        "chrome": lambda: webdriver.Chrome(),
        "firefox": lambda: webdriver.Firefox()
    }

    @staticmethod
    def get_driver(browser):
        return DriverFactory._driver_factory.get(browser)()
