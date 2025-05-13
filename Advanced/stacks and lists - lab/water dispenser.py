from collections import deque

queue = deque([])
quantity = int(input())

while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)

while True:
    command = input().split()
    if command[0] == 'End':
        print(f'{quantity} liters left')
        break

    elif command[0].isdigit():
        if int(command[0]) <= quantity:
            quantity -= int(command[0])
            print(f'{queue.popleft()} got water')
            
        elif  int(command[0]) > quantity:
            print(f'{queue.popleft()} must wait')

    elif command[0] == 'refill':
        quantity += int(command[1])