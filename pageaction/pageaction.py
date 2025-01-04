from wait.wait_factory import WaitFactory


class PageAction:
    @staticmethod
    def click(locator, timeout):
        WaitFactory.wait_for_element_to_be_clickable(locator, timeout).click()

    @staticmethod
    def type(locator, timeout, message):
        print("locator", locator)
        WaitFactory.wait_for_element_to_be_clickable(locator, timeout).send_keys(message)

    @staticmethod
    def is_displayed(locator, timeout):
        return WaitFactory.wait_for_element_to_be_visible(locator, timeout)
