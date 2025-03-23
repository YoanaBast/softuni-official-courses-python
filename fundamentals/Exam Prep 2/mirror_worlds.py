import re
regex = r'([@|#]{1})(?P<word1>[a-zA-Z]{3,})(\1)(\1)(?P<word2>[a-zA-Z]{3,})(\1)'

text_str = input()
match = re.finditer(regex, text_str)
matches = {}
index = 1
for item in match:
    word_one = item.group('word1')
    word_two = item.group('word2')
    matches[index] = [word_one, word_two]
    index += 1

mirror = {}
index2 = 1
for key in matches.keys():
    word1, word2 = matches[key][0], matches[key][1]
    if word1 == word2[::-1]:
        mirror[index2] = [word1, word2]
        index2 += 1

if len(matches) < 1:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if len(mirror) < 1:
    print("No mirror words!")
else:
    print("The mirror words are:")
    result = []
    for keyx in mirror.keys():
        result.append(f"{mirror[keyx][0]} <=> {mirror[keyx][1]}")
    print(', '.join(result))