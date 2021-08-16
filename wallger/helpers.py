"""
Helper functions
"""
import json
import sys

from .constants import CONFIG_PATH
from .ui import error_print


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return json.load(config)
    except json.decoder.JSONDecodeError:
        error_print(" Your configuration is invalid!")
        sys.exit(0)
    except FileNotFoundError:
        error_print("Config file not found!")
        sys.exit(0)
