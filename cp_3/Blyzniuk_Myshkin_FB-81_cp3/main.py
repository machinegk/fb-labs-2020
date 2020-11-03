from funcs import *

exceptions = ["ъ", "ё"]
russian_alphabet = russian_alphabet(exceptions)
indexed_russian_alphabet = index_alphabet(russian_alphabet)

print(russian_alphabet)
print(len(russian_alphabet))
print(indexed_russian_alphabet)
print(len(indexed_russian_alphabet))

stat_file = open("statistics_text.txt", 'r', encoding='UTF-8')
enc_file = open("encrypted.txt", 'r', encoding='UTF-8')

stat_text = re.sub(r'[^А-Яа-я]', '', stat_file.read().lower()).translate(
    str.maketrans({"ъ": "ь", "ё": "е"}))  # Get clear text from file
enc_text = re.sub(r'\W', '', enc_file.read())


stat_frequency, stat_bigrams = bigram(stat_text)
frequency_dict, bigrams = bigram(enc_text)

stat_frequency = OrderedDict(sorted(stat_frequency.items(), key=lambda t: t[1], reverse=True))
frequency_dict = OrderedDict(sorted(frequency_dict.items(), key=lambda t: t[1], reverse=True))

stat_frequency_list, _ = bigram_indexer(['ст', "но", "ен", "то", "на", "ов"], indexed_russian_alphabet)
frequency_dict_list, _ = bigram_indexer(frequency_dict.keys(), indexed_russian_alphabet)

possible_keys_list = param_counter(stat_frequency_list, frequency_dict_list)
print(possible_keys_list)


indexed_bigrams, _ = bigram_indexer(bigrams, indexed_russian_alphabet)
_, reference_bigrams = bigram_indexer(stat_bigrams, indexed_russian_alphabet)

decipher(possible_keys_list, indexed_bigrams, reference_bigrams)

stat_file.close()
enc_file.close()