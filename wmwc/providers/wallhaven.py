from json import load
from random import choice
from subprocess import DEVNULL, STDOUT, check_call
from wmwc.functions.generate_class import generate_class

search_url = "https://wallhaven.cc/api/v1/search?q="


def get_image_link(json_url):
    json = get_json(json_url)
    return select_image(json)


def get_json(txt_url):
    check_call(['curl',f'{txt_url}','--output','data.json'], stdout=DEVNULL, stderr=STDOUT)
    with open("./data.json", "r") as read_file:
        data = load(read_file)
    return data


def select_image(json):
    number = choice(range(0, len(json["data"])))
    image_link = json["data"][number]["path"]
    return image_link

def set_class(options,image_link):
    return generate_class(options,image_link,"random")

def run(options):
    image_link = get_image_link(f"{search_url}{options['topic']}")
    wallhaven = set_class(options,image_link)
    wallhaven.download("wb")
    path = wallhaven.get_path_image()
    wallhaven.setup_image(path)
