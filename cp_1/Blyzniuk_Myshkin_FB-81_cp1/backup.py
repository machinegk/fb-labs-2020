from collections import Counter
import re, math
file = open("text.txt", 'r', encoding='UTF-8')

spaceless_file = file.read().lower()
spaceless_file = re.sub(r'[^А-Яа-я]', '', spaceless_file)

letters_amount = len(spaceless_file)
counted_letters = Counter(spaceless_file)


print(counted_letters)
print(letters_amount)
frequency_dict = {}

for letter in counted_letters:
    frequency_dict[letter] = counted_letters[letter]/letters_amount

    print("Frequency of " + letter + ' = ' + str(frequency_dict[letter]))

entropy = 0


for letter in frequency_dict:
    ent = frequency_dict[letter] * math.log(frequency_dict[letter], 2)
    entropy -= ent

print("Entropy = " + str(entropy))

print("R = " + str(1 - ((entropy)/math.log(32,2))))

##############################################################################################

letter_pairs = list(map(''.join, zip(spaceless_file, spaceless_file[1:])))

bigrams = Counter(letter_pairs)
bigrams_amount = len(letter_pairs)


frequency_dict = {}
for pair in bigrams:
    frequency_dict[pair] = bigrams[pair] / bigrams_amount

    print("Frequency of " + pair + ' = ' + str(frequency_dict[pair]))

entropy = 0
for pair in frequency_dict:
    ent = frequency_dict[pair] * math.log(frequency_dict[pair], 2)
    entropy -= ent
entropy = entropy/2
print("Entropy = " + str(entropy))

print("R = " + str(1 - ((entropy)/math.log(32,2))))





file.close()
