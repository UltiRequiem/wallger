from wmwc.functions.generate_class import generate_class
import os
import random

def set_class(options):
    global filename
    url = options["local"]
    filename = random.choice(os.popen(f"ls {url}").read().split())
    return generate_class(options, url, filename)


def run(options):
    local = set_class(options)
    path = f"{local.url}/{local.filename}"
    local.setup_image(path)
