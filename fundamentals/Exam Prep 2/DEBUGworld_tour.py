stops = input()

command = input().split(':')
while True:
    if command[0] == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    elif command[0] == 'Add Stop': # "Add Stop:{index}:{string}"
    # Insert the given string at that index only if the index is valid.
        index, string = int(command[1]), command[2]
        if index <= len(stops):
            stops = stops[:index] + string + stops[index:]
            print(stops)

    elif command[0] == 'Remove Stop':  # "Remove Stop:{start_index}:{end_index}"
    # Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid.
        start_index, end_index = int(command[1]), int(command[2])
        if start_index < len(stops) and end_index <= len(stops):
            stops = stops[:start_index] + '' + stops[end_index+1:]
        print(stops)

    elif command[0] == 'Switch':  # "Switch:{old_string}:{new_string}"
    # If the old string is in the initial string, replace it with the new one (all occurrences)
        old_string, new_string = command[1], command[2]
        while old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    command = input().split(':')
