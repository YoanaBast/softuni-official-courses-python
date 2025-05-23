rows = cols = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
alive = []

# Parse bomb coordinates as list of [int, int] pairs
coordinates = [[int(x) for x in coor.split(',')] for coor in input().split()]

for r, c in coordinates:
    if matrix[r][c] > 0:
        bomb = matrix[r][c]
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if 0 <= row < rows and 0 <= col < cols and matrix[row][col] > 0:
                    matrix[row][col] -= bomb

# Collect alive cells
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] > 0:
            alive.append(matrix[row][col])

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")

for r in matrix:
    print(*r)

"""
rows = cols = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
alive = []

coordinates = input().split(' ')
for coor in coordinates: #[1,2] [2,1] [2,0]
    r, c = [int(x) for x in coor.split(',')] # r = 1, c = 2
    if r < rows and c < cols:
        bomb = matrix[r][c]

    for row in range(rows): #0-3
        for col in range(cols): #0-3

            if [row, col] not in coordinates and matrix[row][col] > 0: #not the bomb

                if row == r - 1 or row == r or row ==  r + 1:
                    if col == c - 1 or col == c or col == c + 1:
                        matrix[row][col] -= bomb

for row in range(rows): #0-3
    for col in range(cols): #0-3
        if matrix[row][col] > 0:
            alive.append(matrix[row][col])

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")

for rrr in matrix:
    print(*rrr)
"""