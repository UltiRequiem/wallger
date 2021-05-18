from configparser import ConfigParser
from os.path import expanduser, isfile

""" Get User Config """
config = ConfigParser()

config_path = expanduser("~/.config/wm-wallpaper-changer/config")

if isfile(config_path):
    CONFIG_PATH = config.read(config_path)
else:
    # It's runing on GitHub or you didn't create `config_path` :(
    CONFIG_PATH = config.read("./doc/if_no_config")

def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"
