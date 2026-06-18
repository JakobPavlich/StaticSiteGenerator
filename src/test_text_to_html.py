
import unittest
from textnode import TextNode, TextType
from text_to_html import split_nodes_delimiter


class TestTextToHTML(unittest.TestCase):
    def test_lesson_example_codeblock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        comparison = [TextNode("This is text with a ", TextType.TEXT),
                      TextNode("code block", TextType.CODE),
                      TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, comparison)

    def test_italics(self):

        node = TextNode("This is text with a _italics_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        comparison = [TextNode("This is text with a ", TextType.TEXT),
                      TextNode("italics", TextType.ITALIC),
                      TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, comparison)

    def test_bold(self):

        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        comparison = [TextNode("This is text with a ", TextType.TEXT),
                      TextNode("bold", TextType.BOLD),
                      TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, comparison)

    def test_two_bold_words(self):

        node = TextNode(
            "This is text with **two** bold **words**.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        comparison = [TextNode("This is text with ", TextType.TEXT),
                      TextNode("two", TextType.BOLD),
                      TextNode(" bold ", TextType.TEXT),
                      TextNode("words", TextType.BOLD),
                      TextNode(".", TextType.TEXT)]
        self.assertEqual(new_nodes, comparison)

    def test_b_delimiter_at_end(self):
        node_b = TextNode("Bold word at **end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_b], "**", TextType.BOLD)
        comparison = [TextNode("Bold word at ", TextType.TEXT),
                      TextNode("end", TextType.BOLD)]
        self.assertEqual(new_nodes, comparison)

    def test_italics_delimiter_at_end(self):
        node_b = TextNode("Italics word at _end_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_b], "_", TextType.ITALIC)
        comparison = [TextNode("Italics word at ", TextType.TEXT),
                      TextNode("end", TextType.ITALIC)]
        self.assertEqual(new_nodes, comparison)

    def test_combination(self):
        node = TextNode(
            "Having a **bold** and an _italics_ word. And a `codeblock`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        comparison = [TextNode("Having a ", TextType.TEXT),
                      TextNode("bold", TextType.BOLD),
                      TextNode(" and an ", TextType.TEXT),
                      TextNode("italics", TextType.ITALIC),
                      TextNode(" word. And a ", TextType.TEXT),
                      TextNode("codeblock", TextType.CODE)]
        self.assertEqual(comparison, new_nodes)


if __name__ == "__main__":
    unittest.main()
