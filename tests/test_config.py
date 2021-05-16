import unittest
from wmwc.functions import get_config as config

class TestConfig(unittest.TestCase):

    def test_providers(self):
        self.assertEqual(config.provider.lower(), "wallhaven" or "unsplash", "Should be one of them.")
    
    def test_monitor_long(self):
        self.assertTrue(config.monitor_long.isnumeric())
    
    def test_monitor_height(self):
        self.assertTrue(config.monitor_height.isnumeric())


if __name__ == '__main__':
    unittest.main()
