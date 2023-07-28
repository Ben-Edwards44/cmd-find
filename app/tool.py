import app.find_best as find_best
import app.settings as settings
from sys import argv


def print_info(name, desc, man):
    print(f"Command name: {name}")
    print(f"Description: {desc}")
    print(f"Enter '{man} {name}' to get more information\n")


def output_command(command_names, man_types, desc):
    print("\nBest choice:")
    print_info(command_names[-1], desc[-1], man_types[-1])

    num_others = len(command_names) - 1

    if num_others > 0:
        print("Other suggestions:")

    for i in range(num_others):
        print_info(command_names[i], desc[i], man_types[i])


def is_num(string):
    nums = "0123456789"

    for i in string:
        if i not in nums:
            return False
        
    return True


def get_args():
    useful_args = argv[1:]

    if len(useful_args) == 2:
        if is_num(useful_args[0]):
            num = int(useful_args[0])
            desc = useful_args[1]
        elif is_num(useful_args[1]):
            num = int(useful_args[1])
            desc = useful_args[0]
        else:
            raise settings.INVALID_ARGS_EXCEPTION
        
        return desc, num
    elif len(useful_args) == 1:
        num = settings.DEFAULT_SUGGESTED_NUM
        desc = useful_args[0]

        return desc, num
    else:
        raise settings.INVALID_ARGS_EXCEPTION


def main():
    cmd_desc, num = get_args()
    cmd_details = find_best.main(cmd_desc, num)

    names = [i[0] for i in cmd_details]
    man_types = [i[1]["manual type"] for i in cmd_details]
    desc = [i[1]["description"] for i in cmd_details]

    output_command(names, man_types, desc)