students_grades_dict = {}


def get_grades(times):
    for _ in range(times):
        name = input()
        grade = float(input())
        if name not in students_grades_dict:
            students_grades_dict[name] = []
        students_grades_dict[name].append(grade)

def average_grade(dict):
    for student in dict:
        grades = sum(dict[student]) / len(dict[student])
        students_grades_dict[student] = grades
    return students_grades_dict

def sort_failed_out(some_dict):
    some_dict = dict(filter(lambda item: item[1] >= 4.50, some_dict.items()))
    return some_dict

def nice_print(sorted_dict: dict):
    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key} -> {value:.2f}")
    return '\n'.join(result)


students_num = int(input())
get_grades(students_num)
average_grade(students_grades_dict)
students_grades_dict = sort_failed_out(students_grades_dict)
print(nice_print(students_grades_dict))
