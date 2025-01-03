from driver.driver import Driver
from driver.drivermanager import DriverManager


def test_demo():
    Driver.init_driver()
    DriverManager.get_driver().get("https://www.google.com")
    print(DriverManager.get_driver().title)
    print(DriverManager.get_driver().current_url)
    Driver.quit_driver()
