import re
regex = r"!(?P<com>[A-Z]{1}[a-z]{2,})!:\[(?P<valid>[A-z]{8,})\]"

inputs = int(input())

valid = 'nope'
com = ''
for _ in range(inputs):
    stringche = input()
    match = re.finditer(regex, stringche)
    for mat in match:
        valid = mat.group('valid')
        com = mat.group('com')

    if valid == 'nope':
        print('The message is invalid')
        valid = 'nope'
        com = ''
    else:
        translated = [ord(char) for char in valid]
        print(f"{com}: {' '.join(map(str, translated))}")
        valid = 'nope'
        com = ''