import app.neural_network as neural_network
import app.command_info as command_info
import app.settings as settings
import numpy


def cosine_similarity(embedding1, embedding2):
    dot_p = numpy.dot(embedding1, embedding2)

    norm_a = numpy.linalg.norm(embedding1)
    norm_b = numpy.linalg.norm(embedding2)

    return dot_p / (norm_a * norm_b)


def find_semantic_similarity(desc, embedding):
    embedding2 = neural_network.encode_sentences(desc)

    return cosine_similarity(embedding, embedding2)


def progress_bar(completed, total):
    ratio_done = completed / total

    num_hash = int(settings.PROG_BAR_LENGTH * ratio_done)
    num_line = settings.PROG_BAR_LENGTH - num_hash

    bar = f"Searching commands |{settings.PROG_BAR_COMPLETE * num_hash}{settings.PROG_BAR_INCOMPLETE * num_line}| {ratio_done * 100 :.1f}%"

    if ratio_done == 1:
        end = "\n"
    else:
        end = "\r"

    print(bar, end=end)


def find_most_similar(commands, desc, n):
    best = [(0, 0) for _ in range(n)]

    count = 0
    total = len(commands.items())
    for k, v in commands.items():
        similarity = find_semantic_similarity(desc, v["embedding"])

        if similarity > best[0][0]:
            best.pop(0)
            best.append((similarity, (k, commands[k])))
            best.sort()

        count += 1
        progress_bar(count, total)

    return [i[1] for i in best]


def main(desc, n):
    commands = command_info.COMMAND_INFO["commands"]

    best_commands = find_most_similar(commands, desc, n)

    return best_commands