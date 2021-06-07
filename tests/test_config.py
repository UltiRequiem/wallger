import unittest

from wallger import helpers

msg = "Should be one of them."
PROVIDERS = ["wallhaven", "unsplash", "local"]


options = {
    "monitor_long": helpers.get_config("monitor", "long"),
    "monitor_height": helpers.get_config("monitor", "height"),
    "provider": helpers.get_config("wallpaper", "provider"),
    "local": helpers.get_config("wallpaper", "local"),
    "topic": helpers.get_config("wallpaper", "topic"),
    "nfsw": helpers.get_config("wallpaper", "nfsw"),
    "save": helpers.get_config("misc", "save"),
}


class TestConfig(unittest.TestCase):
    def test_providers(self):
        self.assertIn(options["provider"].lower(), PROVIDERS, msg)

    def test_topic(self):
        self.assertFalse(options["topic"].isnumeric())


if __name__ == "__main__":
    unittest.main()
