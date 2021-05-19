from configparser import ConfigParser
from os.path import expanduser, isfile,dirname

this_file_path = dirname(__file__)

config = ConfigParser()

config_path = expanduser("~/.config/wm-wallpaper-changer/config")

if isfile(config_path):
    CONFIG_PATH = config.read(config_path)
else:
    CONFIG_PATH = config.read(f"{this_file_path}/../../doc/if_no_config")

def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"
