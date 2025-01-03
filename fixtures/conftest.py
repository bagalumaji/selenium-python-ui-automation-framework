import pytest

from driver.driver import Driver


@pytest.fixture()
def setup_and_teardown():
    Driver.init_driver()
    yield
    Driver.quit_driver()
