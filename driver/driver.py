from config.config_reader import ConfigReader
from driver.drivermanager import DriverManager
from driver.factory.driverfactory import DriverFactory


class Driver:
    @staticmethod
    def init_driver() -> None:
        config_reader = ConfigReader()
        driver = DriverFactory.get_driver(config_reader.get_browser())
        driver.maximize_window()
        driver.get(config_reader.get_url())
        DriverManager.set_driver(driver)

    @staticmethod
    def quit_driver() -> None:
        DriverManager.get_driver().quit()
        DriverManager.unload()
