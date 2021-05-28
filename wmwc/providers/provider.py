from os import getcwd, path, system
from shutil import copyfileobj

from requests import get


class Provider:
    def __init__(self, monitor_long, monitor_height, topic, save, url, filename,system):
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.topic = topic
        self.save = save
        self.url = url
        self.filename = filename
        self.system =  system

    def download(self, mode):
        r = get(self.url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(self.filename, mode) as f:
                copyfileobj(r.raw, f)

    def get_path_image(self):
        path_to_file = path.join(getcwd(), self.filename)
        return path_to_file

    def setup_image(self, file_path):
        match self.system:
            case "wm":
                system(f"feh --bg-fil {file_path}")
            case "gnome":
                system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{file_path}'")
            case "mate":
                system(f"gsettings set org.mate.background picture-filename 'file://{file_path}'")
