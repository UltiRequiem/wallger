import configparser
from os.path import expanduser

""" Get User Config """
config = configparser.ConfigParser()
CONFIG_PATH = config.read(expanduser("~/.config/wm-wallpaper-changer/config"))


def get_config(secction, option):
    return config.get(secction, option)