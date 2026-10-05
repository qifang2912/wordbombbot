from pathlib import Path


def load_words():
    file_path = Path(__file__).parent / 'words.txt'

    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    return words


def find_word(fragment, words, used_words):
    for word in words:
        if fragment in word and word not in used_words:
            used_words.add(word)
            return word

    return None