import re
from funcs import *

file = open('text.txt', 'r', encoding='UTF-8')
w_file = open('text_encrypted.txt', 'w', encoding='UTF-8')

text = re.sub(r'\W', '', file.read().lower())

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']

indexed_text = list(map(lambda i: indexed_alphabet[i], text))



print(encryptor(keys[0], indexed_text, indexed_alphabet))