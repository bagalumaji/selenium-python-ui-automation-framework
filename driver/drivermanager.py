import threading


class DriverManager:
    _thread_local_driver = threading.local()

    @staticmethod
    def get_driver():
        return getattr(DriverManager._thread_local_driver, "driver", None)

    @staticmethod
    def set_driver(driver):
        DriverManager._thread_local_driver.driver = driver

    @staticmethod
    def unload():
        if hasattr(DriverManager._thread_local_driver, "driver"):
            del DriverManager._thread_local_driver.driver
