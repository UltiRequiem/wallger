import requests
import shutil


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
