r = input().split('|')
matrix = []
for i in range(len(r)):
    data = r[i].split()
    if data:
        matrix.append(data)
matrix_2 = matrix[::-1]

for x in matrix_2:
    print(' '.join(x), end=' ')
