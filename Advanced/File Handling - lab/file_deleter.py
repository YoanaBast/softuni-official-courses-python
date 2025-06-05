import os
from constants import ABSOLUTE_PROJECT_PATH

try:
    path = os.path.join(ABSOLUTE_PROJECT_PATH, 'file_folder', 'my_first_file.txt')
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")
