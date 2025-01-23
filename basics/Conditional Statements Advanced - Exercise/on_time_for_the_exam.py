exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_all_minutes = (exam_hour * 60) + exam_minute
arrive_all_minutes = (arrive_hour * 60) + arrive_minute

difference = exam_all_minutes - arrive_all_minutes
abs_difference = abs(difference)
format_difference_minutes = str(abs_difference % 60)
while len(format_difference_minutes) < 2:
    format_difference_minutes = '0' + format_difference_minutes

is_early = 0 < difference > 30
is_on_time = 0 <= difference <= 30
is_late = difference < 0

if is_early == True:
    print('Early')
    if difference < 60:
        print(f'{abs(difference)} minutes before the start')
    else:
        print(f'{difference // 60}:{format_difference_minutes} hours before the start')

elif is_on_time == True:
    print('On time')
    print(f'{abs(difference)} minutes before the start')

elif is_late == True:
    print('Late')
    if abs_difference < 60:
        print(f'{abs_difference} minutes after the start')
    else:
        print(f'{abs_difference // 60}:{format_difference_minutes} hours after the start')
