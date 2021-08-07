from random import choice

from requests import get

from .. import helpers

SEARCH_URL = "https://wallhaven.cc/api/v1/search?q="


def get_image_link(json_url: str) -> str:
    return select_image(get(json_url).json())


def select_image(json: dict) -> str:
    return json["data"][choice(range(len(json["data"])))]["path"]


def set_class(options: dict, image_link: str):
    return helpers.generate_class(options, image_link, "random")


def run(opt: dict):
    custom_link = f"{SEARCH_URL}{opt['wallpaper']['topic']}&atleast={opt['monitor']['long']}x{opt['monitor']['height']}&sorting=random"
    wallhaven = set_class(opt, get_image_link(custom_link))
    wallhaven.download("wb")
    wallhaven.setup_image(wallhaven.get_path_image())
