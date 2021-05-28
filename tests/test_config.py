import unittest

from wmwc import helpers

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

  #  def test_monitor_long(self):
   #     self.assertTrue(options["monitor_long"].isnumeric())

#    def test_monitor_height(self):
 #       self.assertTrue(options["monitor_height"].isnumeric())

    def test_topic(self):
        self.assertFalse(options["topic"].isnumeric())

 #   def test_purity(self):
  #      self.assertIn(options["nfsw"].lower(), ["true", "false"], msg)


if __name__ == "__main__":
    unittest.main()
