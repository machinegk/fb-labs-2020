from funcs import * # Import all the stuff from file with functions

file = open("text.txt", 'r', encoding='UTF-8') # Open file with proper encoding

space_file, spaceless_file = extra_remover(file)

onegram(space_file)

bigram(space_file, spaceless_file)


file.close() # Closing opened file
