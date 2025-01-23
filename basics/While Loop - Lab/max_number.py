import sys
min_num = sys.maxsize

while True:
    command = input()
    if command == 'Stop':
        break

    number = int(command)
    if number < min_num:
        min_num = number
print(min_num)