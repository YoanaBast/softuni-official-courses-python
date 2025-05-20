row, column = [int(x) for x in input().split(', ')]

matrix = [
    [int(data) for data in input().split(' ')]
    for r in range(row)
]
sum = 0
columns_summed = []

for i in range(len(matrix[0])): # 0-5 == roww
    for roww in matrix:  #list1, list2
        sum += roww[i]
    columns_summed.append(sum)
    sum = 0

print(*columns_summed, sep='\n')