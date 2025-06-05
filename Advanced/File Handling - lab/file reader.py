import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'numbers.txt')

with open(path) as file: # with manager - file is open only for the indented block and will close as soon as the block ends
    numbers = [int(x) for x in file.read().split('\n')]
    print(sum(numbers))

print(file.closed)



