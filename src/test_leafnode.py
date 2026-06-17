import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "this should be bold")
        self.assertEqual(node.to_html(), "<b>this should be bold</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "this might be a link", {
                        "href": "https://www.spletnastran.si"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.spletnastran.si">this might be a link</a>')

    # def test_props_to_html(self):
    #     node = HTMLNode(
    #         "a",
    #         "Boot.dev",
    #         None,
    #         {
    #             "href": "https://www.boot.dev",
    #             "target": "_blank",
    #         },
    #     )
    #     self.assertEqual(
    #         node.props_to_html(),
    #         ' href="https://www.boot.dev" target="_blank"',
    #     )
    #
    # def test_props_to_html_no_props(self):
    #     node = HTMLNode("p", "Hello, world!")
    #     self.assertEqual(node.props_to_html(), "")
    #
    # def test_values_are_set_correctly(self):
    #     node = HTMLNode("p", "A paragraph", [], {"class": "text"})
    #     self.assertEqual(node.tag, "p")
    #     self.assertEqual(node.value, "A paragraph")
    #     self.assertEqual(node.children, [])
    #     self.assertEqual(node.props, {"class": "text"})
    #
    # def test_to_html_raises_not_implemented(self):
    #     node = HTMLNode("p", "Hello")
    #     with self.assertRaises(NotImplementedError):
    #         node.to_html()


if __name__ == "__main__":
    unittest.main()
