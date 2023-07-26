import os


JSON_FILENAME = "command_info.json"


def check_file_present():
    files = os.listdir()

    file_found = False
    for i in files:
        if i == JSON_FILENAME:
            file_found = True

    return file_found


def main():
    if not check_file_present():
        print("JSON file not found. Creating it now...")
        os.chdir(f"{os.getcwd()}/Setup")
        os.system("./setup.sh")
        os.chdir("..")