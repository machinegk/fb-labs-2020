from collections import Counter
import re
file = open("text.txt", 'r')

spaceless_file = file.read()
spaceless_file = re.sub(r"\W", "", spaceless_file)

counted_letters = Counter(spaceless_file)

file.close()
