courses = {}
#totals course: 2
#main course: [student, stident]

def nice_print_gg(main_dict, totals_dict):
    result = []
    for key, value in totals_dict.items():
        result.append(f"{key}: {value}")
        for people in main_dict[key]:
            result.append(f"-- {people}")
    return '\n'.join(result)


while True:
    command = input()
    if command == 'end':
        break
    course_key, person_value = command.split(' : ')
    if course_key not in courses:
        courses[course_key] = []
    if person_value not in courses:
        courses[course_key].append(person_value)
    else:
        continue

courses_totals = {}
for course in courses:
    students = len(courses[course])
    courses_totals[course] = int(students)

print(nice_print_gg(courses, courses_totals))