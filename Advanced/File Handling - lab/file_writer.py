import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'my_first_file.txt')

with open(path, 'w') as f:
    f.write("I just created my first file!")