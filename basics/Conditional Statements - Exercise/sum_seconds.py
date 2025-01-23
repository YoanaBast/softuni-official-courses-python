time_first = int(input())
time_second = int(input())
time_third = int(input())

total = time_third + time_second + time_first

total_minutes = total // 60
total_seconds = total % 60
if total_seconds < 10:
    print(f'{total_minutes}:0{total_seconds}')
elif total_seconds >= 10:
    print(f'{total_minutes}:{total_seconds}')
