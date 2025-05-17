n = int(input())
curr_row= 0
set_odd = set()
set_even = set()

for _ in range(n):
    curr_row += 1
    ascii = []

    name = input()
    for chr in name:
        ascii.append(ord(chr))
    res = sum(ascii) // curr_row
    if res % 2 == 0:
        set_even.add(res)
    else:
        set_odd.add(res)

sum_odd = sum(set_odd)
sum_even = sum(set_even)

if sum_odd == sum_even:
    final = set_odd | set_even
elif sum_odd > sum_even:
    final = set_odd - set_even
elif sum_even > sum_odd:
    final = set_even ^ set_odd

print(', '.join(str(f) for f in final))
