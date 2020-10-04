from collections import Counter
import re, math


def extra_remover(file):
    space_file = file.read().lower()
    space_file = re.sub(r'[^А-Яа-я ]', '', space_file)
    spaceless_file = re.sub(r'\W', '', space_file)
    return space_file, spaceless_file





def onegram(space_file):
    s_letters_amount = len(space_file)
    s_counted_letters = Counter(space_file)

    entropy, frequency_dict = stuff_counter(s_counted_letters, s_letters_amount)

    print("Entropy = " + str(entropy))
    print("R = " + str(1 - ((entropy) / math.log(32, 2))))

    ent = frequency_dict[' '] * math.log(frequency_dict[' '], 2)

    entropy += ent
    del frequency_dict[' ']
    print("Entropy = " + str(entropy))
    print("R = " + str(1 - ((entropy) / math.log(32, 2))))


def bigram(space_file, spaceless_file):
    s_letter_pairs = list(map(''.join, zip(space_file, space_file[1:])))

    s_bigrams = Counter(s_letter_pairs)
    s_bigrams_amount = len(s_letter_pairs)

    entropy, frequency_dict = stuff_counter(s_bigrams, s_bigrams_amount)
    entropy = entropy / 2
    print("Entropy = " + str(entropy))
    print("R = " + str(1 - ((entropy) / math.log(32, 2))))

    letter_pairs = list(map(''.join, zip(spaceless_file, spaceless_file[1:])))
    bigrams = Counter(letter_pairs)
    bigrams_amount = len(letter_pairs)

    entropy, frequency_dict = stuff_counter(bigrams, bigrams_amount)
    entropy = entropy / 2
    print("Entropy = " + str(entropy))
    print("R = " + str(1 - ((entropy) / math.log(32, 2))))

def stuff_counter(counted, amount):
    frequency_dict = {}

    for element in counted:
        frequency_dict[element] = counted[element] / amount
        print("Frequency of " + element + ' = ' + str(frequency_dict[element]))

    entropy = 0

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)
        entropy -= ent

    return entropy, frequency_dict