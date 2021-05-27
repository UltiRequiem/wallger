from os import popen
from random import choice

from wmwc import helpers


def set_class(options):
    url = options["local"]
    filename = choice(popen(f"ls {url}").read().split())
    return helpers.generate_class(options, url, filename)


def run(options):
    local = set_class(options)
    path = f"{local.url}/{local.filename}"
    local.setup_image(path)
