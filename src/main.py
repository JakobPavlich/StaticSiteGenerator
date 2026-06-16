from textnode import TextNode, TextType


def main():
    text_node = TextNode(
        "Hope it works", TextType.LINK, "https://www.google.com")
    print(text_node)


main()
