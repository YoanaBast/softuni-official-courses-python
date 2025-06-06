
text_path = 'text.txt'
syms = {"-", ",", ".", "!", "?"}

lines = []
with open(text_path) as f:
    for index, line in enumerate(f):
        if index % 2 == 0:
            line_lst = line.split()

            for inx, word in enumerate(line_lst):
                for char in word:
                    if char in syms:
                        word = word.replace(char, '@')
                        line_lst[inx] = word
            line_lst = list(reversed(line_lst))
            lines.append(line_lst)


for item in lines:
    print(' '.join(item))