matrix = [
    list(input())
    for _ in range(int(input()))
]

tracy = input()
R, C = -1, -1
found = False

for row in matrix: # list1 list 2
    if C >= 0:
        break
    R += 1
    if tracy in row:
        for char in row:
            if char == tracy:
                C = row.index(char)
                found = True
                break
    if found: # this is for the edge case where Tracy is the last in row, to skip the else statement below
        break

else:
    print(f"{tracy} does not occur in the matrix")

if found:
    print((R, C))
