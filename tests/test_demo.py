import pytest

from driver.drivermanager import DriverManager
from fixtures.conftest import setup_and_teardown
@pytest.mark.usefixtures('setup_and_teardown')
class TestDemo:

    def test_demo(self):
        DriverManager.get_driver().get("https://www.google.com")
        print(DriverManager.get_driver().title)
        print(DriverManager.get_driver().current_url)
