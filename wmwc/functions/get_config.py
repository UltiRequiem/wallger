from configparser import ConfigParser
from os.path import expanduser
import os.path
""" Get User Config """
config = ConfigParser()

config_path = expanduser("~/.configa/wm-wallpaper-changer/config")

if os.path.isfile(config_path):
    CONFIG_PATH = config.read(config_path)
else:
    # It's runing on GitHub or you didn't create `config_path` :(
    CONFIG_PATH = config.read("./doc/exampleconfig")

def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"
