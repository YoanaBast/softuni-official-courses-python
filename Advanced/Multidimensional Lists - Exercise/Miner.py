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