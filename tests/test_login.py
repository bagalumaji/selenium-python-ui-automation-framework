import time

import pytest

from config.config_reader import ConfigReader
from conftest import setup_and_teardown
from pages.homepage import HomePage
from pages.login.login_page import LoginPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    def test_verify_login_for_invalid_credential(self):
        c1 = ConfigReader()
        home_page = HomePage()
        home_page.click_on_my_account_link()
        home_page.click_on_login()
        login_page = LoginPage()
        login_page.login_to_application(c1.user_name(), c1.password())
        time.sleep(5)

    def test_verify_login_for_valid_credential(self):
        pass
