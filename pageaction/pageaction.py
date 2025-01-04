from wait.wait_factory import WaitFactory


class PageAction:
    @staticmethod
    def click(locator, timeout):
        WaitFactory.wait_for_element_to_be_clickable(locator, timeout).click()

    @staticmethod
    def type():
        pass

    @staticmethod
    def is_displayed():
        pass
