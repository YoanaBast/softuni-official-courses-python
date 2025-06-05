received_str = input()

command = input().split()
while True:
    if command[0] == 'End':
        break

    elif command[0] == 'Translate':  # "Translate {char} {replacement}"
        char, replacement = command[1], command[2]
        mytable = str.maketrans(char, replacement)
        received_str = received_str.translate(mytable)
        print(received_str)

    elif command[0] == 'Includes':  # "Includes {substring}"
        substring = command[1]
        if substring in received_str:
            print('True')
        else:
            print('False')

    elif command[0] == 'Start':  # "Start {substring}"
        substring = command[1]
        if received_str[:len(substring)] == substring:
            print('True')
        else:
            print('False')

    elif command[0] == 'Lowercase':  # "Lowercase"
        received_str = received_str.lower()
        print(received_str)

    elif command[0] == 'FindIndex':  # "FindIndex {char}"
        char = command[1]
        found = received_str.rfind(char)
        print(found)

    elif command[0] == 'Remove':  #  "Remove {startIndex} {count}"
        startIndex, count = int(command[1]), int(command[2])
        received_str = received_str[:startIndex] + '' + received_str[startIndex+count:]
        print(received_str)

    command = input().split()
