from urllib.request import urlopen

from wallger import helpers

URL = "https://source.unsplash.com/random/"


def set_class(options: dict):
    """set_class.

    :param options:
    :type options: dict
    """
    url = urlopen(
        f"{URL}{options['monitor']['long']}x{options['monitor']['height']}"
    ).geturl()
    return helpers.generate_class(options, url, "random")


def run(options: dict):
    """run.

    :param options:
    :type options: dict
    """
    unsplash = set_class(options)
    unsplash.download("wb")
    path = unsplash.get_path_image()
    unsplash.setup_image(path)
