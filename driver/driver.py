from selenium import webdriver

from driver.drivermanager import DriverManager


class Driver:
    @staticmethod
    def init_driver() -> None:
        driver = webdriver.Chrome()
        driver.maximize_window()
        DriverManager.set_driver(driver)

    @staticmethod
    def quit_driver() -> None:
        DriverManager.get_driver().quit()
        DriverManager.unload()
