import configparser
from os import path

""" Get User Config """
config = configparser.ConfigParser()
CONFIG_PATH = config.read(path.expanduser("~/.config/wm-wallpaper-changer/config"))


def get_config(secction, option):
    return config.get(secction, option)
