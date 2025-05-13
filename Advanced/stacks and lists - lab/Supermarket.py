from collections import deque

Q = deque([])

while True:
    command = input()
    if command == 'End':
        print(f'{len(Q)} people remaining.')
        break
    elif command == 'Paid':
        while Q:
            print(Q.popleft())
    else:
        Q.append(command)
