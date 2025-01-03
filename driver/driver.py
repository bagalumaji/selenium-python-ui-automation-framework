from driver.drivermanager import DriverManager
from driver.factory import DriverFactory


class Driver:
    @staticmethod
    def init_driver() -> None:
        browser = "firefox"
        driver = DriverFactory.get_driver(browser)
        driver.maximize_window()
        driver.get("https://tutorialsninja.com/demo/index.php")
        DriverManager.set_driver(driver)

    @staticmethod
    def quit_driver() -> None:
        DriverManager.get_driver().quit()
        DriverManager.unload()
