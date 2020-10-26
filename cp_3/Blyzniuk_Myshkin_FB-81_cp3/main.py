from funcs import *

exceptions = ["ъ", "ё"]
russian_alphabet = russian_alphabet(exceptions)
indexed_russian_alphabet = indexed_alphabet(russian_alphabet)

print(russian_alphabet)
print(len(russian_alphabet))
print(indexed_russian_alphabet)
print(len(indexed_russian_alphabet))

stat_file = open("statistics_text.txt", 'r', encoding='UTF-8')
enc_file = open("encrypted.txt", 'r', encoding='UTF-8')

stat_text = re.sub(r'\W', '', stat_file.read().lower()).translate(
    str.maketrans({"ъ": "ь", "ё": "е"}))  # Get clear text from file
enc_text = re.sub(r'\W', '', enc_file.read())

frequency_dict, bigrams = bigram(enc_text)
print(bigram_indexer(bigrams, indexed_russian_alphabet))



stat_file.close()

find_opposite(5, 7)
find_opposite(13, 2)
find_opposite(54, 61)
find_opposite(51, 254)
find_opposite(255, 31)