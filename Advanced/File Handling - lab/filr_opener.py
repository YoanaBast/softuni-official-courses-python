import os

path  = os.path.join("..", "file_folder", "text.xt")


try:
    open(path)
    print('File Found')
except FileNotFoundError:
    print("File not found")

close(path)