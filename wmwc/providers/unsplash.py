from wmwc.functions.generate_class import generate_class
from urllib.request import urlopen
import os

def set_class(options):
    url = urlopen(
        f"https://source.unsplash.com/random/{options['monitor_long']}x{options['monitor_height']}"
    ).geturl()
    global filename
    filename = "random"
#    filename = url.split("/")[-1]
    unsplash = generate_class(options, url, filename)
    return unsplash

def run(options):
    unsplash = set_class(options)
    unsplash.download("wb")
    path = unsplash.get_path_image()
    unsplash.setup_image(path)