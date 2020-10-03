from collections import Counter
import re
file = open("text.txt", 'r')

spaceless_file = file.read()
spaceless_file = re.sub(r"\W", "", spaceless_file)

letters_amount = len (spaceless_file)
counted_letters = Counter(spaceless_file)

print(counted_letters)
print(letters_amount)

for letter in counted_letters:
    print("Frequency of " + letter + ' = ' + str(counted_letters[letter]/letters_amount))

file.close()
