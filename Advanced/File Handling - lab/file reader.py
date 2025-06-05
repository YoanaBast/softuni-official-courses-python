import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'numbers.txt')
file = open(path)

numbers = [int(x) for x in file.read().split('\n')]
print(sum(numbers))




