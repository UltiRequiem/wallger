from os import popen
from random import choice

from wmwc import helpers


def set_class(options:object) -> object:
    """set_class.

    :param options:
    """
    url = options["local"]
    filename = choice(popen(f"ls {url}").read().split())
    return helpers.generate_class(options, url, filename)


def run(options:object):
    """run.

    :param options:
    """
    local = set_class(options)
    path = f"{local.url}/{local.filename}"
    local.setup_image(path)
