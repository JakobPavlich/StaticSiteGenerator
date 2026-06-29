import os
import shutil


def copy_directory():
    cwd = os.getcwd()
    static_path = os.path.abspath("static")
    public_path = os.path.abspath("public")

    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

    static_dir = os.listdir(static_path)
    for item in static_dir:
        item_path = os.path.normpath(os.path.join(cwd, f"static/{item}"))
        if os.path.isfile(item_path):
            print(f"{item} is a file")
        else:
            print(f"{item} is a directory")
