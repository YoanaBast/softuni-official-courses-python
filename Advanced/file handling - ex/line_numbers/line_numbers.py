text_path = 'text.txt'
output = 'output.txt'

syms = {"-", ",", ".", "!", "?", "'"}
lines = []

with open(output, 'a') as o, open(text_path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            no_spaces = line.replace(" ", "")
            s = 0
            for x in syms:
                s += line.count(x)
            o.write(f'Line {i + 1}: {line} ({(len(no_spaces) - s)})({s})\n')

# make sure the output file is empty before running

