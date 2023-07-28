from os import popen
from string import ascii_lowercase


INVALID_COMMANDS = ("job_spec", "((", "", ">")


def get_command_list():
    data = popen("./help.sh 1").read()[393:]
    lines = data.split("\n")

    inx = find_col_index(lines[0])

    col1 = [i[1:inx] for i in lines]
    col2 = [i[inx:] for i in lines]

    commands = []
    for i, x in zip(col1, col2):
        i = i.split(" ")
        x = x.split(" ")

        commands.append(i[0])
        commands.append(x[0])

    commands = [i for i in commands if i not in INVALID_COMMANDS]

    return commands


def find_col_index(line):
    spaces_run = 0

    for i, x in enumerate(line):
        if x == " ":
            spaces_run += 1
        elif spaces_run > 10:
            return i
        else:
            spaces_run = 0

    raise Exception("Column index not found")


def get_short_desc(command):
    script_call = f"./help.sh 2 {command}"
    result = popen(script_call).read()
    result = result.split(" - ")

    desc = ""
    for i in result[1]:
        char = i.lower()

        if char in ascii_lowercase or char == " ":
            desc += char

    return desc


def main():
    names = get_command_list()
    desc = [get_short_desc(i) for i in names]

    return names, desc