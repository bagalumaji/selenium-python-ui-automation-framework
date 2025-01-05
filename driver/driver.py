from config.config_reader import ConfigReader
from driver.drivermanager import DriverManager
from driver.factory.driverfactory import DriverFactory
from enums.browser import Browser


class Driver:
    @staticmethod
    def init_driver(browser_name:Browser) -> None:
        config = ConfigReader()
        driver = DriverFactory.get_driver(browser_name)
        driver.maximize_window()
        driver.get(config.url())
        DriverManager.set_driver(driver)

    @staticmethod
    def quit_driver() -> None:
        DriverManager.get_driver().quit()
        DriverManager.unload()
