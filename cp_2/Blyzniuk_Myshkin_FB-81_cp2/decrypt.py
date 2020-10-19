import re
import matplotlib.pyplot as plt

from funcs import *

file = open('encrypted.txt', 'r', encoding='UTF-8')
w_file = open('decrypted.txt', 'a', encoding='UTF-8')


text = re.sub(r'\W', '', file.read().lower())


data = key_length(text)
print("Conformity of text : " + str(conformity_index(text)))

print (str(data))
clrs = ['grey' if (x < max(data.values())) else 'red' for x in data.values() ]
plt.bar(data.keys(), data.values(), color=clrs)
plt.show()

