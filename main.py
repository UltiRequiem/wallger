"""Import common functions"""
from wmwc import helpers

options = {
    "monitor_long": helpers.get_config("monitor", "long"),
    "monitor_height": helpers.get_config("monitor", "height"),
    "provider": helpers.get_config("wallpaper", "provider"),
    "local": helpers.get_config("wallpaper", "local"),
    "topic": helpers.get_config("wallpaper", "topic"),
    "nfsw": helpers.get_config("wallpaper", "nfsw"),
    "save": helpers.get_config("misc", "save"),
    "system":helpers.get_config("misc","system")
}

if __name__ == "__main__":
    try:
        helpers.set_image(options)
    except Exception as exception:
        print(f"Oops!, {exception} ocurred.")
