def russian_alphabet():

    #alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
    alphabet = list(map(lambda letter: chr(letter), [ind for ind in range(1072, 1104) if ind not in [1073]]))
    return alphabet
from collections import Counter, OrderedDict
import math, re


def bigram(spaceless_file):
    letter_pairs = re.findall(r'..?', spaceless_file)

    grams = Counter(letter_pairs)  # Count the frequency of each pair of letters in the text
    grams = OrderedDict(sorted(grams.items(), key=lambda t: t[0]))  # Sorts the dict
    grams_amount = len(letter_pairs)  # Return amount of pair of the letters

    frequency_dict = {}  # Create empty dict for letter frequency

    for element in grams:
        frequency_dict[element] = grams[element] / grams_amount  # Count frequency for each element

    entropy = 0  # Define starting value of entropy

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)  # Count entropy for each element
        entropy -= ent  # Count overall entropy

    entropy = entropy / 2

    return frequency_dict

def russian_alphabet(exeptions):
    alphabet = list(map(lambda letter: chr(letter), [ind for ind in range(1072, 1104) if ind not in [ord(exeptions)]]))
    return alphabet
