from os import popen
from random import choice

from .. import helpers


def set_class(options: dict):
    url = options["wallpaper"]["local"]
    filename = choice(popen(f"ls {url}").read().split())
    return helpers.generate_class(options, url, filename)


def run(options: dict) -> None:
    local = set_class(options)
    local.setup_image(f"{local.url}/{local.filename}")
