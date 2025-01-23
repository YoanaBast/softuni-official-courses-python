num = int(input()) #n na broi chisla

total = 0
biggest_num = 0

for _ in range(num):
    current_num = int(input())

    total += current_num
    if current_num > biggest_num:
        biggest_num = current_num

if biggest_num == total - biggest_num:
    print("Yes")
    print(f"Sum = {biggest_num}")
else:
    print("No")
    print(f'Diff = {abs(biggest_num - (total - biggest_num))}')
