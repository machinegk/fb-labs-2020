import re
from funcs import encryptor, conformity_index, key_length

file = open('text.txt', 'r', encoding='UTF-8')
w_file = open('text_encrypted.txt', 'a', encoding='UTF-8')

text = re.sub(r'\W', '', file.read().lower())

alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))
indexed_alphabet = {key: v for v, key in enumerate(alphabet)}

keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']

indexed_text = list(map(lambda i: indexed_alphabet[i], text))

# w_file.write(str(encryptor(keys[0], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[1], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[2], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[3], indexed_text, indexed_alphabet)) + "\n\n")
# w_file.write(str(encryptor(keys[4], indexed_text, indexed_alphabet)) + "\n\n")

print("Conformity index of clear text: " + str(conformity_index(text)))
file.close()
w_file.close()

file = open('text_encrypted.txt', 'r', encoding='UTF-8')
enc_text = file.read().split("\n\n")

print("Conformity of text encoded with key (2): " + str(conformity_index(enc_text[0])))
print("Conformity of text encoded with key (3): " + str(conformity_index(enc_text[1])))
print("Conformity of text encoded with key (4): " + str(conformity_index(enc_text[2])))
print("Conformity of text encoded with key (5): " + str(conformity_index(enc_text[3])))
print("Conformity of text encoded with key (17): " + str(conformity_index(enc_text[4])))

print (str(key_length(enc_text[0])))
print (str(key_length(enc_text[1])))
print (str(key_length(enc_text[2])))
print (str(key_length(enc_text[3])))
print (str(key_length(enc_text[4])))


file.close()