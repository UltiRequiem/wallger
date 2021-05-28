from urllib.request import urlopen

from wmwc import helpers

URL = "https://source.unsplash.com/random/"

def set_class(options):
    """set_class.

    :param options:
    """
    url = urlopen(
        f"{URL}{options['monitor_long']}x{options['monitor_height']}"
    ).geturl()
    return helpers.generate_class(options, url, "random")


def run(options):
    """run.

    :param options:
    """
    unsplash = set_class(options)
    unsplash.download("wb")
    path = unsplash.get_path_image()
    unsplash.setup_image(path)
