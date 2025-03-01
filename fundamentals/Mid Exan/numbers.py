sequence_list_int = list(map(int, input().split()))

while True:
    command = input()
    if command == 'Finish':
        break

    command_split = command.split()
    action, value = command_split[0], int(command_split[1])
    if len(command_split) > 2:
        replacement = int(command_split[2])

    if action == 'Add':
        sequence_list_int.append(value)

    elif action == 'Remove':
        count_value = sequence_list_int.count(value)
        if count_value > 0:
            sequence_list_int.remove(value)

    elif action == 'Replace':
        if value in sequence_list_int:
            value_index = sequence_list_int.index(value)
            sequence_list_int[value_index] = replacement

    elif action == 'Collapse':
        sequence_list_int = [num for num in sequence_list_int if num >= value]

print(*sequence_list_int)

