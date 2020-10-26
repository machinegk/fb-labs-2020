from funcs import *

exceptions = ["ъ", "ё"]
russian_alphabet = russian_alphabet(exceptions)
indexed_russian_alphabet = indexed_alphabet(russian_alphabet)

print(russian_alphabet)
print(len(russian_alphabet))
print(indexed_russian_alphabet)
print(len(indexed_russian_alphabet))
