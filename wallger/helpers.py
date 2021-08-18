"""
Helper functions
"""
import json
import os
import shutil
import sys

import requests

from .constants import CONFIG_PATH
from .ui import cprint, error_print, magenta, yellow


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


def set_image(path, tool) -> None:
    if tool == "feh":
        os.system(f"feh --bg-fill {path}")
    elif tool == "gnome":
        os.system(
            f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}'"
        )
    elif tool == "mate":
        os.system("gsettings set org.mate.background picture-filename 'file://{path}'")
    elif tool == "kde":
        cprint("KDE is not supported yet! But it will be soon :)")
    else:
        error_print(f"{tool} is Unknown tool!")


def fetch(url, path):
    data = requests.get(url, stream=True)
    data.raw.decode_content = True
    with open(path, "wb") as file:
        shutil.copyfileobj(data.raw, file)


def select_provider(config) -> None:
    cprint(f"Your Wallpaper Provider is {config['provider'].capitalize()}!")
    cprint(f"The topic is {config['topic'].capitalize()}!", yellow)

    if config["provider"] == "wallhaven":
        from .wallhaven import wall_run

        wall_run(config)

    cprint("Done!", magenta)
