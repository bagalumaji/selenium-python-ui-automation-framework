from selenium.webdriver.common.by import By

from pageaction.pageaction import PageAction


class HomePage:
    _MY_ACCOUNT = By.LINK_TEXT, "My Account"
    _LOGIN = By.LINK_TEXT, "Login"

    def click_on_my_account_link(self):
        PageAction.click(self._MY_ACCOUNT, 10)

    def click_on_login(self):
        PageAction.click(self._LOGIN, 10)
