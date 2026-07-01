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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    try:
        content_dir = os.listdir(dir_path_content)
        for item in content_dir:
            item_path = os.path.normpath(os.path.join(dir_path_content, item))
            if os.path.isfile(item_path) and item[-3:] == ".md":
                with open(item_path) as md_item:
                    md_file = md_item.read()
                with open(template_path) as t:
                    template = t.read()
                html_node = markdown_to_html_node(md_file)
                html_content = html_node.to_html()
                title = extract_title(md_file)
                html_with_title = template.replace("{{ Title }}", title)
                full_html = html_with_title.replace(
                    "{{ Content }}", html_content)

                dest_html_file_path = os.path.normpath(
                    os.path.join(dest_dir_path, (item[:-3] + ".html")))
                parent_dir = os.path.dirname(dest_html_file_path)
                os.makedirs(parent_dir, exist_ok=True)
                with open(dest_html_file_path, "w") as f:
                    f.write(full_html)

                print(f'Successfully wrote to "{dest_html_file_path}"')
            elif os.path.isfile(item_path) and item[-3:] != ".md":
                continue
            else:
                new_dest_dir_path = os.path.normpath(
                    os.path.join(dest_dir_path, item))
                generate_pages_recursive(
                    item_path, template_path, new_dest_dir_path)

    except Exception as e:
        print(f"Error: {e}")
