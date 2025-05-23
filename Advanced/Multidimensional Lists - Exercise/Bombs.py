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
