import json
from . import provider
import random
import os

wallhaven = provider.Provider(_,_,url,topic)

url = f"https://wallhaven.cc/api/v1/search?q="

topic="coc"

url_tag=f"{url}{topic}"

os.popen(f"curl {url_tag} --output data.json")

with open("./data.json", "r") as read_file:
    data = json.load(read_file)

len_of_data = len(data["data"])
number = random.choice(range(0,len_of_data))
print(number)
alist = data["data"]

image = alist[number]['path']

os.popen(f"curl {image} --output image.jpg")
