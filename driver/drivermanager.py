import threading
from selenium.webdriver.remote.webdriver import WebDriver


class DriverManager:
    _thread_local_driver = threading.local()

    @staticmethod
    def get_driver() -> WebDriver:
        return getattr(DriverManager._thread_local_driver, "driver", None)

    @staticmethod
    def set_driver(driver: WebDriver) -> None:
        DriverManager._thread_local_driver.driver = driver

    @staticmethod
    def unload() -> None:
        if hasattr(DriverManager._thread_local_driver, "driver"):
            del DriverManager._thread_local_driver.driver
