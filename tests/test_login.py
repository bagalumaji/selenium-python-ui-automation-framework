import time

import pytest

from config.config_reader import ConfigReader
from conftest import setup_and_teardown
from pages.homepage import HomePage
from pages.login.login_page import LoginPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    def test_verify_login_for_valid_credential(self):
        c1 = ConfigReader()
        home_page = HomePage()
        home_page.click_on_my_account_link()
        home_page.click_on_login()
        login_page = LoginPage()
        login_page.enter_email(c1.user_name())
        login_page.enter_password(c1.password())
        login_page.click_on_login_button()
        time.sleep(5)
