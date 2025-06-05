import os

path  = os.path.join("..", "file_folder", "text.txt")


try:
    file = open(path)
    print('File Found')
    file.close()
except FileNotFoundError:
    print("File not found")

