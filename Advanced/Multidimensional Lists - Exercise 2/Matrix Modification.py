rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        for m in matrix:
            print(*m)
        break

    r, c, v = int(command[1]), int(command[2]), int(command[3])
    if r < 0 or r >= rows\
        or c < 0 or c >= len(matrix[0]):
        print("Invalid coordinates")
        continue

    elif command[0] == 'Add':
        matrix[r][c] += v

    elif command[0] == 'Subtract':
        matrix[r][c] -= v
