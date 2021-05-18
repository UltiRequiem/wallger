from configparser import ConfigParser
from os.path import expanduser

""" Get User Config """
config = ConfigParser()

try:
    CONFIG_PATH = config.read(expanduser("~/.config/wm-wallpaper-changer/config"))
except IOError:
    CONFIG_PATH = config.read(expanduser("../../doc/exampleconfig"))

def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"
