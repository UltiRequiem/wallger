import importlib
import json
import sys

from .constants import CONFIG_PATH, ERROR_MESSAGE


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return json.load(config)
    except FileNotFoundError as error:
        print("Config file not found!")
        sys.exit(0)
