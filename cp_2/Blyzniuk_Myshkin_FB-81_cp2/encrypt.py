import re
import os
import sys
from funcs import encryptor, conformity_index, key_length
# import matplotlib.pyplot as plt

file = open(os.path.join(sys.path[0], 'text.txt'), 'r', encoding='UTF-8')
w_file = open(os.path.join(sys.path[0], 'text_encrypted.txt'), 'a', encoding='UTF-8')

text = re.sub(r'\W', '', file.read().lower())

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']

indexed_text = list(map(lambda i: indexed_alphabet[i], text))

# w_file.write(str(encryptor(keys[0], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[1], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[2], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[3], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[4], indexed_text, indexed_alphabet)) + "\n\n")

print("Conformity index of clear text: " + str(conformity_index(text)))
file.close()
w_file.close()

file = open(os.path.join(sys.path[0], 'text_encrypted.txt'), 'r', encoding='UTF-8')
enc_text = file.read().split("\n\n")

print("Conformity of text encoded with key (2): " + str(conformity_index(enc_text[0])))
print("Conformity of text encoded with key (3): " + str(conformity_index(enc_text[1])))
print("Conformity of text encoded with key (4): " + str(conformity_index(enc_text[2])))
print("Conformity of text encoded with key (5): " + str(conformity_index(enc_text[3])))
print("Conformity of text encoded with key (17): " + str(conformity_index(enc_text[4])))

data_1 = key_length(enc_text[0])
data_2 = key_length(enc_text[1])
data_3 = key_length(enc_text[2])
data_4 = key_length(enc_text[3])
data_5 = key_length(enc_text[4])

print(str(data_1))
print(str(data_2))
print(str(data_3))
print(str(data_4))
print(str(data_5))

# clrs = ['grey' if (x < max(data_1.values())) else 'red' for x in data_1.values()]
# plt.bar(data_1.keys(), data_1.values(), color=clrs)
# plt.show()
# clrs = ['grey' if (x < max(data_2.values())) else 'red' for x in data_2.values()]
# plt.bar(data_2.keys(), data_2.values(), color=clrs)
# plt.show()
# clrs = ['grey' if (x < max(data_3.values())) else 'red' for x in data_3.values()]
# plt.bar(data_3.keys(), data_3.values(), color=clrs)
# plt.show()
# clrs = ['grey' if (x < max(data_4.values())) else 'red' for x in data_4.values()]
# plt.bar(data_4.keys(), data_4.values(), color=clrs)
# plt.show()
# clrs = ['grey' if (x < max(data_5.values())) else 'red' for x in data_5.values()]
# plt.bar(data_5.keys(), data_5.values(), color=clrs)
# plt.show()

file.close()
