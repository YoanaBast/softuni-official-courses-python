from collections import deque

rows = cols = int(input())
moves = deque(input().split())
matrix = []
unmined_coal = 0

for row in range(rows):
    data = [x for x in input().split()]
    matrix.append(data)
    if 's' in data:
        start_row =  row
        start_col = data.index('s')
    if 'c' in data:
        unmined_coal += data.count('c')

coal = 0
moved = False
ended = False
no_coal = False

while moves:
    if ended or no_coal:
        break

    moved = False
    for r in range(start_row - 1, start_row + 1 + 1):
        for c in range(start_col - 1, start_col + 1 + 1):

            if (moves[0] == 'up' and r == start_row - 1 and c == start_col)\
            or (moves[0] == 'down' and r == start_row + 1 and c == start_col)\
            or (moves[0] == 'left' and r == start_row and c == start_col - 1)\
            or (moves[0] == 'right' and r == start_row and c == start_col + 1):
                if (moves[0] == "right" and start_col + 1 >= len(matrix[0]))\
                or (moves[0] == "down" and  start_row + 1 >= len(matrix))\
                or r < 0 or c < 0:
                    moves.popleft()
                    break

                if matrix[r][c] == 'e':
                    ended = True

                elif matrix[r][c] == 'c':
                    coal += 1
                    unmined_coal -= 1
                    matrix[r][c] = '*'
                    if unmined_coal == 0:
                        no_coal = True

                matrix[r][c], matrix[start_row][start_col] = matrix[start_row][start_col], matrix[r][c]
                start_row, start_col = r, c
                moves.popleft()
                moved = True
                break

        if moved:
                break

if no_coal:
    print(f"You collected all coal! ({start_row}, {start_col})")
elif ended:
    print(f"Game over! ({start_row}, {start_col})")
elif not moves:
    print(f"{unmined_coal} pieces of coal left. ({start_row}, {start_col})")



"""
from collections import deque

rows = int(input())
moves = deque(input().split())
matrix = []
unmined_coal = 0
start_row = start_col = 0

# Read matrix and find starting position and coal count
for row in range(rows):
    data = input().split()
    matrix.append(data)
    if 's' in data:
        start_row = row
        start_col = data.index('s')
    unmined_coal += data.count('c')

# Directions map
directions = {
    'up':    (-1, 0),
    'down':  (1, 0),
    'left':  (0, -1),
    'right': (0, 1)
}

while moves:
    move = moves.popleft()
    dr, dc = directions[move]
    new_row, new_col = start_row + dr, start_col + dc

    # Check bounds
    if not (0 <= new_row < rows and 0 <= new_col < len(matrix[0])):
        continue

    cell = matrix[new_row][new_col]

    if cell == 'e':
        print(f"Game over! ({new_row}, {new_col})")
        break
    elif cell == 'c':
        unmined_coal -= 1
        matrix[new_row][new_col] = '*'
        if unmined_coal == 0:
            print(f"You collected all coal! ({new_row}, {new_col})")
            break

    # Move the player
    matrix[start_row][start_col] = '*'
    matrix[new_row][new_col] = 's'
    start_row, start_col = new_row, new_col
else:
    print(f"{unmined_coal} pieces of coal left. ({start_row}, {start_col})")
"""