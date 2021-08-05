""" 
Providers module

Includes the stuff for Wallhaven, Unsplash and Local Files.
"""


class Provider:
    def __init__(
        self,
        mon_long: int = 1600,
        mon_height: int = 900,
        topic: str = "Anime",
        save: bool = True,
        url: str = "https://wallhaven.cc/api/v1/search?q=",
        tool: str = "feh",
    ):
        self.mon_long = mon_long
        self.mon_height = mon_height
        self.topic = topic
        self.save = save
        self.url = url
        self.tool = tool
