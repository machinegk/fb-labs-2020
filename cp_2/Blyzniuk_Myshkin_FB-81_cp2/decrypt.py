from funcs import conformity_index
import re

file = open('encrypted.txt', 'r', encoding='UTF-8')
w_file = open('decrypted.txt', 'a', encoding='UTF-8')


text = re.sub(r'\W', '', file.read().lower())


letter_frequency = conformity_index(text)

print(letter_frequency)