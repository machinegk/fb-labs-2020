import math
import re
from collections import Counter, OrderedDict


def bigram(spaceless_file):
    bigrams = re.findall(r'..?', spaceless_file)

    grams = Counter(bigrams)  # Count the frequency of each pair of letters in the text
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[1], reverse=True))  # Sorts the dict
    grams_amount = len(bigrams)  # Return amount of pair of the letters

    frequency_dict = {}  # Create empty dict for letter frequency

    for element in grams:
        frequency_dict[element] = grams[element] / grams_amount  # Count frequency for each element

    entropy = 0  # Define starting value of entropy

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)  # Count entropy for each element
        entropy -= ent  # Count overall entropy

    entropy = entropy / 2

    return frequency_dict, bigrams


def russian_alphabet(exeptions):
    alp = list(map(lambda letter: ord(letter), exeptions))
    alphabet = list(map(lambda letter: chr(letter), [ind for ind in range(1072, 1104) if ind not in alp]))
    return alphabet


def indexed_alphabet(alphabet):
    return {key: v for v, key in enumerate(alphabet)}


def bigram_indexer(bigrams, indexed_alphabet):
    indexed_bigrams = list(map(lambda bgm: indexed_alphabet[bgm[0]] * 31 + indexed_alphabet[bgm[1]], bigrams))
    return indexed_bigrams
