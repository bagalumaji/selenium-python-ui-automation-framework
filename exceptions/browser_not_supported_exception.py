class BrowserNotSupportedException(Exception):
    def __init__(self, message):
        super().__init__(f"'{message}' is not a valid Browser")
