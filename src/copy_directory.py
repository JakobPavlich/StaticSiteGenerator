import os


def copy_directory():
    cwd = os.getcwd()
    print(cwd)
    if os.path.exists(os.path.abspath("static")):
        print("folder 'static' exists")

    if os.path.exists(os.path.abspath("public")):
        print("folder 'public' exists")
