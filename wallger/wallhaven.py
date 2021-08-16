from .helpers import download, set_image

import requests
import random


def select_image(json: dict) -> str:
    return json["data"][random.choice(range(len(json["data"])))]["path"]


def get_image_link(json_url: str) -> str:
    return select_image(requests.get(json_url).json())


def wall_run(config) -> None:
    url = get_image_link(
        f"https://wallhaven.cc/api/v1/search?q={config['topic']}&atleast={config['resolution'][0]}x{config['resolution'][1]}&sorting=random"
    )

    image_path = config["path"] + "/" + url.split("/")[len(url.split("/")) - 1]

    download(url, image_path)

    set_image(image_path)
