# 3. Elevator
#
# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

# n_persons = int(input())
# capacity = int(input())
#
# result = n_persons / capacity
# print(round(result))

from math import ceil
n_persons = int(input())
capacity = int(input())
result = ceil(n_persons / capacity)
print(round(result))