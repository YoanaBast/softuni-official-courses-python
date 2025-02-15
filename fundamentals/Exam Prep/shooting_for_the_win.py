targets = input().split()

while True:
    command = input()
    if command == 'End':
        break

    index = int(command)

    if index <= len(targets) - 1:
        current_target_mod = int(targets[index])
        targets[index] = '-1'

        position = -1
        for target in targets:
            position += 1
            if int(target) != -1 and int(target) > current_target_mod:
                targets[position] = str(int(target) - current_target_mod)
            elif int(target) != -1 and int(target) <= current_target_mod:
                targets[position] = str(int(target) + current_target_mod)

shot_targets = targets.count('-1')
print(f"Shot targets: {shot_targets} -> {' '.join(list(map(str, targets)))}")