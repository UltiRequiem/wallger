from .helpers import download
from .ui import cprint
import requests
import random


def get_image_link(json_url: str) -> str:
    return select_image(requests.get(json_url).json())


def select_image(json: dict) -> str:
    return json["data"][random.choice(range(len(json["data"])))]["path"]


def wall_run(config) -> None:
    print(get_image_link(f"https://wallhaven.cc/api/v1/search?q={config['topic']}"))
    url = f"https://wallhaven.cc/api/v1/search?q={config['topic']}"
    # download(url, config["path"])

