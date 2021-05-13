import configparser
import os
import importlib

config = configparser.ConfigParser()

config_path = config.read(os.path.expanduser("~/.config/wm-wallpaper-changer/config"))

monitor_long = config.get("monitor","long")
monitor_height = config.get("monitor","height")
provider = config.get("monitor","provider")

def dynamic_import(module):
    return importlib.import_module(module)

if __name__ == '__main__':
    try:
        provider = f"providers.{provider}"
        module = dynamic_import(provider)
        module.main(monitor_long,monitor_height)
    except: 
        print("An exception occurred")
