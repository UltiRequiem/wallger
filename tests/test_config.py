import unittest
import sys, os, inspect
# TODO: This is working but I don't like it
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import main

msg = "Should be one of them."
PROVIDERS = ["wallhaven", "unsplash", "local"]


class TestConfig(unittest.TestCase):
    def test_providers(self):
        self.assertIn(main.provider.lower(), PROVIDERS, msg)

    def test_monitor_long(self):
        self.assertTrue(main.monitor_long.isnumeric())

    def test_monitor_height(self):
        self.assertTrue(main.monitor_height.isnumeric())

    def test_topic(self):
        self.assertFalse(main.topic.isnumeric())

    def test_purity(self):
        self.assertIn(main.nfsw.lower(), ["true", "false"], msg)


if __name__ == "__main__":
    unittest.main()
