matrix = [
    [int(x) for x in input().split(', ') if int(x) % 2 == 0] for row in range(int(input()))
]
print(matrix)