import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.expanduser("~/.config/wm-wallpaper-changer/config")
config.read(config_path)

monitor_long = config.get("monitor","long")
monitor_height = config.get("monitor","height")
provider = config.get("monitor","provider").lower()
