import unittest
from webpage_functions import extract_title


class TestWebpageFunctions(unittest.TestCase):
    def test_extract_title(self):
        title = "# Hello"
        self.assertEqual(extract_title(title), "Hello")

    def test_extract_title_header_missing(self):
        with self.assertRaises(ValueError):
            extract_title("### Hey")
