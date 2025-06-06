
text_path = 'text.txt'
syms = {"-", ",", ".", "!", "?"}

lines = []
with open(text_path) as f:
    for index, line in enumerate(f):
        if index % 2 == 0:
            for char in syms:
                line = line.replace(char, '@')
            lines.append(list(reversed(line.split())))

for item in lines:
    print(' '.join(item))