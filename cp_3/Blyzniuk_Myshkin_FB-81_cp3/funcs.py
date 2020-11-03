import math
import re
from collections import Counter, OrderedDict


def bigram(spaceless_file):
    bigrams = re.findall(r'..?', spaceless_file)

    grams = Counter(bigrams)  # Count the frequency of each pair of letters in the text
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


def index_alphabet(alphabet):
    return {key: v for v, key in enumerate(alphabet)}


def gcd(first_number, second_number):
    coefs = []
    # print("gcd of " + str(first_number) + " and " + str(second_number), end=" is ")
    while second_number != 0:
        t = second_number
        if first_number > second_number:
            coefs.append(math.floor(first_number / second_number))
        second_number = first_number % second_number
        first_number = t
    # print(first_number)
    return first_number, coefs


def find_a_key(X, Y, mod):
    X = X % mod  # make sure no number in ouw equation
    Y = Y % mod  # is not higher then our mod

    divider, _ = gcd(X, mod)
    answers = []
    if divider == 1:
        a_opp = find_opposite(X, mod)
        print("x = " + str(a_opp) + "*" + str(Y) + "mod" + str(mod))
        x = (a_opp * Y) % mod
        answers.append(x)
    elif divider > 1:
        if (Y % divider) == 0:
            a_opp = find_opposite(math.floor(X / divider), math.floor(mod / divider))
            for answer in range(0, (divider)):
                # print("x = " + str(a_opp) + "*" + str(b/divider) + " + " + str(answer) + "*" + str(mod/divider) + " " + "mod" + str(mod))
                x = ((a_opp * math.floor(Y / divider)) + (answer * math.floor(mod / divider))) % mod
                answers.append(x)
        else:
            amount_of_answers = 0
    # print("x = " + str(answers))
    return answers


def find_opposite(a, mod):
    _, coefs = gcd(a, mod)
    # print("coefs: " + str(coefs))
    x = 1
    y = 0
    t = 0
    for index in range(0, (len(coefs) - 1)):
        t = x
        x = x * -(coefs[index]) + y
        y = t
    if x < 0:
        x = x + mod
    print("opposite is: " + str(x))
    return x


def bigram_indexer(bigrams, indexed_alphabet_dict):
    indexed_bigrams = list(map(lambda bgm: indexed_alphabet_dict[bgm[0]] * 31 + indexed_alphabet_dict[bgm[1]], bigrams))
    reference_bigrams = dict(zip(indexed_bigrams, bigrams))
    return indexed_bigrams, reference_bigrams




def param_counter(stat_frequency, enc_bigram_frequency):
    possible_keys_list = []
    for index in range(5):
        sublist = []
        a_arr = find_a_key(stat_frequency[index] - stat_frequency[index + 1],
                           enc_bigram_frequency[0] - enc_bigram_frequency[1],
                           961)
        for a in a_arr:
            b = (enc_bigram_frequency[index] - a * stat_frequency[index]) % 961
            sublist.append([a, b])
        possible_keys_list.append(sublist)
    return possible_keys_list


def decipher(keys_list, indexed_bigrams, reference_bigrams):
    for lst in keys_list:
        for sublist in lst:
            a = sublist[0]
            b = sublist[1]
            a_opposite = find_opposite(a, 961)
            text = ''
            for bigram in indexed_bigrams:
                X = a_opposite*(bigram - b) % 961
                try:
                    text += reference_bigrams[X]
                except Exception as e:
                    text += '__'
            print(text)