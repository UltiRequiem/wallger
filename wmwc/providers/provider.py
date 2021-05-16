import requests

class Provider:
    def __init__(self, monitor_long, monitor_height, topic,save):
        self.monitor_long = monitor_long
        self.monitor_height = monitor_height
        self.topic = topic
"""
    def download_image(self):
        with open("random.jpg", "wb") as file:
            response = requests.get(self.url)
            file.write(response.content)

    def download_text(self):
        with open("data.json", "wb") as file:
            response = requests.get(self.url)
            file.write(response.content)
            """
