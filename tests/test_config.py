import unittest
from wmwc.functions import get_config as config

msg = "Should be one of them."
PROVIDERS = ["wallhaven", "unsplash"]


class TestConfig(unittest.TestCase):
    def test_providers(self):
        self.assertIn(config.provider.lower(), PROVIDERS, msg)

    def test_monitor_long(self):
        self.assertTrue(config.monitor_long.isnumeric())

    def test_monitor_height(self):
        self.assertTrue(config.monitor_height.isnumeric())

    def test_topic(self):
        self.assertFalse(config.topic.isnumeric())

    def test_purity(self):
        self.assertIn(config.nfsw.lower(), ["true", "false"], msg)


if __name__ == "__main__":
    unittest.main()
