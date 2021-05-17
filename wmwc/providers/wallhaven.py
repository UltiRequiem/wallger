from wmwc.functions.generate_class import generate_class
from urllib.request import urlopen

url = "https://wallhaven.cc/api/v1/search?q="
#json_url = f"{url}{topic}"

def get_image(something):
    # bedtime 
    pass

def set_class(options):
    url = f"url{options['topic']}"
    wallhaven = generate_class(options, url,"random")
    return wallhaven


def run(options):
    wallhaven = set_class(options)


# TODO FINISH THIS

"""
import json
import random
import os
from . import provider

def main(unused_one, unused_two,topic):
    data_url = f"{url}{topic}"
    
    wallhaven = provider.Provider(unused_one,unused_two,url, "ignore")
    os.popen(f"curl {data_url} --output data.json")
    with open("./data.json", "r") as read_file:
        data = json.load(read_file)
    number = random.choice(range(0, len(data["data"])))
    alist = data["data"]
    image = alist[number]['path']
    name_of_file = "image.jpg"
    os.popen(f"curl {image} --output {name_of_file}")
    path_to_file = os.path.join(os.getcwd(), name_of_file) # This gives full path: /home/username/etc
    os.system(f"feh --bg-fill {path_to_file}")
    """
