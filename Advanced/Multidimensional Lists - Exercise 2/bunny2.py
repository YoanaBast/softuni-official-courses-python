size = int(input())
matrix = []
bun_r, bun_c = 0, 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bun_r, bun_c = row, col

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_eggs = float("-inf")
max_dir = ''
max_eggs_matrix = []

for direction, move in moves.items():
    eggs = 0
    curr_egg_mat = []
    cur_row = bun_r + move[0]
    cur_col = bun_c + move[1]

    while 0 <= cur_row < size and 0 <= cur_col < size:
        if matrix[cur_row][cur_col] == 'X':
            break

        eggs += int(matrix[cur_row][cur_col])
        curr_egg_mat.append([cur_row, cur_col])
        cur_row += move[0]
        cur_col += move[1]