rows = cols = int(input())
matrix = []
bun_st_r, bun_st_col = 0, 0
for row in range(rows):
    data = input().split()
    matrix.append(data)
    for col, dat in enumerate(data):
        if dat == 'B':
            bun_st_r, bun_st_col = row, col
