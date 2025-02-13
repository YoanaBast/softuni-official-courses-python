list = input().split(', ')

pos = [item for item in list if int(item) >= 0]
neg =[item for item in list if int(item) < 0]
even = [item for item in list if int(item) % 2 == 0]
odd = [item for item in list if int(item) % 2 != 0]

print(f"Positive: {', '.join(pos)}")
print(f'Negative: {", ".join(neg)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')