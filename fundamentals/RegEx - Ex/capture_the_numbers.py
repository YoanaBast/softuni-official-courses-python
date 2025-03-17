import re

pattern = r'\d+'

line = input() # initial line
while line: # will break the loop if line is empty
    match = re.findall(pattern, line)

    if match:
        print(' '.join(match), end=' ')

    line = input() # gives new line each time

