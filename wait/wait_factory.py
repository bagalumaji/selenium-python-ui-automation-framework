from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from driver.drivermanager import DriverManager


class WaitFactory:
    @staticmethod
    def _wait(timeout):
        return WebDriverWait(DriverManager.get_driver(), timeout)

    @staticmethod
    def wait_for_element_to_be_visible(locator, timeout):
        return WaitFactory._wait(timeout).until(ec.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_to_be_clickable(locator, timeout):
        return WaitFactory._wait(timeout).until(ec.element_to_be_clickable(locator))
