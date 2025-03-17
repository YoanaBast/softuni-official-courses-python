import re
match = ''

line = input() # initial line
while line: # will break the loop if line is empty
    pattern = r'\d+'
    match = re.findall(pattern, line)

    if match:
        print(' '.join(match), end=' ')

    line = input() # gives new line each time

