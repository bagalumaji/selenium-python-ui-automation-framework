from selenium.webdriver.common.by import By

from driver.drivermanager import DriverManager


class HomePage:
    _MY_ACCOUNT = By.LINK_TEXT, "My Account"

    def click_on_my_account_link(self):
        DriverManager.get_driver().find_element(*self._MY_ACCOUNT).click()
