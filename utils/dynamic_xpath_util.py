from selenium.webdriver.common.by import By


class DynamicXpathUtil:
    @staticmethod
    def create_xpath(xpath: str, text1: str) -> tuple:
        return By.XPATH, xpath.format(text=text1)
