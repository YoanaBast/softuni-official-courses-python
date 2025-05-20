fruit = ['apple', 'banana']
# start[0] = start[0][:-1]
fruit[0] = fruit[0][:-1]
fruit[-1] = fruit[-1][:-1]

print(fruit)
# #['appl', 'banana']

# list = [1, 2, 3]   # ✅ valid, but bad practice — "list" is a built-in type
# list = [4, 5, 6]   # now 'list' points to a different list
# print(list)

# start = [10, 20, 30, 40, 50]
# middle = 2
#
# left = start[0:middle + 1]     # [10, 20, 30]
# right = start[middle + 1:]     # [40, 50]
#
# print(left)
# print(right)