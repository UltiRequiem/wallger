from wmwc.functions.get_config import get_config
from wmwc.functions.dynamic_import import dynamic_import

options = {
    "monitor_long": get_config("monitor", "long"),
    "monitor_height": get_config("monitor", "height"),
    "provider": get_config("wallpaper", "provider"),
    "local": get_config("wallpaper", "local"),
    "topic": get_config("wallpaper", "topic"),
    "nfsw": get_config("wallpaper", "nfsw"),
    "save": get_config("misc", "save"),
}

provider_module = f"wmwc.providers.{options['provider']}"


if __name__ == "__main__":
    try:
        module = dynamic_import(provider_module)
        module.run(options)
    except Exception as e:
        print(f"Oops!, {e} ocurred.")
