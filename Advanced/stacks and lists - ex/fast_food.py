from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders and orders[0] <= food:
    food -= orders[0]
    orders.popleft()

printable = ' '.join(map(str, orders))
if not orders:
    print('Orders complete')
else:
    print(f'Orders left: {printable}')