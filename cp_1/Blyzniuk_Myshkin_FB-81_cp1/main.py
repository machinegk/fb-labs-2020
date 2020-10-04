from collections import Counter
import re, math
file = open("text.txt", 'r')

spaceless_file = file.read()
spaceless_file = re.sub(r"\W", "", spaceless_file)

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

print("R = " + str(1 - ((ent)/math.log(31,2))))
file.close()
