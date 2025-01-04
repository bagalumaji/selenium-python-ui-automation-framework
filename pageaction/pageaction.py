from appium.webdriver import WebElement

from wait.wait_factory import WaitFactory


class PageAction:
    @staticmethod
    def click(locator: tuple or WebElement, timeout: int):
        WaitFactory.wait_for_element_to_be_clickable(locator, timeout).click()

    @staticmethod
    def type(locator: tuple or WebElement, timeout: int, message: str):
        print("locator", locator)
        WaitFactory.wait_for_element_to_be_clickable(locator, timeout).send_keys(message)

    @staticmethod
    def is_displayed(locator: tuple or WebElement, timeout: int):
        return WaitFactory.wait_for_element_to_be_visible(locator, timeout)
