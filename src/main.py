# from textnode import TextNode, TextType
from copy_directory import copy_directory
import os
import shutil
from webpage_functions import generate_page


def main():

    destination_path = os.path.abspath("public")
    source_path = os.path.abspath("static")
    print("---copy_directory.py:")
    public_path = os.path.abspath("public")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    copy_directory(source_path, destination_path)
    generate_page("content/index.md", "template.html", "public/index.html")


main()
