import matplotlib.pyplot as plt
import os
import sys
from funcs import *

file = open(os.path.join(sys.path[0], 'encrypted.txt'), 'r', encoding='UTF-8')
w_file = open(os.path.join(sys.path[0], 'decrypted.txt'), 'a', encoding='UTF-8')


alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

text = re.sub(r'\W', '', file.read().lower())
indexed_text = list(map(lambda i: indexed_alphabet[i], text))

stat_file = open(os.path.join(sys.path[0], 'statistics_text.txt'), 'r', encoding='UTF-8')
stat_text = re.sub(r'[^А-Яа-я]', '', stat_file.read().lower())

reference_dict = entropy_counter(stat_text)


data = key_length(text)
print("Conformity of text : " + str(conformity_index(text)))


print(str(data))
clrs = ['grey' if (x < max(data.values())) else 'red' for x in data.values()]
plt.bar(data.keys(), data.values(), color=clrs)
plt.show()


partial_caesar_decryptor(text, reference_dict, 14)
decrypted_text = decryptor('последнийдозор', indexed_text, indexed_alphabet)
w_file.write(" ".join(wordninja.split(decrypted_text)))



file.close()
w_file.close()
stat_file.close()
