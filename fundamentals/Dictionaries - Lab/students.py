students = {}
sorted = {}

def set_dict(user_input: str):
    name, ID, course = user_input.split(':')
    students[name] = {}
    students[name]['ID'] = ID
    students[name]['course'] = course
    return students

def nice_print_key_value(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key} - {value}")
    return '\n'.join(result)

def sorting(lookup: str):
    for student in students:
        if students[student]['course'] == lookup:
            sorted[student] = students[student]['ID']
    return nice_print_key_value(sorted)

while True:
    command = input()
    if ':' not in command:
        course_lookup = ' '.join(command.split('_'))
        break
    else:
        set_dict(command)

print(sorting(course_lookup))