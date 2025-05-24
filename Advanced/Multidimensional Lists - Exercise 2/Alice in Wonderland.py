directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


size = int(input())
matrix = []
alice_r, alice_c = 0, 0
tea = 0


for row in range(size):
    matrix.append(input().split())
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'A':
            alice_r, alice_c = row, col

curr_r, curr_c = alice_r, alice_c

while tea < 10:
    command = input()
    if command in directions:
        nr, nc = directions[command][0], directions[command][1]

        if 0 <= curr_r + nr < size \
        and 0 <= curr_c + nc < size:
            curr_r += nr
            curr_c += nc
            # print(curr_r, curr_c)

            if matrix[curr_r][curr_c] == 'R':
                matrix[curr_r][curr_c] = '*'
                print("Alice didn't make it to the tea party.")
                break

            if matrix[curr_r][curr_c].isdigit():
                tea += int(matrix[curr_r][curr_c])
                # print(tea)

            matrix[curr_r][curr_c] = '*'

        else:
            print("Alice didn't make it to the tea party.")
            break

        # print(matrix[curr_r][curr_c])

matrix[alice_r][alice_c] = '*'

if tea >= 10:
    print("She did it! She went to the party.")
for m in matrix:
    print(*m)