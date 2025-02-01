import logging

from config.config_reader import ConfigReader
from driver.drivermanager import DriverManager
from driver.factory.driverfactory import DriverFactory
from enums.browser import Browser

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Driver:
    @staticmethod
    def init_driver(browser_name: Browser) -> None:
        """
        Initialize the WebDriver instance.
        :param browser_name: Browser enum value indicating the browser type.
        """
        try:
            if not DriverManager.get_driver():
                config = ConfigReader()
                driver = DriverFactory.get_driver(browser_name)
                driver.maximize_window()
                driver.get(config.url())
                DriverManager.set_driver(driver)
                logger.info("Driver initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize driver: {e}")

    @staticmethod
    def quit_driver() -> None:
        """
        Quit the WebDriver instance and clean up resources.
        """
        try:
            if DriverManager.get_driver():
                DriverManager.get_driver().quit()
                DriverManager.unload()
                logger.info("Driver quit successfully.")
        except Exception as e:
            logger.error(f"Failed to quit driver: {e}")


#
# class Driver:
#     @staticmethod
#     def init_driver(browser_name: Browser) -> None:
#         if not DriverManager.get_driver():
#             config = ConfigReader()
#             driver = DriverFactory.get_driver(browser_name)
#             driver.maximize_window()
#             driver.get(config.url())
#             DriverManager.set_driver(driver)
#
#     @staticmethod
#     def quit_driver() -> None:
#         if DriverManager.get_driver():
#             DriverManager.get_driver().quit()
#             DriverManager.unload()
