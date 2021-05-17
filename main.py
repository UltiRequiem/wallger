from wmwc.functions.get_config import get_config
from wmwc.functions.dynamic_import import dynamic_import


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

provider_module = f"wmwc.providers.{provider}"


if __name__ == "__main__":
    try:
        module = dynamic_import(provider_module)
        module.run(options)
    except Exception as e:
        print(f"Oops!, {e} ocurred")
