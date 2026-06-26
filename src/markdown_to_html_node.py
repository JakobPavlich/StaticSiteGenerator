from markdown_to_blocks import markdown_to_blocks
from markdown_to_blocks import block_to_block_type, BlockType
from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import HTMLNode
import re


def markdown_to_html_node(markdown):
    blocks = get_blocks(markdown)
    for block in blocks:
        block_to_html_node(block)


def get_blocks(markdown):
    return markdown_to_blocks(markdown)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.P:
        block.replace("\n", " ")
        return HTMLNode("p", block, text_to_children(block))
    elif block_type == BlockType.H:
        tag, text = md_heading_to_htmlnode(block)
        return HTMLNode(tag, text, text_to_children(block))
    elif block_type == BlockType.QUOTE:
        text = md_quote_to_htmlnode(block)
        return HTMLNode("blockquote", text, text_to_children(block))
    elif block_type == BlockType.UL:
        text = md_ul_to_ul(block)
        return HTMLNode("ul", text, text_to_children(block))
    elif block_type == BlockType.OL:
        text = md_ol_to_ol(block)
        return HTMLNode("ol", text, text_to_children(block))
    # še za CODE, potem pa verjetno text_to_childre.
    elif block_type == BlockType.CODE:
        return md_code_to_htmlnode(block)
    # še <pre>


def try_code(markdown):
    match = re.findall(r"^```(\n[\s\S]*?)```$", markdown)
    text = match[0]
    return text


def md_code_to_htmlnode(markdown):

    match = re.findall(r"^```(\n[\s\S]*?)```$", markdown)
    text = match[0]
    text_node = TextNode(text, TextType.CODE)
    return text_node_to_html_node(text_node)
    # še <pre>


def md_ol_to_ol(markdown):
    md_ol = markdown.split("\n")
    list_items_string = ""
    for item_text in md_ol:
        item = re.findall(r"\d+\. (.*)", item_text)
        list_items_string += f"<li>{item[0]}</li>"
    return list_items_string


def md_ul_to_ul(markdown):
    md_ul = markdown.split("\n")
    list_items_string = ""
    for item_text in md_ul:
        list_items_string += f"<li>{item_text[2:]}</li>"
    return list_items_string


def md_heading_to_htmlnode(md_heading):
    html_heading = ""
    for i in range(1, 7):
        if re.match(fr"^#{{{i}}} +", md_heading):
            text = md_heading[(i+1):]
            html_heading = f"<h{i}>{text}</h{i}>"
            tag = f"h{i}"
    if not html_heading:
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

    return plain_quote


def text_to_children(text):
    pass
