message = input()

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        print(f"You have a new text message: {message}")
        break

    elif command[0] == 'ChangeAll':
        message = message.replace(command[1], command[2])
        print(message)

    elif command[0] == 'Reverse':
        if command[1] in message:
            message = message.replace(command[1], ''.join(reversed(command[1])))
            print(message)
        else:
            print('error')

    elif command[0] == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

