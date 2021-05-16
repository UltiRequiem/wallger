import unittest
from wmwc.functions import get_config

class TestValues(unittest.TestCase):

    def test_values(self):
        self.assertEqual(get_config.provider, "wallhaven" or "unsplash", "Should be one of them.")

if __name__ == '__main__':
    unittest.main()
