import os
import re

from constants import ABSOLUTE_PROJECT_PATH

input_path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'input.txt')
words_path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'words.txt')

with open(words_path) as f1:
    word_contents = f1.read().split()

with open(input_path) as f2:
    text = f2.read()

data = {}
for word in word_contents:
    patter = rf"\b{word}\b"
    count = len(re.findall(patter, text, re.IGNORECASE)) #list
    data[word] = count

data = dict(sorted(data.items(), key=lambda kvp: -kvp[1] ))

for key, value in data.items():
    print(f"{key} - {value}")