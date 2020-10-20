from collections import Counter, OrderedDict
import wordninja
import re, math


def stuff_counter(counted, amount):
    frequency_dict = {}  # Create empty dict for letter frequency

    for element in counted:
        frequency_dict[element] = counted[element] / amount  # Count frequency for each element

    return frequency_dict  # Return value of entropy and frequency dictionary


def entropy_counter(counted):
    grams = Counter(counted)  # Count the frequency of each pair of letters in the text
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[1], reverse=True))  # Sorts the dict
    grams_amount = len(counted)  # Return amount of pair of the letters

    frequency_dict = stuff_counter(grams, grams_amount)
    return frequency_dict


def encryptor(key, indexed_text, indexed_alphabet):
    text_to_return = []

    key_len = len(key)
    alphabet_len = len(indexed_alphabet)

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for i in range(0, len(indexed_text)):
        text_to_return.append(
            key_list[val_list.index((indexed_text[i] + indexed_alphabet[key[i % key_len]]) % alphabet_len)])

    return ''.join(text_to_return)


def decryptor(key, indexed_text, indexed_alphabet):
    deciphered_text = []

    key_len = len(key)
    alphabet_len = len(indexed_alphabet)

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for i in range(0, len(indexed_text)):
        deciphered_text.append(
            key_list[val_list.index((indexed_text[i] - indexed_alphabet[key[i % key_len]]) % alphabet_len)])
    return ''.join(deciphered_text)


def partial_caesar_decryptor(text, reference_dict, key_len):
    key_stat = [] # List of most frequent letters of each position of the key
    possible_key = ''
    alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
    indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for element in range(0, key_len):
        letter_list = text[element::key_len]
        txt = "".join(map(str, letter_list))
        stat = entropy_counter(txt)
        key_stat.append(max(stat, key=stat.get))

    indexed_key_stat = list(map(lambda i: indexed_alphabet[i], key_stat))
    for shift in reference_dict.keys():
        possible_key = ''
        for index in indexed_key_stat:
            possible_index = (index - indexed_alphabet[shift]) % 32
            possible_key += key_list[val_list.index(possible_index)]
        print(wordninja.split(possible_key))



def conformity_index(text):
    text_length = len(text)
    grams = Counter(text)
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[0]))

    index = 0

    for element in grams:
        index += (grams[element] * (grams[element] - 1)) / (text_length * (text_length - 1))

    return index


def key_length(text):
    index_dict = {}
    for chunk in range(2, 31):
        index = 0
        for element in range(0, chunk):
            letter_list = text[element::chunk]
            txt = "".join(map(str, letter_list))
            index += conformity_index(txt)
        index_dict[chunk] = index / chunk
    return index_dict
