import re




file = open('text.txt', 'r', encoding='UTF-8')
w_file = open('text_encrypted.txt', 'w', encoding='UTF-8')


text = re.sub(r'\W', '', file.read().lower())
print(text)


alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))


key1 = 'да'
key2 = 'кот'
key3 = 'лорд'
key4 = 'салат'
key5 = 'вкусныйвидеосалат'


indexed_alphabet = {key: v for v, key in enumerate(alphabet)}
print (indexed_alphabet)

list = list(map(lambda i: indexed_alphabet[i], text))
print(list)
keyLen = len(key1)
alphLen = len(alphabet)
for i in range(0, len(list)):
    list[i] = ( list[i] + indexed_alphabet[ (key1[i % keyLen]) ] ) % alphLen
    
    
print(list)

print(indexed_alphabet)
