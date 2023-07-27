import app.change_dir as change_dir
import os


JSON_FILENAME = "command_info.json"


def check_file_present():
    change_dir.change_to_app()

    files = os.listdir()

    file_found = False
    for i in files:
        if i == JSON_FILENAME:
            file_found = True

    return file_found


def run_setup():
    change_dir.change_to_setup()
    os.system("./setup.sh")


def main():
    if not check_file_present():
        print("JSON file not found. Creating it now...")
        run_setup()