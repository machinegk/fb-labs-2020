
def encryptor(key, indexed_text, indexed_alphabet):
    key_len = len(key)
    aplphabet_len = len(indexed_alphabet)

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for i in range(0, len(indexed_text)):
        indexed_text[i] = (indexed_text[i] + indexed_alphabet[ key[i % key_len ]]) % aplphabet_len
        indexed_text[i] = key_list[val_list.index(indexed_text[i])]

    return ''.join(indexed_text)
