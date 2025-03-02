metals_dict = {}

def format_for_print(some_dict):
    result = []
    for key, value in some_dict.items():
        result.append(f"{key} -> {value}")
    return '\n'.join(result)


while True:
    command_1 = input()
    if command_1 == 'stop':
        break
    command_2 = input()
    if command_2 == 'stop':
        break
    if command_1 not in metals_dict:
        metals_dict[command_1] = int(command_2)
    else:
        metals_dict[command_1] += int(command_2)

print(format_for_print(metals_dict))