from collections import Counter, OrderedDict
import re, math


def extra_remover(file):
    space_file = file.read().lower()  # Read data from file and convert to lowercase
    space_file = re.sub(r'[^А-Яа-я ]', '',
                        space_file)  # Remove all the characters, accept for cyrillic letters and whitespaces
    spaceless_file = re.sub(r'\W', '', space_file)  # Remove also whitespaces
    return space_file, spaceless_file


def monogram(space_file):
    s_letters_amount = len(space_file)  # Get amount of symbols in file with spaces
    s_counted_letters = Counter(space_file)  # Get a dict with frequency of each letter

    s_counted_letters = OrderedDict(sorted(s_counted_letters.items(), key=lambda t: t[0])) # Sorts the dict

    entropy, frequency_dict = stuff_counter(s_counted_letters,
                                            s_letters_amount)  # Get overall entropy and counted frequency of each
    # letter

    print("Entropy with spaces = " + str(entropy))  # Print the result
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Print the redundancy

    ent = frequency_dict[' '] * math.log(frequency_dict[' '], 2)  # Count the entropy of whitespaces

    entropy += ent  # Get rid of that value in our overall entropy
    print("Entropy without spaces = " + str(entropy))  # Print entropy of the text without whitespaces
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy without whitespaces


def bigram(space_file, spaceless_file):
    s_letter_pairs = re.findall(r'..', space_file)
    s_bigrams = Counter(s_letter_pairs)  # Count the frequency of each pair of letters in the text
    s_bigrams = OrderedDict(sorted(s_bigrams.items(), key=lambda t: t[0]))  # Sorts the dict
    s_bigrams_amount = len(s_letter_pairs)  # Return amount of pair of the letters

    entropy, frequency_dict = stuff_counter(s_bigrams, s_bigrams_amount)# Return overall entropy for the pairs with

    # whitespaces and the dict with frequency of
    # each pair
    entropy = entropy / 2  # Get proper value of entropy for text
    print("Entropy with spaces = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy


    #######################################################################
    s_letter_pairs_crossed = list(map(''.join, zip(space_file, space_file[1:])))  # Get letter pairs (including whitespaces)
    s_bigrams_crossed = Counter(s_letter_pairs_crossed)  # Count the frequency of each pair of letters in the text
    s_bigrams_crossed= OrderedDict(sorted(s_bigrams_crossed.items(), key=lambda t: t[0])) # Sorts the dict
    s_bigrams_amount = len(s_letter_pairs_crossed)  # Return amount of pair of the letters

    entropy, frequency_dict = stuff_counter(s_bigrams_crossed, s_bigrams_amount)  # Return overall entropy for the pairs with

    # whitespaces and the dict with frequency of
    # each pair
    entropy = entropy / 2  # Get proper value of entropy for text
    print("Entropy with spaces (crossed) = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy

    letter_pairs = re.findall(r'..', spaceless_file)
    bigrams = Counter(letter_pairs)  # Count the frequency of each pair of letters in the text
    bigrams = OrderedDict(sorted(bigrams.items(), key=lambda t: t[0]))  # Sorts the dict
    bigrams_amount = len(letter_pairs)  # Return amount of pair of the letters

    entropy, frequency_dict = stuff_counter(bigrams, bigrams_amount)

    entropy = entropy / 2  # Get proper value of entropy for text
    print("Entropy without spaces = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy

    letter_pairs_crossed = list(map(''.join, zip(spaceless_file, spaceless_file[1:])))  # Get letter pairs without whitespaces
    bigrams_crossed = Counter(letter_pairs_crossed)  # Count the frequency of each pair of letters in the text
    bigrams_crossed = OrderedDict(sorted(bigrams_crossed.items(), key=lambda t: t[0])) # Sorts the dict
    bigrams_amount = len(letter_pairs_crossed)  # Return amount of pair of the letters

    entropy, frequency_dict = stuff_counter(bigrams_crossed, bigrams_amount)  # Return overall entropy for the pairs with
    # whitespaces and the dict with frequency of
    # each pair
    entropy = entropy / 2  # Get proper value of entropy for text
    print("Entropy without spaces (crossed) = " + str(entropy))  # Print that value
    print("R = " + str(1 - (entropy / math.log(32, 2))))  # Count the redundancy


def stuff_counter(counted, amount):
    frequency_dict = {}  # Create empty dict for letter frequency

    for element in counted:
        frequency_dict[element] = counted[element] / amount  # Count frequency for each element
        print("Frequency of " + element + ' = ' + str(frequency_dict[element]))  # Print frequency for each element

    entropy = 0  # Define starting value of entropy

    for element in frequency_dict:
        ent = frequency_dict[element] * math.log(frequency_dict[element], 2)  # Count entropy for each element
        entropy -= ent  # Count overall entropy



    return entropy, frequency_dict # Return value of entropy and frequency dictionary
