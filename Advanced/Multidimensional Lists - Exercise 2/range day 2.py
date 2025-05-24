directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
}

SIZE = 5
range_matrix = []
my_position = []
targets_down = []
targets = 0

for row in range(SIZE):
    range_matrix.append(input().split())
    for col in range(SIZE):
        if range_matrix[row][col] == 'A':
            my_position = [row, col]
        elif range_matrix[row][col] == 'x':
            targets += 1


for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        shoot_r = my_position[0] + directions[command[1]][0]
        shoot_c = my_position[1] + directions[command[1]][1]

        while 0 <= shoot_r < SIZE and 0 <= shoot_c < SIZE:
            if range_matrix[shoot_r][shoot_c] == 'x':
                range_matrix[shoot_r][shoot_c] = '.'
                targets -= 1
                targets_down.append([shoot_r, shoot_c])
                break
            shoot_r += directions[command[1]][0]
            shoot_c += directions[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == 'move':
        curr_r= my_position[0] + directions[command[1]][0] * int(command[2])
        curr_c = my_position[1] + directions[command[1]][1] * int(command[2])

        if 0 <= curr_r < SIZE and 0 <= curr_c < SIZE:
            if range_matrix[curr_r][curr_c] == '.':

                range_matrix[curr_r][curr_c] = 'A'
                range_matrix[my_position[0]][my_position[1]] = '.'
                my_position = [curr_r, curr_c]


if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(shot) for shot in targets_down]
