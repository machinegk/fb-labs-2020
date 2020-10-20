import matplotlib.pyplot as plt
import os
import sys
from funcs import *

file = open(os.path.join(sys.path[0], 'encrypted.txt'), 'r', encoding='UTF-8')
w_file = open(os.path.join(sys.path[0], 'decrypted.txt'), 'a', encoding='UTF-8')

stat_file = open(os.path.join(sys.path[0], 'statistics_text.txt'), 'r', encoding='UTF-8')

stat_text = re.sub(r'[^А-Яа-я]', '', stat_file.read().lower())


text = re.sub(r'\W', '', file.read().lower())


reference_dict = entropy_counter(stat_text)


partial_caesar_decryptor(text, reference_dict, 14)




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
