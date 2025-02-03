first_list = input().split()
second_list = []
for item in first_list:
    second_list.append(abs(float(item)))
print(second_list)