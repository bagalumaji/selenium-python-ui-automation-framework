import pytest

from fixtures.conftest import setup_and_teardown
from pages.homepage import HomePage


@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    def test_verify_login_for_valid_credential(self):
        home_page = HomePage()
        home_page.click_on_my_account_link()
        home_page.click_on_login()
