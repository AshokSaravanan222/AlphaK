import unittest
import entry_methods


class TestEntry(unittest.TestCase):
    def test_click(self):
        self.assertEqual(entry_methods.click())


if __name__ == "__main__":
    unittest.main()
