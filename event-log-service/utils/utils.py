import re
from pathlib import Path
import os

def get_project_root() -> Path:
    return Path(os.getcwd())

def get_logging_config():
    # Get the absolute path of the logger.ini file in the config directory
    config_file_path = os.path.join(get_project_root(), "logger.ini")
    return config_file_path