import configparser
import os

config = configparser.ConfigParser()

config_path = config.read(os.path.expanduser("~/.config/wm-wallpaper-changer/config"))

monitor_long = config.get("monitor","long")
monitor_height = config.get("monitor","height")
provider = config.get("monitor","provider")

if __name__ == "__main__":
    try:
        from providers.unsplash import main
        main(monitor_long,monitor_height)
    except:
         print("An exception occurred")
