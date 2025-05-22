rows, cols = [int(x) for x in input().split()]
matrix = []
equals = 0

for row_i in range(rows):
    matrix.append( [data for data in input().split() ] )
    if row_i > 0:  # 1 2
        for col_i in range(len(matrix[0]) -1 ): # 0 1 2
            above = matrix[row_i-1][col_i+1]
            diagonal_up = matrix[row_i-1][col_i]
            prev = matrix[row_i][col_i]
            current = matrix[row_i][col_i+1]
            if above == diagonal_up == prev == current:
                equals +=1

print(equals)