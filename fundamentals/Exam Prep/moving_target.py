targets = input().split() #str

while True:
    command = input()
    if command == 'End':
        break
    action, index, value = command.split()
    index,value = int(index),int(value)
#SHOOT
    if action == 'Shoot':
        if index <= len(targets) - 1:
            targets[index] = str(int(targets[index]) - value)
            if targets[index] == '0':
                targets.pop(index)
        else:
            print("Invalid placement!")
#ADD
    elif action == 'Add':
        if index <= len(targets) - 1:
            targets[index] = str(value)
        else:
            print("Invalid placement!")
#STRIKE
    elif action == 'Strike':
        if index - value >= 0 and index + value <= len(targets) - 1:
            for striked_index in range(index - value, index + value + 2):
                targets.pop(index - value)
        else:
            print('Strike missed!')

print('|'.join(targets))