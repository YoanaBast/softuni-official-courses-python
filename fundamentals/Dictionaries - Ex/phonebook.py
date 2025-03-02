phonebook_dict = {}
num_searches = 0

def search(some_dict):
    result = []
    for i in range(num_searches):
        person = input()
        if person in phonebook_dict:
            result.append(f"{person} -> {phonebook_dict[person]}")
        else:
            result.append(f"Contact {person} does not exist.")
    return '\n'.join(result)

while True:
    command = input()
    if '-' not in command:
        num_searches = int(command)
        break
    else:
        contact, number = command.split('-')
        phonebook_dict[contact] = number

print(search(phonebook_dict))