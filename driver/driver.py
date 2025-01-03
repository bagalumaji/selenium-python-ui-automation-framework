from driver.drivermanager import DriverManager
from factory.driverfactory import DriverFactory


class Driver:
    @staticmethod
    def init_driver() -> None:
        browser = "firefox"
        driver = DriverFactory.get_driver(browser)
        DriverManager.set_driver(driver)

    @staticmethod
    def quit_driver() -> None:
        DriverManager.get_driver().quit()
        DriverManager.unload()
