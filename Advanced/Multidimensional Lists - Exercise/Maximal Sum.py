rows, cols = [int(x) for x in input().split()]
matrix = []
results = {}

for row_i in range(rows):
    matrix.append( [int(data) for data in input().split() ] )
    if row_i > 1:
        for col_i in range(len(matrix[0])):
            if col_i > 1:
                top_left = matrix[row_i -2][col_i -2]
                top_mid = matrix[row_i -2][col_i -1]
                top_right = matrix[row_i -2][col_i]

                mid_left = matrix[row_i -1][col_i -2]
                mid_mid = matrix[row_i -1][col_i -1]
                mid_right = matrix[row_i -1][col_i]

                bot_left = matrix[row_i][col_i -2]
                bot_mid = matrix[row_i][col_i -1]
                bot_right = matrix[row_i][col_i]

                sumi = sum([top_left, top_mid, top_right, mid_left, mid_mid, mid_right, bot_left, bot_mid, bot_right])
                results[sumi] = [[top_left, top_mid, top_right], [mid_left, mid_mid, mid_right], [bot_left, bot_mid, bot_right]]

max_key = max(results)
print(f"Sum = {max_key}")
for item in results[max_key]:
    print(*item)