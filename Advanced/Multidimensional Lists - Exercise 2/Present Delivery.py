directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

presents = int(input())
size = int(input())
matrix = []
santa_p = []
nice_kids = 0
nice_kids_presents = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_p = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1

while presents:
    command = input()
    if command == "Christmas morning":
        break

    if command in directions:
        r = directions[command][0] + santa_p[0]
        c = directions[command][1] + santa_p[1]

        if 0 <= r < size and 0 <= c < size:

            if matrix[r][c] == 'V':
                presents -= 1
                nice_kids_presents += 1
                matrix[r][c] = 'S'
                matrix[santa_p[0]][santa_p[1]] = '-'
                santa_p = [r, c]

            elif matrix[r][c] == 'C':

                for move in directions:
                    r1 = r + directions[move][0]
                    c1 = c + directions[move][1]

                    if 0 <= r1 < size and 0 <= c1 < size:
                        if matrix[r1][c1] == 'V':
                            presents -= 1
                            nice_kids_presents += 1
                            matrix[r1][c1] = '-'

                        elif matrix[r1][c1] == 'X':
                            presents -= 1
                            matrix[r1][c1] = '-'

                matrix[r][c] = 'S'
                matrix[santa_p[0]][santa_p[1]] = '-'

                santa_p = [r, c]

            else:
                matrix[r][c] = 'S'
                matrix[santa_p[0]][santa_p[1]] = '-'
                santa_p = [r, c]


if nice_kids_presents < nice_kids and not presents:
    print("Santa ran out of presents!")

for m in matrix:
    print(*m)

if nice_kids_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_presents} nice kid/s.")