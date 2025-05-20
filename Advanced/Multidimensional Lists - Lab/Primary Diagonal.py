num = int(input())

matrix = [
    [int(x) for x in input().split()] for row in range(num)
]

column_index, sumi = 0, 0

for row_index in range(num): # 0 1 2
    sumi += matrix[row_index][column_index]
    column_index += 1

print(sumi)