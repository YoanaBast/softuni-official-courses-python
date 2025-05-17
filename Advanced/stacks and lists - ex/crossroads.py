from collections import deque
green = int(input())
free = int(input())
safe  =  green + free
cars = deque([])
no_crash = True
passed = 0

while True:
    command = input()
    if command == 'END':
        break
    cars.append(command)

time_left = safe
while cars:
    if cars[0] == 'green':
        time_left = safe
        cars.popleft()
        continue
    car_len = len(cars[0])
    if time_left >= free: #car goes
        if car_len <= time_left:
            cars.popleft()
            time_left -= car_len
            passed += 1
        else:
            crash = cars[0][time_left]
            no_crash = False
            print('A crash happened!')
            print(f'{cars[0]} was hit at {crash}.')
            break
    else:
        cars.popleft()

if no_crash:
    print(f'Everyone is safe.\n{passed} total cars passed the crossroads.')

