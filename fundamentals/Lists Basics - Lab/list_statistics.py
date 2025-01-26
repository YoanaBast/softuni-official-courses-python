n = int(input())

pos = []
neg = []

for x in range(n):
    new_n = int(input())

    if new_n < 0:
        neg.append(new_n)
    else:
        pos.append(new_n)

print(pos)
print(neg)
print(f'Count of positives: {len(pos)}')
print(f'Sum of negatives: {sum(neg)}')