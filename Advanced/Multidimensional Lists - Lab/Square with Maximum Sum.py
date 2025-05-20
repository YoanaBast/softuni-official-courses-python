row, column = [int(x) for x in input().split(', ')]

matrix = [
    [int(x) for x in input().split(', ')] for row in range(row)
]

row_index, column_index  = 1, 1
sumi = 0
all_sums = {}

for row_index in range(row-1):
    for column_index in range(column-1):

        current = matrix[row_index][column_index]
        below = matrix[row_index+1][column_index]
        next = matrix[row_index][column_index + 1]
        diagonal = matrix[row_index + 1][column_index + 1]
        sumi = current + below + next + diagonal

        if sumi not in all_sums:
            all_sums[sumi] = [[current, next], [below, diagonal]]


max_key = max(all_sums)

f_row, f_column = all_sums[max_key]

print(*f_row)
print(*f_column)

print(max_key)