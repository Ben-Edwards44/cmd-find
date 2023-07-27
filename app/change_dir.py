from sys import argv
import os


def get_main():
    dir = argv[0]
    path = os.path.abspath(dir)
    script_dir = os.path.dirname(path)

    return script_dir


def change_to_main():
    dir = get_main()

    os.chdir(dir)


def change_to_app():
    dir_main = get_main()
    dir_app = f"{dir_main}/app"

    os.chdir(dir_app)


def change_to_setup():
    dir_main = get_main()
    dir_setup = f"{dir_main}/app/Setup"

    os.chdir(dir_setup)