import re
import os
import sys
from funcs import encryptor, conformity_index, key_length
import matplotlib.pyplot as plt

file = open(os.path.join(sys.path[0], 'text.txt'), 'r', encoding='UTF-8')
w_file = open(os.path.join(sys.path[0], 'text_encrypted.txt'), 'a', encoding='UTF-8')

text = re.sub(r'\W', '', file.read().lower())

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']

indexed_text = list(map(lambda i: indexed_alphabet[i], text))

print("Conformity index of clear text: " + str(conformity_index(text)))

for i in range(0, len(keys)):

    encrypted_text = encryptor(keys[i], indexed_text, indexed_alphabet)
    encrypted_text_conformity = conformity_index(encrypted_text)
    keys_conformity = key_length(encrypted_text)
    print(str("\n" + "KEY: " + keys[i] + "\n\n" + encrypted_text + "\n\n" + str(keys_conformity) + "\n"))
    # w_file.write(str("\n\n" + "KEY: " + keys[i] + "\n" + encrypted_text + "\n\n")

    clrs = ['grey' if (x < max(keys_conformity.values())) else 'red' for x in keys_conformity.values()]
    plt.bar(keys_conformity.keys(), keys_conformity.values(), color=clrs)
    plt.show()

file.close()
w_file.close()
