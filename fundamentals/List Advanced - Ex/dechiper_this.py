# # the second and the last letter are switched (e.g., Holle means Hello)
# # · the first letter is replaced by its character code (e.g., 72 means H
words = input().split(' ')
dechi = []
for word in words:
    digi = ' '
    index = -1
    for char in word:
        if char.isdigit():
            digi += str(char)
            index += 1
    letter = chr(int(digi))
    no_num = letter + word[index + 1::]
    dechi.append(no_num)

def replacer(word: str) -> str:
    second = 1
    last = -1
    if len(word) > 2:
        replace = word[:second] + word[last::] + word[second + 1:last] + word[second:second +1:]
        return replace
    else:
        return word

result = [replacer(dech) for dech in dechi]
print(*result)