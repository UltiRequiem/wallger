from configparser import ConfigParser
from importlib import import_module
from os.path import expanduser

from wmwc.providers.provider import Provider

config = ConfigParser()

config_path = expanduser("~/.config/wm-wallpaper-changer/config")
config.read(config_path)



def get_config(secction, option):
    try:
        return config.get(secction, option)
    except:
        return "none"


def generate_class(options, url, filename):
    return Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"],
        url,
        filename,
    )


def dynamic_import(module):
    try:
        return import_module(module)
    except ImportError as error:
        print(f"Oops {error} ocurred.")



def set_image(options):
    provider = options["provider"]
    match provider:
        case "wallhaven":
            from wmwc.providers.wallhaven import run
            run(options)
        case "unsplash":
            from wmwc.providers.unsplash import run
            run(options)
        case "local":
            from wmwc.providers.local import run
            run(options)
