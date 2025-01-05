import configparser

from constants.framework_constants import FrameworkConstants


class ConfigReader:
    _instance = None
    _config = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigReader, cls).__new__(cls, *args, **kwargs)
            cls._config = configparser.RawConfigParser()
            cls._config.read(FrameworkConstants.FRAMEWORK_CONFIG_FILE_NAME)
        return cls._instance

    def url(self) -> str:
        return self._config.get("basic_info", "url")

    def user_name(self) -> str:
        return self._config.get("basic_info", "username")

    def password(self) -> str:
        return self._config.get("basic_info", "password")

    def browser(self):
        return self._config.get("basic_info", "browser")
