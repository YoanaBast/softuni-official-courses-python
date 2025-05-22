rows, cols = [int(x) for x in input().split()]
matrix = []
# chr(97) = a
i = ii = iii = 96

for row_i in range(rows):
    data = []
    ii = i
    i += 1
    iii += 1
    for col_i in range(cols):
        ii += 1
        d = chr(i) + chr(ii) + chr(iii)
        data.append(d)
    matrix.append(data)

for R in matrix:
    print(*R)