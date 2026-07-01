from markdown_to_blocks import markdown_to_blocks
from markdown_to_blocks import block_to_block_type, BlockType
from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
import re
from text_to_html import text_to_textnodes


def markdown_to_html_node(markdown):
    children = []
    blocks = get_blocks(markdown)
    for block in blocks:
        children.append(block_to_html_node(block))

    parent = ParentNode("div", children)
    return parent


def get_blocks(markdown):
    return markdown_to_blocks(markdown)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.P:
        paragraph = block.replace("\n", " ")
        return ParentNode("p", text_to_children(paragraph))
    elif block_type == BlockType.H:
        tag, text = md_heading_to_htmlnode(block)
        return ParentNode(tag, text_to_children(text))
    elif block_type == BlockType.QUOTE:
        children = md_quote_to_htmlnode(block)
        return ParentNode("blockquote", children)
    elif block_type == BlockType.UL:
        children = md_ul_to_ul(block)
        return ParentNode("ul", children)
    elif block_type == BlockType.OL:
        children = md_ol_to_ol(block)
        return ParentNode("ol", children)
    # še za CODE, potem pa verjetno text_to_childre.
    elif block_type == BlockType.CODE:
        return md_code_to_htmlnode(block)
    # še <pre> -- mislim, da zdaj dela.


def text_to_children(text):
    html_nodes: list[HTMLNode] = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def try_code(markdown):
    match = re.findall(r"^```(\n[\s\S]*?)```$", markdown)
    text = match[0]
    return text


def md_code_to_htmlnode(markdown):

    match = re.findall(r"^```\n([\s\S]*?)```$", markdown)
    text = match[0]
    # text_node = TextNode(text, TextType.TEXT)
    return ParentNode("pre", [LeafNode("code", text)])
    # mogoče bodo še problemi tu - prej je bilo
    # ParentNode("code", text_node_to_html_node(text_node))


def md_ol_to_ol(markdown):
    md_ol = markdown.split("\n")
    li_items_list = []
    for item_text in md_ol:
        item = re.findall(r"\d+\. (.*)", item_text)
        # list_items_string += f"<li>{item[0]}</li>"
        li = ParentNode("li", text_to_children(item[0]))
        li_items_list.append(li)
    return li_items_list


def md_ul_to_ul(markdown):
    md_ul = markdown.split("\n")
    li_items_list = []
    for item_text in md_ul:
        # list_items_string += f"<li>{item_text[2:]}</li>"
        li = ParentNode("li", text_to_children(item_text[2:]))
        li_items_list.append(li)
    return li_items_list


def md_heading_to_htmlnode(md_heading):
    # for i in range(1, 7):
    #     if re.match(fr"^#{{{i}}} +", md_heading):
    #         text = md_heading[(i+1):]
    #         tag = f"h{i}"

    level = 0
    for char in md_heading:
        if char == "#":
            level += 1
        else:
            break
    text = md_heading[level:].strip()
    tag = f"h{level}"
    if level == 0:
        raise ValueError("Not a valid markdown heading.")
    return tag, text
    # return HTMLNode(f"h{i}", text, text_to_children(md_heading))


def md_quote_to_htmlnode(quote):

    lines = quote.split("\n")
    plain_quote = []
    for line in lines:
        if line[0:2] == "> ":
            plain_quote.append(line[2:])
        else:
            plain_quote.append(line[1:])
    plain_quote = "\n".join(plain_quote)

    return text_to_children(plain_quote)
