from random import choice

from requests import get

from wallger import helpers

SEARCH_URL = "https://wallhaven.cc/api/v1/search?q="


def get_image_link(json_url: str):
    """get_image_link.

    :param json_url:
    :type json_url: str
    """
    json = get(json_url).json()
    return select_image(json)


def select_image(json):
    """select_image.

    :param json:
    """
    return json["data"][choice(range(0, len(json["data"])))]["path"]


def set_class(options: dict, image_link: str):
    """set_class.

    :param options:
    :type options: dict
    :param image_link:
    :type image_link: str
    """
    return helpers.generate_class(options, image_link, "random")


def run(options: dict):
    """run.

    :param options:
    :type options: dict
    """
    custom_link = f"{SEARCH_URL}{options['topic']}&atleast={options['monitor_long']}x{options['monitor_height']}&sorting=random"
    image_link = get_image_link(custom_link)
    wallhaven = set_class(options, image_link)
    wallhaven.download("wb")
    wallhaven.setup_image(wallhaven.get_path_image())
