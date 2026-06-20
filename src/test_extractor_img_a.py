import unittest
from extractor_img_a import extract_markdown_images, extract_markdown_links


class TestExtractor(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_two_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another image](https://www.another-image.com)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", "https://www.another-image.com")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_two_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and [another link](https://www.another-image.com)"
        )
        self.assertListEqual(
            [("link", "https://i.imgur.com/zjjcJKZ.png"), ("another link", "https://www.another-image.com")], matches)

    def test_extract_markdown_link_and_image(self):
        text = "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an ![image](https://www.another-image.com)"
        matches = extract_markdown_links(text)
        matches.extend(extract_markdown_images(text))
        self.assertListEqual(
            [("link", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://www.another-image.com")], matches)

    def test_no_image(self):
        text = "This is a text with no image."
        matches = extract_markdown_images(text)
        self.assertEqual([], matches)

    def test_no_images_nor_links(self):
        text = "This is a text with no image."
        matches = extract_markdown_images(text)
        matches.extend(extract_markdown_links(text))
        self.assertEqual([], matches)


if __name__ == "__main__":
    unittest.main()
