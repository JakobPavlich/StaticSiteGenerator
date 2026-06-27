import unittest
from markdown_to_html_node import markdown_to_html_node, get_blocks, md_heading_to_htmlnode
from markdown_to_html_node import md_quote_to_htmlnode, md_ul_to_ul, md_ol_to_ol
from markdown_to_html_node import md_code_to_htmlnode, try_code
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node, TextType
from markdown_to_html_node import text_to_children


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_text_to_children_one(self):
        text = "This is a text with a **bold** word."
        children = [LeafNode(None, "This is a text with a ", None),
                    LeafNode("b", "bold", None),
                    LeafNode(None, " word.", None)]
        self.assertEqual(text_to_children(text), children)

    def test_text_to_children_two(self):
        text = "This is a text with a **bold** and an _italics_ word."
        children = [LeafNode(None, "This is a text with a ", None),
                    LeafNode("b", "bold", None),
                    LeafNode(None, " and an ", None),
                    LeafNode("i", "italics"),
                    LeafNode(None, " word.", None)]
        self.assertEqual(text_to_children(text), children)

    def test_code_1(self):
        code = """```
def is_code?(self):
    ask = 'Is this a code block and will it work?'
    return 'Who knows?'```"""
        output = """def is_code?(self):
    ask = 'Is this a code block and will it work?'
    return 'Who knows?'"""

        self.assertEqual(md_code_to_htmlnode(code), ParentNode(
            "pre", [ParentNode("code", [LeafNode(None, output)])]))

    def test_code_simpler(self):
        simple_code = """```
example```"""
        output_text = """example"""
        # output_node = text_node_to_html_node(
        #     TextNode(output_text, TextType.CODE))
        # self.assertEqual(md_code_to_htmlnode(
        #     simple_code), output_node)
        self.assertEqual(md_code_to_htmlnode(simple_code), ParentNode(
            "pre", [ParentNode("code", [LeafNode(None, output_text)])]))

    def test_code_text(self):

        simple_code = """```
small example```"""
        output_text = """
small example"""
        self.assertEqual(try_code(simple_code), output_text)

    def test_h1_to_html(self):
        md_naslov = "# Naslov"
        self.assertEqual(md_heading_to_htmlnode(md_naslov), ("h1", "Naslov"))

    def test_h2_to_html(self):
        md_naslov = "## Naslov"
        self.assertEqual(md_heading_to_htmlnode(md_naslov), ("h2", "Naslov"))

    def test_h6_to_html(self):
        md_naslov = "###### Naslov"
        self.assertEqual(md_heading_to_htmlnode(md_naslov), ("h6", "Naslov"))

    def test_not_a_markdown_heading(self):
        md_naslov = "Naslov"
        with self.assertRaises(ValueError):
            return md_heading_to_htmlnode(md_naslov)

    def test_paragraph(self):
        md_paragraph = "Hello world\nHow is it going?\nHave a nice day"
        html_paragraph = "Hello world How is it going? Have a nice day"
        self.assertEqual(md_paragraph.replace("\n", " "), html_paragraph)

    def test_quote(self):
        md_quote = """>Hopefully
> this will be
>a quote"""
        children = [LeafNode(None, "Hopefully\nthis will be\na quote")]
        self.assertEqual(md_quote_to_htmlnode(md_quote), children)

    def test_ul(self):
        md_ul = """- this
- might be
- an unordered list"""
        # html_ul = "<li>this</li><li>might be</li><li>an unordered list</li>"
        node = [ParentNode("li", [LeafNode(None, "this", None)]),
                ParentNode("li", [LeafNode(None, "might be", None)]),
                ParentNode("li", [LeafNode(None, "an unordered list", None)])
                ]
        self.assertEqual(md_ul_to_ul(md_ul), node)

    def test_ol(self):
        md_ul = """1. this
2. might be
3. an ordered list"""
        node = [ParentNode("li", [LeafNode(None, "this", None)]),
                ParentNode("li", [LeafNode(None, "might be", None)]),
                ParentNode("li", [LeafNode(None, "an ordered list", None)])
                ]
        self.assertEqual(md_ol_to_ol(md_ul), node)


class TestMarkdownToBlocks(unittest.TestCase):

    # Isti testi kot v markdown_to_blocks
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = get_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_two(self):
        md = """
# This is a heading

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- item1
- item2
"""
        blocks = get_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- item1\n- item2",
            ],
        )

    def test_markdown_to_blocks_three(self):
        md = """
# This is a heading



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- item1
- item2
"""
        blocks = get_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- item1\n- item2",
            ],
        )
