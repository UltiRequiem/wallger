"""
Helper functions
"""
import json
import os
import shutil
import requests
import sys

from .constants import CONFIG_PATH
from .ui import error_print, cprint, magenta


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return json.load(config)
    except json.decoder.JSONDecodeError:
        error_print("Your configuration is invalid!")
        sys.exit(0)
    except FileNotFoundError:
        error_print("Config file not found!")
        sys.exit(0)


def set_image(path) -> None:
    os.system(f"feh --bg-fill {path}")


def download(url, path):
    r = requests.get(url, stream=True)
    r.raw.decode_content = True
    with open(path, "wb") as file:
        shutil.copyfileobj(r.raw, file)


def select_provider(config) -> None:
    cprint(f"Your Wallpaper Provider is {config['provider'].capitalize()}!")

    if config["provider"] == "wallhaven":
        from .wallhaven import wall_run

        wall_run(config)

    cprint("Done!", magenta)
