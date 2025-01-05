import os


class FrameworkConstants:
    _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    _USER_DIR = os.path.abspath(os.path.join(_SCRIPT_DIR, os.pardir))
    FRAMEWORK_CONFIG_FILE_NAME = _USER_DIR + "/resources/config/framework_config.ini"
