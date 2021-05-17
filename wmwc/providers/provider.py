import requests
import shutil
import os

class Provider:
    def __init__(self, monitor_long, monitor_height, topic, save, url, filename):
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.topic = topic
        self.save = save
        self.url = url
        self.filename = filename

    def download(self, mode):
        r = requests.get(self.url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(self.filename,mode) as f:
                shutil.copyfileobj(r.raw, f)

    def get_path_image(self):
            path_to_file = os.path.join(os.getcwd(), self.filename)
            return path_to_file


    def setup_image(self,file_path):
        os.system(f"feh --bg-fil {file_path}")
