import os
import shutil


def copy_directory(relative_path: str = None):
    # cwd = os.getcwd()
    public_path = os.path.abspath("public")
    if relative_path:
        source_path = os.path.abspath("static" + relative_path)
        destination_path = os.path.abspath("public" + relative_path)
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
    else:
        relative_path = ""
        destination_path = os.path.abspath("public")
        source_path = os.path.abspath("static")
        if os.path.exists(public_path):
            shutil.rmtree(public_path)
        os.mkdir(public_path)

    static_dir = os.listdir(source_path)
    for item in static_dir:
        item_path = os.path.normpath(os.path.join(source_path, item))
        if os.path.isfile(item_path):
            print(f"-Trying to copy {item}")
            shutil.copy(item_path, destination_path)
        else:
            dir = item
            relative_path += f"/{dir}"
            copy_directory(relative_path)
