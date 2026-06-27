import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_code(self):
        code_text = """
def is_code?(self):
ask = 'Is this a code block and will it work?'
return 'Who knows?'"""
        node = LeafNode("code", code_text)
        html = """<code>
def is_code?(self):
ask = 'Is this a code block and will it work?'
return 'Who knows?'</code>"""
        self.assertEqual(node.to_html(), html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        first_child = LeafNode("b", "The firstborn child")
        second_child = LeafNode(None, " and the second one")
        third_child = LeafNode("i", " and another.")
        parent_node = ParentNode(
            "div", [first_child, second_child, third_child])

        self.assertEqual(parent_node.to_html(),
                         "<div><b>The firstborn child</b> and the second one<i> and another.</i></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
