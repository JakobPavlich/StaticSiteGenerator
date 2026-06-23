from enum import Enum
import re


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    # blocks: list[str] = list(map(lambda b: b.strip(), blocks))
    # for i in range(len(blocks) - 1):
    #     if blocks[i] == "":
    #         del blocks[i]
    blocks = [block.strip() for block in blocks if block.strip() != ""]
    return blocks


class BlockType(Enum):
    P = "paragraph"
    H = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def block_to_block_type(block: str) -> BlockType:

    if re.findall(r"^#{1,6} +", block):
        return BlockType.H
    elif re.findall(r"^```\n[\s\S]*?```$", block):
        return BlockType.CODE
    elif quote_multiline(block):
        return BlockType.QUOTE
    elif ul_multiline(block):
        return BlockType.UL
    elif ol_multiline(block):
        return BlockType.OL
    else:
        return BlockType.P


def quote_multiline(block):
    found = False
    for line in block.split("\n"):
        if re.findall(r"^>.*", line):  # re.match() bi bilo bolj primerno
            found = True
        else:
            return False
    return found


def ul_multiline(block):
    found = False
    for line in block.split("\n"):
        if re.findall(r"^- .+", line):
            found = True
        else:
            return False
    return found


def ol_multiline(block):
    found = False
    block_lines = block.split("\n")
    for i in range(len(block_lines)):
        if re.findall(r"^\d+\. {1}.*", block_lines[i]) and re.findall(r"^(\d+)\. {1,}.*", block_lines[i])[0] == f"{i + 1}":
            found = True
        else:
            return False
    return found
