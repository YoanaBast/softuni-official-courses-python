students = int(input())
dict = {} # {'Alex': [2.0], 'Mark': [5.5, 2.5, 3.46], 'Peter': [5.2, 3.2]}
for _ in range(students):
    name, grade = input().split()
    if name not in dict.keys():
        dict[name] = [float(grade)]
    else:
        dict[name].append(float(grade))

for student in dict:
    average = sum(dict[student]) / len(dict[student])
    print(f'{student} -> ', end='')
    for grade in dict[student]:
        print(f'{grade:.2f} ', sep=' ', end='')
    print(f'(avg: {average:.2f})')


