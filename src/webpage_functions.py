import re
import os
from markdown_to_html_node import markdown_to_html_node, markdown_to_blocks
from htmlnode import HTMLNode, ParentNode, LeafNode


def extract_title(markdown: str) -> str:

    h1 = re.findall(r"^# (.+)", markdown)
    if not h1:
        raise ValueError("Heading(h1) missing")
    return h1[0].strip()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    try:
        with open(from_path) as f:
            source_md_file = f.read()
        with open(template_path) as t:
            template = t.read()

        html_node = markdown_to_html_node(source_md_file)
        html = html_node.to_html()
        title = extract_title(source_md_file)
        html_with_title = template.replace("{{ Title }}", title)
        full_html = html_with_title.replace("{{ Content }}", html)

        parent_dir = os.path.dirname(dest_path)
        os.makedirs(parent_dir, exist_ok=True)

        with open(dest_path, "w") as f:
            f.write(full_html)

        print(f'Successfully wrote to "{dest_path}"')

    except Exception as e:
        print(f"Error: {e}")
