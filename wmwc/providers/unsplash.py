from wmwc.functions.generate_class import generate_class
from urllib.request import urlopen

url = urlopen("https://source.unsplash.com/random").geturl()
filename = url.split("/")[-1]

def run(options):
    unsplash = generate_class(options, url, filename)
    unsplash.download("wb")
