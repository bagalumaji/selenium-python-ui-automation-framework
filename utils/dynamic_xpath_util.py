from selenium.webdriver.common.by import By


def create_xpath(xpath, text) -> By:
    return By.XPATH(xpath.format(text))


create_xpath("//label[normalize-space()='text']/following-sibling::input", )
