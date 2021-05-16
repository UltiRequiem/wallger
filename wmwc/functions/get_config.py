import configparser
from os import path

""" Get User Config """
config = configparser.ConfigParser()
config_path = config.read(path.expanduser("~/.config/wm-wallpaper-changer/config"))

""" Monitor Details """
monitor_long = config.get("monitor","long")
monitor_height = config.get("monitor","height")

""" Wallpapers Details"""
provider = config.get("wallpaper","provider")
topic = config.get("wallpaper","topic")
nfsw = config.get("wallpaper","nfsw")

""" Others """
save = config.get("misc","save")
