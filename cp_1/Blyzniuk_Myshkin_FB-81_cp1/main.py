from funcs import *

file = open("text.txt", 'r', encoding='UTF-8')

space_file, spaceless_file = extra_remover(file)

onegram(space_file)

bigram(space_file, spaceless_file)



file.close()
