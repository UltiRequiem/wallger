from json import load

from .constants import CONFIG_PATH, ERROR_MESSAGE


def get_config() -> dict:
    try:
        with open(CONFIG_PATH) as config:
            return load(config)
    except FileNotFoundError:
        print(ERROR_MESSAGE)
        raise BaseException("Config file not found!")


### TODO: Better way to Import needed
# IDEAS:
# print(__import__("wallger").core.constants.CONFIG_PATH)
# __import__("wallger").providers.wallhaven.run()
# __import__(PROVIDER, globals(), locals(), [], 0).run()
# Or use `match` when Python3.10 is more popular


def run() -> None:
    """
    The program entry point.
    """
    CONFIG = get_config()
    PROVIDER = CONFIG["wallpaper"]["provider"]

    if PROVIDER == "wallhaven":
        from ..providers import wallhaven as provider

        provider.run(CONFIG)
    elif PROVIDER == "unsplash":
        from ..providers import unsplash as provider

        provider.run(CONFIG)
    elif PROVIDER == "local":
        from ..providers import local as provider

        provider.run(CONFIG)
    else:
        print(ERROR_MESSAGE)
        raise BaseException(
            "You have put a wrong provider in your configuration, or maybe its just misspelled."
        )
