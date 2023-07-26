import neural_network
import numpy
from json import loads


def read_file():
    with open("command_info.json", "r") as file:
        data = file.read()

    return loads(data)


def cosine_similarity(embedding1, embedding2):
    dot_p = numpy.dot(embedding1, embedding2)

    norm_a = numpy.linalg.norm(embedding1)
    norm_b = numpy.linalg.norm(embedding2)

    return dot_p / (norm_a * norm_b)


def find_semantic_similarity(desc, embedding):
    embedding2 = neural_network.encode_sentences(desc)

    return cosine_similarity(embedding, embedding2)


def progress_bar(completed, total, length):
    ratio_done = completed / total

    num_hash = int(length * ratio_done)
    num_line = length - num_hash

    bar = f"|{'#' * num_hash}{'~' * num_line}| {ratio_done * 100 :.1f}%"

    if ratio_done == 1:
        end = "\n"
    else:
        end = "\r"

    print(bar, end=end)


def main(desc):
    commands = read_file()["commands"]

    best_similarity = 0
    best_command = None

    count = 0
    total = len(commands.items())
    for k, v in commands.items():
        similarity = find_semantic_similarity(desc, v["embedding"])

        if similarity > best_similarity:
            best_similarity = similarity
            best_command = (k, commands[k])

        count += 1
        progress_bar(count, total, 50)

    return best_command