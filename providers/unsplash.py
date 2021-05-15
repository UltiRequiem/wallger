from . import provider
import os

url = "https://source.unsplash.com/random/"

def main(monitor_long,monitor_height):
    unsplash = provider.Provider(monitor_long,monitor_height,url, "ignore")
    unsplash.download()

    name_of_file = "random.jpg"
    path_to_file = os.path.join(os.getcwd(), name_of_file)
    os.system(f"feh --bg-fill {path_to_file}")
