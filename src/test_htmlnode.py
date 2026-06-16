import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Boot.dev",
            None,
            {
                "href": "https://www.boot.dev",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" target="_blank"',
        )

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")

    def test_values_are_set_correctly(self):
        node = HTMLNode("p", "A paragraph", [], {"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "A paragraph")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
