age = float(input())
gender = input()

age_of_16 = age >= 16
if age_of_16 is True:
    if gender == 'm':
        print("Mr.")
    elif gender == 'f':
        print("Ms.")
elif age_of_16 is False:
    if gender == 'm':
        print("Master")
    elif gender == 'f':
        print("Miss")
