# Write a program that receives a number and creates the following pattern. The number represents the largest count of stars on one row.

n = int(input())

for rotate in range(n+1):
    print('*' * rotate)
for rotate_reverse in range(n-1, 0, -1):
    print('*' * rotate_reverse)
