import re
regex = r'www\.[A-Za-z0-9\-]+\.[a-z]+(?:\.[a-z]+)*'

text = input()
while text:
    match = re.findall(regex, text)

    if match:
        print('\n'.join(match))

    text = input()
