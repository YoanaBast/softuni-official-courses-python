lot = {}

def nice_print_key_value(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key} => {value}")
    return '\n'.join(result)

num = int(input())
for _ in range(num):
    command = input().split()
    if command[0] == 'register':
        name, plate = command[1], command[2]
        if name not in lot:
            lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == 'unregister':
        name = command[1]
        if name not in lot:
            print(f"ERROR: user {name} not found")
        else:
            lot.pop(name)
            print(f"{name} unregistered successfully")

print(nice_print_key_value(lot))