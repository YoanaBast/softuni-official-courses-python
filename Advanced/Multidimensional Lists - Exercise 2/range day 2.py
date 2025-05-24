directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
}

SIZE = 5
range_matrix = []
my_position = []
shots = []
targets = 0

for row in range(SIZE):
    range_matrix.append(input().split())
    for col in range(SIZE):
        if range_matrix[row][col] == 'A':
            my_position = [row, col]
        elif range_matrix[row][col] == 'x':
            targets += 1

targets_left = targets

for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        shoot_r = my_position[0] + directions[command[1]][0]
        shoot_c = my_position[1] + directions[command[1]][1]

        while 0 <= shoot_r < SIZE and 0 <= shoot_c < SIZE:
            if range_matrix[shoot_r][shoot_c] == 'x':
                range_matrix[shoot_r][shoot_c] = '.'
                targets_left -= 1
                shots.append([shoot_r, shoot_c])
                break
            shoot_r += directions[command[1]][0]
            shoot_c += directions[command[1]][1]

        if targets_left == 0:
            print(f"Training completed! All {targets} targets hit.")
            break

    elif command[0] == 'move':
        curr_r= my_position[0] + directions[command[1]][0]
        curr_c = my_position[1] + directions[command[1]][1]
        steps = int(command[2])


        for _ in range(steps):
            if 0 <= curr_r < SIZE\
            and 0 <= curr_c < SIZE:
                if range_matrix[curr_r][curr_c] == '.':

                    range_matrix[curr_r][curr_c] = '.'
                    range_matrix[curr_r - directions[command[1]][0]][curr_c - directions[command[1]][1]] = 'A'
                    my_position = [curr_r, curr_c]


                    # print('swap')



                # print(f'curr r {curr_r}')
                # print(f'curr c {curr_c}')


    print(f"Training completed! All {targets} targets hit.")
for shot in shots:
    print(shot)
