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


def find_a_key(X, Y, mod):
    gcd = math.gcd(X, mod)
    res = []
    if gcd == 1:
        return [(find_opposite(X, mod) * Y) % mod]
    elif gcd > 1:
        X = X / gcd
        Y = Y / gcd
        mod = mod / gcd
        solution = (Y * find_opposite(X, mod)) % mod
        res.append(round(solution))
        for i in range(gcd-1):
            solution = round(solution + (mod % gcd))
            res.append(solution)
        return res

def find_opposite(a, in_mod):
    q_arr = []
    mod = in_mod
    remnant = mod - (a * (mod // a))

    if mod // a != mod:
        q_arr.append(mod // a)
        a, mod = remnant, a
        while remnant != 1:
            remnant = mod - (a * (mod // a))
            q_arr.append(mod // a)
            a, mod = remnant, a
        q_arr = list(map(lambda x: x * -1, q_arr))
    else:
        q_arr.append(1)
    p0 = 0
    p1 = 1
    res = 0
    for q in q_arr:
        res = (p1 * q) + p0
        p0 = p1
        p1 = res
    return res % in_mod


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
                X = a_opposite * (bigram - b) % 961
                try:
                    text += reference_bigrams[X]
                except Exception as e:
                    text += '__'
            print(text)
