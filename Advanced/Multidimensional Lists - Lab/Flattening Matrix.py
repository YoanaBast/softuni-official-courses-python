matrix = [
    [int(x) for x in input().split(', ')] for row in range(int(input()))
]

flat = []
for row in matrix:
    flat.extend(row)
print(flat)