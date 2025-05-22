primary = []
secondary = []
matrix = []

for row_i in range(int(input())) : # 0 1 2
    matrix.append([int(data) for data in input().split(', ')] )
    col_i = row_i
    primary.append(matrix[row_i][col_i])
    secondary.append(matrix[row_i][-col_i-1])

print(f"Primary diagonal: {', '.join(map(str, primary))}. Sum: {sum(primary)} ")
print(f"Secondary diagonal: {', '.join(map(str, secondary))}. Sum: {sum(secondary)}")
