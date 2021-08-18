import random

import requests

from .helpers import fetch, set_image


def select_image(json: dict) -> str:
    return json["data"][random.choice(range(len(json["data"])))]["path"]


def construct_url(topic, long, height) -> str:
    return f"https://wallhaven.cc/api/v1/search?q={topic}&atleast={long}x{height}&sorting=random"


def get_image_link(json_url: str) -> str:
    return select_image(requests.get(json_url).json())


def wall_run(config) -> None:
    url = get_image_link(
        construct_url(config["topic"], config["resolution"][0], config["resolution"][1])
    )

    image_path = config["path"] + "/" + url.split("/")[len(url.split("/")) - 1]

    fetch(url, image_path)

    set_image(image_path, config["tool"])
