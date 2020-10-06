import re

def cipherWith(key, numberText, alphabet):

    returnedNumberText = numberText
    keyLen = len(key)
    alphLen = len(alphabet)
    for i in range(0, len(returnedNumberText)):
        returnedNumberText[i] = ( returnedNumberText[i] + indexed_alphabet[ (key[i % keyLen]) ] ) % alphLen
        returnedNumberText[i] += 1072
    
    returnedNumberText = ''.join(map(lambda letter: chr(letter), returnedNumberText))
    return returnedNumberText
    


file = open('text.txt', 'r', encoding='UTF-8')
w_file = open('text_encrypted.txt', 'w', encoding='UTF-8')


text = re.sub(r'\W', '', file.read().lower())
print(text)


alphabet = list(map(lambda letter: chr(letter), range(1072, 1104)))


keys = ['да', 'кот', 'лорд', 'салат', 'вкусныйвидеосалат']

indexed_alphabet = {key: v for v, key in enumerate(alphabet)}


numberText = list(map(lambda i: indexed_alphabet[i], text))

key = keys[0]
ciferedText = cipherWith(key, numberText, alphabet)
