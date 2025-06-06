import threading

import threading
from selenium.webdriver.remote.webdriver import WebDriver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DriverManager:
    _thread_local_driver = threading.local()

    @classmethod
    def get_driver(cls) -> WebDriver:
        return getattr(cls._thread_local_driver, "driver", None)

    @classmethod
    def set_driver(cls, driver: WebDriver) -> None:
        cls._thread_local_driver.driver = driver
        logger.info("Driver set for the current thread.")

    @classmethod
    def unload(cls) -> None:
        if hasattr(cls._thread_local_driver, "driver"):
            del cls._thread_local_driver.driver
            logger.info("Driver unloaded for the current thread.")

