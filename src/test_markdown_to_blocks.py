import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
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
        blocks = markdown_to_blocks(md)
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
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- item1\n- item2",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        heading = "## This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.H)

    def test_code_block(self):
        code = """```
this could be a code block
```"""
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote(self):
        quote = ">This should be a quote"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_multiline_quote(self):
        quote = """>hopefully
> this
> works
> but maybe not"""
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_ul(self):
        ul_block = """- maybe
- a list
- or maybe
- not"""
        self.assertEqual(block_to_block_type(ul_block), BlockType.UL)

    def test_ul_line_without_dash(self):
        ul_block = """- maybe
- a list
or maybe
- not"""
        self.assertNotEqual(block_to_block_type(ul_block), BlockType.UL)

    def test_ol(self):
        ol_block = """1. first item
2. second one
3. and a third"""
        self.assertEqual(block_to_block_type(ol_block), BlockType.OL)

    def test_ol_numbering(self):
        ol_block = """1. first item
3. second one
2. and a third"""
        self.assertNotEqual(block_to_block_type(ol_block), BlockType.OL)

    def test_ol_missing_space(self):
        ol_block = """1. first item
2. second one
3.and a third"""
        self.assertNotEqual(block_to_block_type(ol_block), BlockType.OL)

    def test_p(self):
        paragraph = """Just nothing really special
        a normal paragraph
        with some **boldness**"""
        self.assertEqual(block_to_block_type(paragraph), BlockType.P)
# Boots

    def test_heading_no_space(self):
        block = "##not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.P)

    def test_heading_too_many_hashes(self):
        block = "####### not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.P)

    def test_multiline_quote_with_invalid_line(self):
        block = """>valid
not valid
>valid again"""
        self.assertEqual(block_to_block_type(block), BlockType.P)

    def test_ordered_list_must_start_at_one(self):
        block = """2. second
3. third"""
        self.assertEqual(block_to_block_type(block), BlockType.P)

    def test_unordered_list_missing_space(self):
        block = """- valid
-invalid"""
        self.assertEqual(block_to_block_type(block), BlockType.P)


if __name__ == "__main__":
    unittest.main()
