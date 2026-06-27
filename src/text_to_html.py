from textnode import TextType, TextNode
from extractor_img_a import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        array_after_split = old_node.text.split(delimiter)
        if len(array_after_split) % 2 == 0:
            raise ValueError(
                "Invalid Markdown syntax. No closing delimiter found")
        # if old_node.text[0] == delimiter:
        #     even_type = text_type
        #     odd_type = TextType.TEXT
        # else:
        #     even_type = TextType.TEXT
        #     odd_type = text_type
        temp_nodes = []
        for i in range(len(array_after_split)):
            if array_after_split[i] == "":
                continue
            if i % 2 == 0:
                # if array_after_split[i] != "":
                temp_nodes.append(
                    TextNode(array_after_split[i], TextType.TEXT))
            else:
                # if array_after_split[i] != "":
                temp_nodes.append(
                    TextNode(array_after_split[i], text_type))
        new_nodes.extend(temp_nodes)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images: list[tuple] = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        temp_nodes = []
        text = old_node.text
        for image_alt, image_link in images:
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError(
                    "invalid markdown syntax, image section not closed")
            if sections[0] != "":
                temp_nodes.append(TextNode(sections[0], TextType.TEXT))
                temp_nodes.append(
                    TextNode(image_alt, TextType.IMAGE, image_link))
            else:
                temp_nodes.append(
                    TextNode(image_alt, TextType.IMAGE, image_link))
            text = sections[1]
        if text != "":
            temp_nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(temp_nodes)

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links: list[tuple] = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.extend([old_node])
            continue
        temp_nodes = []
        text = old_node.text
        for link_text, link_url in links:
            sections = text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError(
                    "invalid markdown syntax, link section not closed.")
            if sections[0] != "":
                temp_nodes.append(TextNode(sections[0], TextType.TEXT))
                temp_nodes.append(
                    TextNode(link_text, TextType.LINK, link_url))
            else:
                temp_nodes.append(
                    TextNode(link_text, TextType.LINK, link_url))
            text = sections[1]

        if text != "":
            temp_nodes.append(TextNode(text, TextType.TEXT))
        new_nodes.extend(temp_nodes)

    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)
    textnodes: list[TextNode] = split_nodes_delimiter(
        [text_node], "`", TextType.CODE)
    textnodes = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "_", TextType.ITALIC)
    textnodes = split_nodes_link(textnodes)
    textnodes = split_nodes_image(textnodes)
    return textnodes
