rows, columns = [int(x) for x in input().split(', ')] #judge ne go haresva

matrix = [
    [int(data) for data in input().split(', ')]
    for _ in range(rows)
]

summed = 0
for row in matrix: # 0 1 2
    for data in row: # 7, 1, 3, 3, 2, 1
        summed += data

print(summed)
print(matrix)