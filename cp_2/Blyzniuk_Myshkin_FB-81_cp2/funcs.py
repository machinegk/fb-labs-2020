from collections import Counter, OrderedDict
import re


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
        if text_length != 1:
            index += (grams[element] * (grams[element] - 1)) / (text_length * (text_length - 1))

    return index

def key_length(text):
    index_dict = {}
    for chunk in range(2, 30):
        index = 0
        start = 0
        for element in range(1, chunk+1):
            letter_list = text[start::element]
            txt = "".join(map(str,letter_list))
            index += conformity_index(txt)
            start += 1
        index_dict[chunk] = index / chunk
    return index_dict
#
# def key_length(text):
#     key_length_dict = {}
#     text_length = len(text)
#     for chunk in range(2, 30):
#         text_splited = re.findall('.{1,' + str(round(text_length/chunk)) + '}', text)
#         index = 0
#         for q in text_splited:
#             index += conformity_index(q)
#         key_length_dict[chunk] = index / len(text_splited)
#
#     return key_length_dict
