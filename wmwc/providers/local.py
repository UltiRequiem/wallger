from wmwc.functions.generate_class import generate_class
from os import popen
from random import choice

def set_class(options):
    global filename
    url = options["local"]
    filename = choice(popen(f"ls {url}").read().split())
    print(filename)
    return generate_class(options, url, filename)


def run(options):
    local = set_class(options)
    path = f"{local.url}/{local.filename}"
    local.setup_image(path)
