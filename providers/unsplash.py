import requests
import os

def main(monitor_long,monitor_height):
    url = f"https://source.unsplash.com/random/{monitor_long}x{monitor_height}"
    
    with open("random.jpg", "wb") as file:
        response = requests.get(url)
        file.write(response.content)

    name_of_file = "random.jpg"
    path_to_file = os.path.join(os.getcwd(), name_of_file)
    os.system(f"feh --bg-fill {path_to_file}")
