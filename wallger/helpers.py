import json
import sys

from .constants import CONFIG_PATH
from .ui import cprint


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return json.load(config)
    except json.decoder.JSONDecodeError:
        cprint(" Your configuration is invalid!")
        sys.exit(0)
    except FileNotFoundError:
        cprint("Config file not found!")
        sys.exit(0)
    except:
        sys.exit(0)
