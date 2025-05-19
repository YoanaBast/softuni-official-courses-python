from collections import deque

choco = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while choco and milk and milkshakes < 5:
    #curr_choc = choco[-1]
    # milk[0] e current milk

    if choco[-1] <= 0 and milk[0] <= 0:
        choco.pop()
        milk.popleft()
        continue

    if choco[-1] <= 0:
        choco.pop()
        continue

    if  milk[0] <= 0:
        milk.popleft()
        continue

    if choco[-1] == milk[0]:
        milk.popleft()
        choco.pop()
        milkshakes += 1

    else:
        milk.rotate(-1)
        choco[-1] -= 5

        if choco[-1] <= 0:
            choco.pop()

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

choco_str = map(str, choco)
if choco:
    print(f"Chocolate: {', '.join(choco_str)}")
else:
    print("Chocolate: empty")

milk_str = map(str, milk)
if milk:
    print(f"Milk: {', '.join(milk_str)}")
else:
    print("Milk: empty")
