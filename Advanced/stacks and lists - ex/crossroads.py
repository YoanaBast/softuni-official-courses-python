from collections import deque

green_light_dur = int(input())
free_win_duration = int(input())

queue = deque()

total_passed = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        time_left = green_light_dur

        while queue and time_left > 0:
            car = queue.popleft()
            car_length = len(car)

            if car_length <= time_left:
                time_left -= car_length
                total_passed += 1
            else:
                # Check if it can still pass during the free window
                if car_length <= time_left + free_win_duration:
                    total_passed += 1
                    break  # green time and window consumed
                else:
                    # Crash occurs
                    crash_index = time_left + free_win_duration
                    crash_letter = car[crash_index]
                    print("A crash happened!")
                    print(f"{car} was hit at {crash_letter}.")
                    crash = True
                    break
        if crash:
            break
    else:
        queue.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{total_passed} total cars passed the crossroads.")
