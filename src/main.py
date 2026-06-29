from textnode import TextNode, TextType
from copy_directory import copy_directory


def main():
    text_node = TextNode(
        "Hope it works", TextType.LINK, "https://www.google.com")
    print(text_node)

    copy_directory()


main()
