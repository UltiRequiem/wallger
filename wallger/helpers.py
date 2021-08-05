import json
from importlib import import_module
from os.path import expanduser
from wallger.providers import Provider


def get_config_file() -> dict:
    try:
        with open(expanduser("~/.config/wallger/config.json"), "r") as config:
            return json.load(config)
    except FileNotFoundError:
        print("No config.")


def generate_class(options: dict, url: str, filename: str):
    return Provider(
        options["monitor"]["long"],
        options["monitor"]["height"],
        options["wallpaper"]["topic"],
        options["save"],
        url,
        filename,
        options["system"],
    )


def dynamic_import(module: str):
    try:
        return import_module(module)
    except ImportError as error:
        print(f"Oops {error} ocurred.")


def set_image(options: dict):
    provider = options["wallpaper"]["provider"]
    if provider == "wallhaven":
        from wallger.providers.wallhaven import run

        run(options)
    if provider == "unsplash":
        from wallger.providers.unsplash import run

        run(options)
    if provider == "local":
        from wallger.providers.local import run

        run(options)
