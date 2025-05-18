from collections import deque
wasted = 0

cups = deque([int(x) for x in input().split()]) #Fifo
bottles  = [int(y) for y in input().split()] #lifO

while cups and bottles:

    curr_bottle = bottles.pop() #5
    cups[0] -= curr_bottle # 3-5 = -2

    if cups[0] <= 0:
        if cups[0] < 0:
            wasted += abs(cups[0]) #2
        cups.popleft()

if cups:
    print('Cups:' + ' ', end='')
    for cup in cups:
        print(str(cup) + ' ', end='')
elif bottles:
    print('Bottles:' + ' ', end='')
    for bot in bottles:
        print(str(bot) + ' ', end='')
print(f'\nWasted litters of water: {wasted}')