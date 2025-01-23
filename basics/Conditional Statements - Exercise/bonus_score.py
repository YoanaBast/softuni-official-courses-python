num = int(input())

bonus = 0

if num <= 100:
    bonus = 5
elif num > 100 and num <= 1000:
    bonus = num * 0.20
elif num > 1000:
    bonus = num * 0.10

add_bonus = 0
if num % 2 == 0:
    add_bonus = 1
if num % 10 == 5:
    add_bonus = 2

total_bonus = bonus + add_bonus
print(total_bonus)
print(num + total_bonus)