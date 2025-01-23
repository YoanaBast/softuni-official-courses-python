hour = int(input())
minute = int(input())

hour_in_minute = hour * 60
total_minutes = hour_in_minute + minute

after_15 = total_minutes + 15

final_hour = after_15 // 60
final_minute = after_15 % 60

if final_hour == 24:
    final_hour = 0

if final_minute < 10:
    print(f'{final_hour}:0{final_minute}')
elif final_minute >= 10:
    print(f'{final_hour}:{final_minute}')