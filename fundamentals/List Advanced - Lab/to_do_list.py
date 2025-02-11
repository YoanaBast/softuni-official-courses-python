to_do_list = []
command = input()
while command != 'End':
    to_do_list.append(command)

    command = input()

sorted_list = sorted(to_do_list)
final_list = []
for item in sorted_list:
    final_list.append(item[2::])

print(final_list)