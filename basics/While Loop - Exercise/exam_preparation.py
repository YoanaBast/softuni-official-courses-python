bad_grades = int(input())
command = input()
grade = 0
fail = 0
ex_count = 0
total_grade = 0
last_ex = ''

while command != 'Enough':
    name = command
    grade = int(input())

    if grade <= 4:
        fail += 1
        if fail >= bad_grades:
            break


    ex_count += 1
    total_grade += grade
    last_ex = name

    command = input()



if fail >= bad_grades:
    print(f"You need a break, {fail} poor grades.")
else:
    print(f"Average score: {(total_grade / ex_count):.2f}")
    print(f"Number of problems: {ex_count}")
    print(f"Last problem: {last_ex}")



# Issues:
# grade is not updated before the if condition check:
# The condition if grade <= 4: appears before grade is assigned a value inside the loop. Initially, grade is 0, so it will always count as a failure on the first iteration.