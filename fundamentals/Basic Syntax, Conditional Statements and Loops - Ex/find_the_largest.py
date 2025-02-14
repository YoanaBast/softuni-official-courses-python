num = int(input())
list = list(str(num))
list_sorted = sorted(list, reverse=True)
print(''.join(list_sorted))