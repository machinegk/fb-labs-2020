
def encryptor(key, indexed_text, indexed_alphabet):
    text_to_return = []

    key_len = len(key)
    aplphabet_len = len(indexed_alphabet)

    key_list = list(indexed_alphabet.keys())
    val_list = list(indexed_alphabet.values())

    for i in range(0, len(indexed_text)):
        text_to_return.append(key_list[val_list.index((indexed_text[i] + indexed_alphabet[ key[i % key_len]]) % aplphabet_len)])

    return ''.join(text_to_return)
