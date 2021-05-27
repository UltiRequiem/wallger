from configparser import ConfigParser
from importlib import import_module
from os.path import dirname, expanduser, isfile

from wmwc.providers.provider import Provider

def generate_class(options, url, filename):
    return Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"],
        url,
        filename,
    )

def dynamic_import(module):
    try:
        return import_module(module)
    except ImportError as error:
        print(f"Oops {error} ocurred.")


config = ConfigParser()

config_path = expanduser("~/.config/wm-wallpaper-changer/config")

if isfile(config_path):
    CONFIG_PATH = config.read(config_path)
else:
    CONFIG_PATH = config.read(f"{dirname(__file__)}/../../doc/if_no_config")


def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"



