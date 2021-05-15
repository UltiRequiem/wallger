import json
import random
import os

url = "https://wallhaven.cc/api/v1/search?q="

def main(unused_one, unused_two,topic):
    data_url = f"{url}{topic}"
    os.popen(f"curl {data_url} --output data.json")
    with open("./data.json", "r") as read_file:
        data = json.load(read_file)
    number = random.choice(range(0, len(data["data"])))
    alist = data["data"]
    image = alist[number]['path']
    name_of_file = "image.jpg"
    os.popen(f"curl {image} --output {name_of_file}")

    path_to_file = os.path.join(os.getcwd(), name_of_file)
    os.system(f"feh --bg-fill {path_to_file}")
