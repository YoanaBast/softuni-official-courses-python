rows, cols = [int(x) for x in input().split()]
matrix = [
    [data for data in input().split()] for _ in range(rows)
]

while True:
    command = input().split()
    if command[0] == 'END':
        break

    elif len(command) == 5 and command[0] == "swap":
        row1 = int(command[1])
        col1 = int(command[2])

        row2 = int(command[3])
        col2 = int(command[4])

        if (row1 < len(matrix) and row1 < len(matrix) and
                col1 < len(matrix[0])) and col2 < len(matrix[0]):
            el1 = matrix[row1][col1]
            el2 = matrix[row2][col2]

            matrix[row1][col1] = el2
            matrix[row2][col2] = el1

            for rrr in matrix:
                print(*rrr)

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")