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

    def get_url(self) -> str:
        return self._config.get("basic_info", "url")

    def get_user_name(self) -> str:
        return self._config.get("basic_info", "username")

    def get_password(self) -> str:
        return self._config.get("basic_info", "password")

    def get_browser(self):
        return self._config.get("basic_info", "browser")
