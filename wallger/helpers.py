import json
from importlib import import_module
from os.path import expanduser

from wallger.providers.provider import Provider


def get_config_file():
    """get_config_file."""
    try:
        with open(expanduser("~/.config/wallger/config.json"), "r") as json_data:
            return json.load(json_data)
    except FileNotFoundError:
        print("No config.")


def get_config(secction: str, option: str):
    """get_config.

    :param secction:
    :type secction: str
    :param option:
    :type option: dict
    """
    json_data = get_config_file()
    try:
        return json_data[secction][option]
    except:
        return "none"


def generate_class(options: dict, url: str, filename: str):
    """generate_class.

    :param options:
    :type options: dict
    :param url:
    :type url: str
    :param filename:
    :type filename: str
    """
    return Provider(
        options["monitor_long"],
        options["monitor_height"],
        options["topic"],
        options["save"],
        url,
        filename,
        options["system"],
    )


def dynamic_import(module: str):
    """dynamic_import.

    :param module:
    :type module: str
    """
    try:
        return import_module(module)
    except ImportError as error:
        print(f"Oops {error} ocurred.")


def set_image(options: dict):
    """set_image.

    :param options:
    :type options: dict
    """
    provider = options["provider"]
    if provider == "wallhaven":
        from wallger.providers.wallhaven import run

        run(options)
    if provider == "unsplash":
        from wallger.providers.unsplash import run

        run(options)
    if provider == "local":
        from wallger.providers.local import run

        run(options)
