from selenium.webdriver.common.by import By


class DynamicXpathUtil:
    @staticmethod
    def create_xpath(xpath: str, *args) -> tuple:
        return By.XPATH, xpath.format(*args)
