import time

import pytest

from fixtures.conftest import setup_and_teardown
from pages.homepage import HomePage
from pages.login.login_page import LoginPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    def test_verify_login_for_valid_credential(self):
        home_page = HomePage()
        home_page.click_on_my_account_link()
        home_page.click_on_login()
        login_page = LoginPage()
        login_page.enter_email("demo@gmail.com")
        login_page.enter_password("test@123")
        login_page.click_on_login_button()
        time.sleep(5)
