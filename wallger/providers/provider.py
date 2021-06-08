from os import getcwd, path, system
from shutil import copyfileobj

from requests import get

GSETTINGS = "gsettings set org"


class Provider:
    """Provider."""

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
        """__init__.

        :param monitor_long:
        :type monitor_long: int
        :param monitor_height:
        :type monitor_height: int
        :param topic:
        :type topic: str
        :param save:
        :type save: str
        :param url:
        :type url: str
        :param filename:
        :type filename: str
        :param system:
        :type system: str
        """
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.topic = topic
        self.save = save
        self.url = url
        self.filename = filename
        self.system = system

    def download(self, mode: str):
        """download.

        :param mode:
        :type mode: str
        """
        r = get(self.url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(self.filename, mode) as f:
                copyfileobj(r.raw, f)

    def get_path_image(self):
        """get_path_image."""
        path_to_file = path.join(getcwd(), self.filename)
        return path_to_file

    def setup_image(self, path: str):
        """setup_image.

        :param file_path:
        :type file_path: str
        """
        if self.system == "wm":
            system(f"feh --bg-fil {path}")
        elif self.system == "gnome":
            system(f"{GSETTINGS}.gnome.desktop.background picture-uri 'file://{path}'")
        elif self.system == "mate":
            system(f"{GSETTINGS}.mate.background picture-filename 'file://{path}'")
        else:
            print("That is not a valid system!")
