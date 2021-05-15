import configparser
import os
import importlib

config = configparser.ConfigParser()
config_path = config.read(os.path.expanduser("~/.config/wm-wallpaper-changer/config"))

monitor_long = config.get("monitor","long")
monitor_height = config.get("monitor","height")
provider = config.get("wallpaper","provider")
provider = f"providers.{provider}"
topic = config.get("wallpaper","topic")

def dynamic_import(module):
    return importlib.import_module(module)

if __name__ == '__main__':
    try:
        module = dynamic_import(provider)
        module.main(monitor_long,monitor_height,topic)
    except: 
        print("An exception occurred")
