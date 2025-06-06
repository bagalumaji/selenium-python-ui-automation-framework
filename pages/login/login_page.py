from selenium.webdriver.common.by import By

from config.config_reader import ConfigReader
from constants.login_page_constants import LoginPageConstants
from pageaction.pageaction import PageAction
from utils.dynamic_xpath_util import DynamicXpathUtil


class LoginPage:
    _XPATH_FOR_EMAIL_AND_PASSWORD = "//label[normalize-space()='{}']/following-sibling::input"
    _LOGIN_BUTTON = By.XPATH, "//input[@value='Login']"
    _config = ConfigReader()

    def _enter_email(self, user_name):
        email_locator = DynamicXpathUtil.create_xpath(self._XPATH_FOR_EMAIL_AND_PASSWORD,
                                                      LoginPageConstants.EMAIL_ID_ADDRESS)
        PageAction.type(email_locator, self._config.default_timeout(), user_name)

    def _enter_password(self, password):
        password_locator = DynamicXpathUtil.create_xpath(self._XPATH_FOR_EMAIL_AND_PASSWORD,
                                                         LoginPageConstants.PASSWORD_TEXT)
        PageAction.type(password_locator, self._config.default_timeout(), password)

    def _click_on_login_button(self):
        PageAction.click(self._LOGIN_BUTTON, self._config.default_timeout())

    def login_to_application(self, username: str, password: str):
        self._enter_email(username)
        self._enter_password(password)
        self._click_on_login_button()
