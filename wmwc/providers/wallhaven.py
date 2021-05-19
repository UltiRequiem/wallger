from requests import get
from random import choice
from wmwc.functions.generate_class import generate_class

search_url = "https://wallhaven.cc/api/v1/search?q="


def get_image_link(json_url):
    json = get(json_url).json()
    return select_image(json)


def select_image(json):
    return json["data"][choice(range(0, len(json["data"])))]["path"]


def set_class(options, image_link):
    return generate_class(options, image_link, "random")


def run(options):
    image_link = get_image_link(f"{search_url}{options['topic']}")
    wallhaven = set_class(options, image_link)
    wallhaven.download("wb")
    path = wallhaven.get_path_image()
    wallhaven.setup_image(path)
