from pageaction.pageaction import PageAction


class LoginPage:
    _XPATH_FOR_EMAIL_AND_PASSWORD = "//label[normalize-space()='text']/following-sibling::input"
    def enter_email(self):
        email_locator = DXU
        PageAction.type()