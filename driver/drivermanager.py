import threading

from selenium.webdriver.remote.webdriver import WebDriver


class DriverManager:
    _thread_local_driver = threading.local()

    @classmethod
    def get_driver(cls) -> WebDriver:
        return getattr(cls._thread_local_driver, "driver", None)

    @classmethod
    def set_driver(cls, driver: WebDriver) -> None:
        cls._thread_local_driver.driver = driver

    @classmethod
    def unload(cls) -> None:
        if hasattr(cls._thread_local_driver, "driver"):
            del cls._thread_local_driver.driver
