import find_best
from sys import argv


def output_command(command_name, man_type, desc):
    print(f"Command name: {command_name}")
    print(f"Description: {desc}")
    print(f"Use '{man_type} {command_name}' to get more information")


def get_args():
    useful_args = argv[1:]

    if len(useful_args) == 1:
        return useful_args[0]
    else:
        raise Exception("Invalid arguments")


def main():
    print("Searching commands...")

    cmd_desc = get_args()
    cmd_name, cmd_details = find_best.main(cmd_desc)

    output_command(cmd_name, cmd_details["manual type"], cmd_details["description"])