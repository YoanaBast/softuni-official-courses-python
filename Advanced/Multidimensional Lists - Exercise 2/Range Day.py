directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)
}

ranged_size = 5
range_matrix = []
ass_r, ass_c = 0, 0
shots = []
targets = 0

for row in range(ranged_size):
    range_matrix.append(input().split())
    for col in range(len(range_matrix[0])):
        if range_matrix[row][col] == 'A':
            ass_r, ass_c = row, col
        elif range_matrix[row][col] == 'x':
            targets += 1

curr_r, curr_c = ass_r, ass_c
targets_left = targets

commands_n = int(input())
for _ in range(commands_n):
    command = input().split()

    if command[0] == "shoot":
        shoot_r, shoot_c = curr_r, curr_c
        sr, sc = directions[command[1]][0], directions[command[1]][1]
        while True:
            if 0 <= shoot_r + sr < ranged_size \
            and 0 <= shoot_c + sc < ranged_size:
                # print(range_matrix[shoot_r][shoot_c])
                shoot_r += sr
                shoot_c += sc
                # print(f'shoot_r {shoot_r}')
                # print(f'shoot_c  {shoot_c}')
                # print(range_matrix[shoot_r][shoot_c])

                if range_matrix[shoot_r][shoot_c] == 'x':
                    shots.append([shoot_r, shoot_c])
                    targets_left -= 1
                    range_matrix[shoot_r][shoot_c] = '.'
                    # print(shots)
                    break
            else:
                break
    if targets_left == 0: #TOVA E EDNOTO
        break
    elif command[0] == 'move':
        mr, mc = directions[command[1]][0], directions[command[1]][1]
        steps = int(command[2])

        # print(f'curr r {curr_r}')
        # print(f'curr c {curr_c}')
        # print(f'mr {mr}')
        # print(f'mc {mc}')
        for _ in range(steps):
            if 0 <= curr_r + mr < ranged_size\
            and 0 <= curr_c + mc < ranged_size:
                # print(range_matrix[curr_r + mr][curr_c + mc])
                if range_matrix[curr_r + mr][curr_c + mc] == '.':

                    range_matrix[curr_r][curr_c] = '.'
                    range_matrix[curr_r + mr][curr_c + mc] = 'A'
                    curr_r += mr
                    curr_c += mc
                    # print('swap')



                # print(f'curr r {curr_r}')
                # print(f'curr c {curr_c}')

if targets_left:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {targets} targets hit.")
for shot in shots:
    print(shot)
