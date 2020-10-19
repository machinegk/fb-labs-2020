import matplotlib.pyplot as plt

from funcs import *

file = open('encrypted.txt', 'r', encoding='UTF-8')
w_file = open('decrypted.txt', 'a', encoding='UTF-8')

stat_file = open('statistics_text.txt', 'r', encoding='UTF-8')
stat_text = re.sub(r'[^А-Яа-я]', '', stat_file.read().lower())

monograms = monogram_counter(stat_text)


text = re.sub(r'\W', '', file.read().lower())

print(monograms)

partial_caesar_decryptor(text, monograms, 14)






# data = key_length(text)
# print("Conformity of text : " + str(conformity_index(text)))
#
# print (str(data))
# clrs = ['grey' if (x < max(data.values())) else 'red' for x in data.values() ]
# plt.bar(data.keys(), data.values(), color=clrs)
# plt.show()

file.close()
w_file.close()
stat_file.close()
