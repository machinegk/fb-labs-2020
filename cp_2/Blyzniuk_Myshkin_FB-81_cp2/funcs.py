from collections import Counter, OrderedDict


def encryptor(key, indexed_text, indexed_alphabet):
    text_to_return = []

    key_len = len(key)
    aplphabet_len = len(indexed_alphabet)

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for i in range(0, len(indexed_text)):
        text_to_return.append(
            key_list[val_list.index((indexed_text[i] + indexed_alphabet[key[i % key_len]]) % aplphabet_len)])

    return ''.join(text_to_return)


def conformity_index(text):
    text_length = len(text)
    grams = Counter(text)
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[0]))

    index = 0

    for element in grams:
        index += (grams[element] * (grams[element] - 1)) / (text_length * (text_length - 1))

    return index

def key_length(text):
    index = conformity_index(text)
    text_length = len(text)
    possible_key = (0.027*text_length)/((text_length-1)*index + 0.65 - 0.038*text_length)
    return possible_key