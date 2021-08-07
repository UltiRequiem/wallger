from urllib.request import urlopen

from .. import helpers

URL = "https://source.unsplash.com/random/"


def set_class(options: dict):
    url = urlopen(
        f"{URL}{options['monitor']['long']}x{options['monitor']['height']}"
    ).geturl()
    return helpers.generate_class(options, url, "random")


def run(options: dict) -> None:
    unsplash = set_class(options)
    unsplash.download("wb")
    unsplash.setup_image(unsplash.get_path_image())
