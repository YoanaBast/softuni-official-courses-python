numbers_dictionary = {}

while True:
    line = input()
    if line == 'End':
        break

    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')

    if line == "Search":
        searched = input()
        try:
            print(numbers_dictionary[searched])
        except KeyError:
            print('Number does not exist in dictionary')

    elif line == "Remove":
        searched = input()
        try:
            del numbers_dictionary[searched]
        except KeyError:
            print('Number does not exist in dictionary')

print(numbers_dictionary)
