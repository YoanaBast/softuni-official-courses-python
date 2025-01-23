n = int(input())
lqv_sum = 0
desen_sum = 0

for _ in range(n):
    new_lqv_n = int(input())
    lqv_sum += new_lqv_n
for _ in range(n):
    new_desen_n = int(input())
    desen_sum += new_desen_n

if lqv_sum == desen_sum:
    print(f'Yes, sum = {lqv_sum}')
elif lqv_sum != desen_sum:
    print(f'No, diff = {abs(lqv_sum - desen_sum)}')