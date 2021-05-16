from wmwc.functions.get_config import get_config
from wmwc.functions.generate_class import generate_class

""" Monitor Details """
monitor_long = get_config("monitor", "long")
monitor_height = get_config("monitor", "height")

""" Wallpapers Details"""
provider = get_config("wallpaper", "provider")
topic = get_config("wallpaper", "topic")
nfsw = get_config("wallpaper", "nfsw")

""" Others """
save = get_config("misc", "save")

options = {
    "monitor_long": monitor_long,
    "monitor_height": monitor_height,
    "provider": provider,
    "topic": topic,
    "nfsw": nfsw,
    "save": save,
}

if __name__ == "__main__":    
    print(generate_class(options))
