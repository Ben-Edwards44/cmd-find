import help_commands
import man_commands
from json import dumps


def build_json_file(commands):
    json_file = {"commands" : {}}

    for i in commands:
        name, desc, man_type = i

        json_file["commands"][name] = {
            "description" : desc,
            "manual type" : man_type
        }

    file_content = dumps(json_file, indent=4)

    with open("command_info.json", "w") as file:
        file.write(file_content)


def convert_command_list(names, desc, man_type):
    commands = []
    for i in range(len(names)):
        cmd = [names[i], desc[i], man_type]
        commands.append(cmd)

    return commands


def get_man_commands():
    names, desc = man_commands.main()

    return convert_command_list(names, desc, "man")


def get_help_commands():
    names, desc = help_commands.main()

    return convert_command_list(names, desc, "help")


def merge_command_list(man_commands, help_commands):
    man_names = [i[0] for i in man_commands]
    help_names = [i[0] for i in help_commands]

    commands = [i for i in man_commands]
    for i in range(len(help_names)):
        name = help_names[i]

        if name not in man_names:
            commands.append(help_commands[i])

    return commands


def main():
    man = get_man_commands()
    help = get_help_commands()

    all_commands = merge_command_list(man, help)

    build_json_file(all_commands)


if __name__ == "__main__":
    main()