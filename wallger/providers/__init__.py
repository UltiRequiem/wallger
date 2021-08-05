# This file tells Python that this is a submodule

from os import getcwd, path, system
from shutil import copyfileobj

from requests import get

GSETTINGS = "gsettings set org"


class Provider:
    def __init__(
        self,
        monitor_long: int,
        monitor_height: int,
        topic: str,
        save: str,
        url: str,
        filename: str,
        system: str,
    ):
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.topic = topic
        self.save = save
        self.url = url
        self.filename = filename
        self.system = system

    def download(self, mode: str):
        r = get(self.url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(self.filename, mode) as f:
                copyfileobj(r.raw, f)

    def get_path_image(self):
        path_to_file = path.join(getcwd(), self.filename)
        return path_to_file

    def setup_image(self, path: str):
        if self.system == "wm":
            system(f"feh --bg-fil {path}")
        elif self.system == "gnome":
            system(f"{GSETTINGS}.gnome.desktop.background picture-uri 'file://{path}'")
        elif self.system == "mate":
            system(f"{GSETTINGS}.mate.background picture-filename 'file://{path}'")
        else:
            raise BaseException("That is not a valid system!")
