import sys
n = int(input())
max = -sys.maxsize
min = sys.maxsize

for _ in range(n):
    new_n = int(input())
    if new_n > max:
        max = new_n
    if new_n < min:
        min = new_n

print(f'Max number: {max}')
print(f'Min number: {min}')