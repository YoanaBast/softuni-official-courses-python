from collections import deque

rows, cols = [int(x) for x in input().split()]

directions = {
    'L': (0, -1),
    'R': (0, +1),
    'U': (-1, 0),
    'D': (+1, 0)
}

def bunnies_exapnd(r, c, dirs):
    if dirs == 'U':
        r += directions['U'][0]
        c += directions['U'][1]
    elif dirs == 'D':
        r += directions['D'][0]
        c += directions['D'][1]
    elif dirs == 'L':
        r += directions['L'][0]
        c += directions['L'][1]
    elif dirs == 'R':
        r += directions['R'][0]
        c += directions['R'][1]
    if 0 <= r < rows and 0 <= c < cols:
        return r, c
    else:
        return 0



matrix = []
bunnies = deque([])
s_row, s_col = 0, 0

for r in range(rows):
    data = list(input())
    matrix.append(data)
    if 'P' in data:
        s_row = r
        s_col = data.index('P')
    if 'B' in data:
        y = list(enumerate(data))
        for item in y:
            if item[1] == 'B':
                bunnies.append([r, item[0]])

moves = deque(list(input()))

won = False
lost = False

while moves:
    if lost or won:
        break

    dir_r, dir_c = directions[moves[0]]
    new_r, new_c = (s_row + dir_r), (s_col + dir_c)

    if new_r < 0 or new_r >= rows\
    or new_c < 0 or new_c >= cols:
        won = True
        matrix[s_row][s_col] = '.'

    elif matrix[new_r][new_c] == 'B':
        lost = True

    else:
        matrix[s_row][s_col], matrix[new_r][new_c] = matrix[new_r][new_c], matrix[s_row][s_col]
        s_row, s_col = new_r, new_c
    moves.popleft()

    new_buns = []
    while bunnies:

        bunny = bunnies.popleft()
        for move in directions.keys():
            check = bunnies_exapnd(bunny[0],bunny[1],move)
            if check != 0:
                bun_r, bun_c = check
                if matrix[bun_r][bun_c] == 'P':
                    lost = True

                matrix[bun_r][bun_c] = 'B'
                new_buns.append([bun_r, bun_c])

    bunnies.extend(new_buns)


for m in matrix:
    print(*m, sep='')

if won:
    print(f"won: {s_row} {s_col}")
elif lost:
    print(f"dead: {new_r} {new_c}")