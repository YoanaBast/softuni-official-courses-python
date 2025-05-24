from collections import deque

matrix = []
bun_st_r, bun_st_col = 0, 0
# traps = set()
collected = {}

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}

rows = cols = int(input())

for row in range(rows):
    data = input().split()
    matrix.append(data)
    for col, dat in enumerate(data):
        if dat == 'B':
            bun_st_r, bun_st_col = row, col
        # elif dat == 'X':
        #     traps.add((row, col))


for dire in directions:
    collected[dire] = {}
    mid = []
    new_r, new_c = bun_st_r, bun_st_col
    sum_eggs = 0
    while True:
        new_r, new_c = directions[dire](new_r, new_c)
        if new_r < 0 or new_c < 0\
            or new_r >= rows or new_c >= cols:
            break
        if matrix[new_r][new_c] == 'X':

            break

        egg = int(matrix[new_r][new_c])
        mid.append(new_r)
        mid.append(new_c)
        sum_eggs += egg

    collected[dire] = (mid, sum_eggs)

max_key, max_value = max(collected.items(), key=lambda item: item[1][-1])

pairs = [max_value[0][i:i+2] for i in range(0, len(max_value[0]), 2)]

total_eggs = max_value[1]

print(max_key)
for pair in pairs:
    print(pair)
print(total_eggs)
