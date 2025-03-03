comp_ID_dict = {}


def nice_print_key_value(dict_lookup: dict):
    result = []
    for key in dict_lookup:
        list_values = []
        for value1 in dict_lookup[key]:
            list_values.append(value1)
        result.append(key + '\n-- '+  '\n-- '.join(list_values))
    return '\n'.join(result)


while True:
    command = input()
    if command == 'End':
        break
    company, ID = command.split(' -> ')
    if company not in comp_ID_dict:
        comp_ID_dict[company] = []
    if ID not in comp_ID_dict[company]:
        comp_ID_dict[company].append(ID)

print(nice_print_key_value(comp_ID_dict))