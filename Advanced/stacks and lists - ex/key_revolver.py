from collections import deque

bullet_price = int(input())
gun_barrel_static = int(input())
bullets = [int(x) for x in input().split()] #LIFO
locks = deque(int(x) for x in input().split()) #FIFO
int_value = int(input())

gun_barrel = gun_barrel_static

while locks and bullets:
    if locks[0] >= bullets[-1]:
        print('Bang!')
        locks.popleft()
        bullets.pop()
        gun_barrel -= 1
        int_value -= bullet_price
    else:
        print('Ping!')
        bullets.pop()
        gun_barrel -= 1
        int_value -= bullet_price
    if bullets:
        if gun_barrel == 0:
            print('Reloading!')
            gun_barrel = gun_barrel_static


if locks:
    locks_left = len(locks)
    print(f"Couldn't get through. Locks left: {locks_left}")
else:
    bullets_left = len(bullets)
    print(f"{bullets_left} bullets left. Earned ${int_value}")

