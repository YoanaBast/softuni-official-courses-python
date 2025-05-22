rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = []
snake_i = 0
for row_i in range(rows):
    data = []
    for col_i in range(cols):
        data.append(snake[snake_i])
        snake_i += 1
        if snake_i == len(snake):
            snake_i = 0

    if row_i % 2 == 1:
        matrix.append(data[::-1])
    else:
        matrix.append(data)

for r in matrix:
    print(''.join(r))