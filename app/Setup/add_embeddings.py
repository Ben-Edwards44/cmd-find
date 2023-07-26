import embed_commands
from json import loads, dumps


def read_file():
    with open("command_info.json", "r") as file:
        data = file.read()

    return loads(data)


def write_file(dict):
    content = dumps(dict, indent=4)

    with open("command_info.json", "w") as file:
        file.write(content)


def embed_desc(command_info):
    desc = [command_info["commands"][i]["description"] for i in command_info["commands"].keys()]

    return embed_commands.embed_sentences(desc)


def add_to_dict(embeddings, dict):
    for i, x in enumerate(dict["commands"].keys()):
        embedding = embeddings[i]
        dict["commands"][x]["embedding"] = embedding

    return dict


def main():
    dict = read_file()
    embeddings = embed_desc(dict)
    final_dict = add_to_dict(embeddings, dict)

    write_file(final_dict)


if __name__ == "__main__":
    main()