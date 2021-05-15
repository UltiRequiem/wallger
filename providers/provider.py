import requests

class Provider():
    """
    Require:monitor long,monitor_height and url.
    """
    def __init__(self,monitor_long,monitor_height,url, topic):
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.url = url

    def download(self):
        with open("random.jpg", "wb") as file:
            response = requests.get(self.url)
            file.write(response.content)

