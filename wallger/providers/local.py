from os import popen
from random import choice

from wallger import helpers


def set_class(options: dict):
    """set_class.

    :param options:
    :type options: dict
    """
    url = options["local"]
    filename = choice(popen(f"ls {url}").read().split())
    return helpers.generate_class(options, url, filename)


def run(options: dict):
    """run.

    :param options:
    :type options: dict
    """
    local = set_class(options)
    path = f"{local.url}/{local.filename}"
    local.setup_image(path)
