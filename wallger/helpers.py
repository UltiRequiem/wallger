"""
Helper functions
"""

import json
import os
import shutil
import sys

import requests
from colores import MAGENTA, RED, YELLOW, colorized_print

from .constants import CONFIG_PATH


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH, encoding="UTF-8") as config:
            return json.load(config)
    except json.decoder.JSONDecodeError:
        colorized_print("Your configuration is invalid!", RED)
        sys.exit(0)
    except FileNotFoundError:
        colorized_print("Config file not found!", RED)
        sys.exit(0)


def set_image(path, tool) -> None:
    tool = tool.lower()

    if tool == "feh":
        os.system(f"feh --bg-fill {path}")
    elif tool == "gnome":
        os.system(
            f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}'"
        )
    elif tool == "mate":
        os.system("gsettings set org.mate.background picture-filename 'file://{path}'")
    elif tool == "kde":
        colorized_print("KDE is not supported yet! But it will be soon :)")
    else:
        colorized_print(f"{tool} is Unknown tool!", RED)


def fetch(url, path):
    data = requests.get(url, stream=True, timeout=30)
    data.raw.decode_content = True

    with open(path, "wb") as file:
        shutil.copyfileobj(data.raw, file)


def select_provider(config) -> None:
    colorized_print(f"Your Wallpaper Provider is {config['provider'].capitalize()}!")
    colorized_print(f"The topic is {config['topic'].capitalize()}!", YELLOW)

    provider = config["provider"].lower()

    if provider == "wallhaven":
        from .wallhaven import wall_run

        wall_run(config)

    colorized_print("Done!", MAGENTA)
