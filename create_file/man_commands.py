from os import popen
from string import ascii_lowercase


def get_command_list():
    commands = get_raw_commands()

    cmd_names = []
    cmd_desc = []

    for i in commands:
        sep = i.split(" - ")
        name = sep[0]
        desc = " - ".join(sep[1:])

        stripped_name = add_until_space(name)

        page = int(name[len(stripped_name) + 2])

        if page == 1:
            desc = strip_desc(desc.lower())
            
            cmd_names.append(stripped_name)
            cmd_desc.append(desc)

    return cmd_names, cmd_desc


def get_raw_commands():
    commands = popen("man -k .")
    commands = commands.read()
    
    return commands.split("\n")[:-1]


def add_until_space(string):
    result = ""

    for i in string:
        if i == " ":
            break
        else:
            result += i

    return result


def strip_desc(desc):
    new_desc = ""

    for i in desc:
        if i in ascii_lowercase or i == " ":
            new_desc += i

    return new_desc


def main():
    names, desc = get_command_list()

    return names, desc