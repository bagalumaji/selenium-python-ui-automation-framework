from selenium import webdriver


class DriverFactory:
    _driver_factory = {
        "chrome": webdriver.Chrome(),
        "firefox": webdriver.Firefox()
    }

    @staticmethod
    def get_driver(browser):
        return DriverFactory._driver_factory.get(browser)
