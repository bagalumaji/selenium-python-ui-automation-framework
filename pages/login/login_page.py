from selenium.webdriver.common.by import By

from constants.login_page_constants import LoginPageConstants
from pageaction.pageaction import PageAction
from utils.dynamic_xpath_util import DynamicXpathUtil


class LoginPage:
    _XPATH_FOR_EMAIL_AND_PASSWORD = "//label[normalize-space()='{}']/following-sibling::input"
    _LOGIN_BUTTON = By.XPATH, "//input[@value='Login']"

    def enter_email(self, user_name):
        email_locator = DynamicXpathUtil.create_xpath(self._XPATH_FOR_EMAIL_AND_PASSWORD,
                                                      LoginPageConstants.EMAIL_ID_ADDRESS)
        print(email_locator)
        PageAction.type(email_locator, 10, user_name)

    def enter_password(self, password):
        password_locator = DynamicXpathUtil.create_xpath(self._XPATH_FOR_EMAIL_AND_PASSWORD,
                                                         LoginPageConstants.PASSWORD_TEXT)
        PageAction.type(password_locator, 10, password)

    def click_on_login_button(self):
        PageAction.click(self._LOGIN_BUTTON, 10)
