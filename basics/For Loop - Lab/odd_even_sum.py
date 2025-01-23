n = int(input())
sum_even = 0
sum_odd = 0

for idx in range(n):
    new_n = int(input())
    if idx % 2 == 0:
        sum_even += new_n
    elif idx % 2 == 1:
        sum_odd += new_n

if sum_odd == sum_even:
    print('Yes')
    print(f'Sum = {sum_even}')
elif sum_odd != sum_even:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')