from driver.drivermanager import DriverManager


class PageAction:
    @staticmethod
    def click(locator):
        DriverManager.get_driver().find_element(*locator).click()

    @staticmethod
    def type():
        pass

    @staticmethod
    def is_displayed():
        pass
