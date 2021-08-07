from json import load
from importlib import import_module
from os.path import expanduser

from .providers import Provider


from .constants import CONFIG_PATH, ERROR_MESSAGE


def get_config_file() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return load(config)
    except FileNotFoundError:
        print(ERROR_MESSAGE)
        raise BaseException("Config file not found!")


def generate_class(options: dict, url: str, filename: str) -> Provider:
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
    elif provider == "unsplash":
        from wallger.providers.unsplash import run

        run(options)
    elif provider == "local":
        from wallger.providers.local import run

        run(options)
    else:
        print(ERROR_MESSAGE)
        raise BaseException(
            "You have put a wrong provider in your configuration, or maybe its just misspelled."
        )
