from textnode import TextType, TextNode


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
