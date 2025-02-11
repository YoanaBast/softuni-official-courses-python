version = input().split('.')
list_ver = [int(item) for item in version]

if list_ver[2] < 9:
    list_ver[2] += 1
elif list_ver[2] == 9:
    list_ver[2] = 0
    if list_ver[1] < 9:
        list_ver[1] += 1
    elif list_ver[1] == 9:
        list_ver[1] = 0
        list_ver[0] += 1
separator = '.'
print(separator.join(map(str, list_ver)))
